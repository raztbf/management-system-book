"""
Reia procesarea documentelor ramase FAILED/PENDING dupa o intrerupere
(ex. cascada de rate-limit). NU re-insereaza continut — docurile sunt deja
in coada; doar reia pipeline-ul. Foloseste concurenta redusa (din .env / env).

Dupa ce termina, reconciliaza manifest.json sa reflecte DOAR docurile
'processed' (ca incrementalul viitor sa fie corect).

Rulare:
    MAX_ASYNC_LLM=3 MAX_ASYNC_EMBED=2 MAX_PARALLEL_INSERT=2 \
      .venv/bin/python retry_failed.py
"""

import asyncio
import hashlib
import json
import os
from collections import Counter

from kb_lib import CONTENT_ROOT, WORKING_DIR, build_rag

MANIFEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "manifest.json")
STATUS = os.path.join(WORKING_DIR, "kv_store_doc_status.json")


def status_counts():
    d = json.load(open(STATUS, encoding="utf-8"))
    return Counter(v.get("status") for v in d.values()), d


async def main():
    before, _ = status_counts()
    print("Inainte de retry:", dict(before))

    rag = await build_rag(for_query=False)
    try:
        print("Reiau coada (FAILED/PENDING) cu concurenta redusa...")
        await rag.apipeline_process_enqueue_documents()
    finally:
        await rag.finalize_storages()

    after, ds = status_counts()
    print("Dupa retry:", dict(after))

    # Reconciliem manifestul: doar docurile 'processed' raman marcate ca gata.
    # ATENTIE: in doc_status, file_path e DOAR basename-ul (ex. 'fundament-0988.md'),
    # nu relpath-ul ('raw/fundamente/...'). Asa ca NU reconstruim din file_path
    # (ar da join gresit -> manifest gol). Mergem invers: parcurgem content/,
    # calculam doc_id-ul determinist al fiecarui fisier si il pastram daca acel
    # doc_id e 'processed' in doc_status.
    processed_ids = {
        k for k, v in ds.items() if v.get("status") == "processed"
    }
    manifest = {}
    rebuilt = 0
    for dirpath, _, names in os.walk(CONTENT_ROOT):
        for n in names:
            if not n.endswith(".md"):
                continue
            ap = os.path.join(dirpath, n)
            rel = os.path.relpath(ap, CONTENT_ROOT)
            did = "tbf-" + hashlib.sha1(rel.encode("utf-8")).hexdigest()[:16]
            if did in processed_ids:
                h = hashlib.sha1(open(ap, encoding="utf-8").read().encode("utf-8")).hexdigest()
                manifest[rel] = {"hash": h, "doc_id": did}
                rebuilt += 1
    json.dump(manifest, open(MANIFEST, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Manifest reconciliat: {rebuilt} documente 'processed' urmarite.")
    still = after.get("failed", 0) + after.get("pending", 0)
    if still:
        print(f"Inca de reluat: {still} (re-ruleaza scriptul daca a mai ramas).")


if __name__ == "__main__":
    asyncio.run(main())
