"""
Indexare incrementala a continutului in LightRAG.

- Parcurge fisiere .md din content/ (sau o lista data).
- Pastreaza atribuirea sursei (scriere proprie vs studiu) ca antet de context,
  ca extractia sa stie ce citeste si sa lege corect "ce a scris Razvan" de "studiul din spate".
- Foloseste un manifest (manifest.json) ca sa reindexeze DOAR fisierele noi sau modificate.
  Asta acopera cerinta "toata informatia care exista SAU VA EXISTA in content/".

Exemple:
    # pilot pe o lista de fisiere
    python ingest.py --files pilot_files.txt
    # tot folderul raw + papers (indexarea completa)
    python ingest.py --dirs raw papers
    # un singur subfolder
    python ingest.py --dirs raw/fundamente
"""

import argparse
import asyncio
import hashlib
import json
import os
import sys

from kb_lib import CONTENT_ROOT, WORKING_DIR, build_rag

MANIFEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "manifest.json")


def parse_frontmatter(text: str):
    """Intoarce (dict_frontmatter, corp) pentru un fisier markdown cu YAML simplu."""
    fm, body = {}, text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            raw = text[3:end].strip()
            body = text[end + 4:].lstrip("\n")
            for line in raw.splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def source_header(relpath: str, fm: dict) -> str:
    """Antet de context pentru extractie, in functie de tipul sursei."""
    if relpath.startswith("papers/"):
        autori = fm.get("autori", "autor necunoscut")
        an = fm.get("an", "")
        jurnal = fm.get("jurnal", "")
        titlu = fm.get("titlu", "")
        meta = ", ".join(p for p in [f"{autori} ({an})" if an else autori, jurnal] if p)
        return (f"[SURSA: studiu academic, rezumat in romana, legat de scrierile lui Razvan. "
                f"{meta}. {titlu}]")
    if relpath.startswith("raw/cursuri/"):
        return f"[SURSA: curs TBF scris de Razvan Cazanescu. Fisier: {relpath}]"
    if relpath.startswith("raw/fundamente/"):
        return (f"[SURSA: scriere proprie a lui Razvan Cazanescu — Fundament "
                f"#{fm.get('numar','?')}, {fm.get('data','')}]")
    if relpath.startswith("raw/filozofii/"):
        return (f"[SURSA: scriere proprie a lui Razvan Cazanescu — Filozofie "
                f"#{fm.get('numar','?')}, {fm.get('data','')}]")
    if relpath.startswith("raw/ganduri/"):
        return f"[SURSA: gand/scriere personala a lui Razvan Cazanescu. Fisier: {relpath}]"
    return f"[SURSA: {relpath}]"


def doc_id_for(relpath: str) -> str:
    return "tbf-" + hashlib.sha1(relpath.encode("utf-8")).hexdigest()[:16]


def collect_files(args) -> list[str]:
    paths = []
    if args.files:
        with open(args.files, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    paths.append(os.path.join(CONTENT_ROOT, line))
    for d in args.dirs or []:
        root = os.path.join(CONTENT_ROOT, d)
        for dirpath, _, names in os.walk(root):
            for n in sorted(names):
                if n.endswith(".md"):
                    paths.append(os.path.join(dirpath, n))
    # dedup pastrand ordinea
    seen, out = set(), []
    for p in paths:
        ap = os.path.abspath(p)
        if ap not in seen and os.path.isfile(ap):
            seen.add(ap)
            out.append(ap)
    return out


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--files", help="fisier text cu cai relative la content/, una pe linie")
    ap.add_argument("--dirs", nargs="*", help="subfoldere din content/ de indexat")
    ap.add_argument("--force", action="store_true", help="reindexeaza chiar daca nu s-a schimbat")
    args = ap.parse_args()

    files = collect_files(args)
    if not files:
        print("Niciun fisier de indexat. Foloseste --files sau --dirs.")
        sys.exit(1)

    manifest = {}
    if os.path.exists(MANIFEST):
        manifest = json.load(open(MANIFEST, encoding="utf-8"))

    to_insert, contents, ids, file_paths, changed_ids = [], [], [], [], []
    for ap_path in files:
        rel = os.path.relpath(ap_path, CONTENT_ROOT)
        raw = open(ap_path, encoding="utf-8").read()
        h = hashlib.sha1(raw.encode("utf-8")).hexdigest()
        if not args.force and manifest.get(rel, {}).get("hash") == h:
            continue  # neschimbat -> sarim
        fm, body = parse_frontmatter(raw)
        did = doc_id_for(rel)
        if rel in manifest:  # modificat -> stergem versiunea veche din graf
            changed_ids.append(did)
        text = f"{source_header(rel, fm)}\n\n{body}"
        contents.append(text)
        ids.append(did)
        file_paths.append(rel)
        to_insert.append((rel, h, did))

    print(f"Fisiere candidate: {len(files)} | de (re)indexat: {len(to_insert)} | "
          f"neschimbate sarite: {len(files) - len(to_insert)}")
    if not to_insert:
        print("Nimic de facut. Graful e la zi.")
        return

    rag = await build_rag(for_query=False)
    try:
        for did in changed_ids:
            try:
                await rag.adelete_by_doc_id(did)
            except Exception as e:
                print(f"  (avertisment: nu am putut sterge {did}: {e})")

        print(f"Indexare {len(contents)} documente cu extractie pe graf (poate dura)...")
        await rag.ainsert(contents, ids=ids, file_paths=file_paths)

        # Marcam in manifest DOAR ce a procesat efectiv LightRAG cu succes.
        # Docurile esuate raman in afara manifestului -> se reincearca automat
        # la urmatoarea rulare a ingest.py (retry incremental, fara batai de cap).
        status_path = os.path.join(WORKING_DIR, "kv_store_doc_status.json")
        processed_ids = set()
        if os.path.exists(status_path):
            ds = json.load(open(status_path, encoding="utf-8"))
            processed_ids = {k for k, v in ds.items() if v.get("status") == "processed"}

        ok = [(r, h, d) for (r, h, d) in to_insert if d in processed_ids]
        failed = [(r, d) for (r, h, d) in to_insert if d not in processed_ids]
        for rel, h, did in ok:
            manifest[rel] = {"hash": h, "doc_id": did}
        json.dump(manifest, open(MANIFEST, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

        print(f"Procesate OK: {len(ok)} | manifest: {len(manifest)} documente urmarite.")
        if failed:
            print(f"ESUATE (se reincearca la urmatoarea rulare): {len(failed)}")
            for rel, did in failed[:20]:
                print(f"  - {rel}")
        print(f"Storage: {WORKING_DIR}")
    finally:
        await rag.finalize_storages()


if __name__ == "__main__":
    asyncio.run(main())
