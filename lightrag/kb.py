"""
Interogheaza baza de cunostinte TBF din terminal.

Exemple:
    python kb.py "Ce am scris despre nerezonabil si ce studii il sustin?"
    python kb.py -m global "Ce pattern-uri apar in fundamentele despre leadership?"
    python kb.py -m local "Ce spune Aaker despre diferentiere?"

Moduri (-m):
    mix     (implicit) graf + vectori, cel mai complet
    local   fapte precise, potrivire pe entitati
    global  teme largi, rationament intre documente
    hybrid  local + global
    naive   doar cautare vectoriala clasica

--context : intoarce DOAR dovezile regasite (concepte + relatii + fragmente-sursa
            cu citari), fara ca LightRAG sa genereze raspunsul. Util cand sintetizeaza
            altcineva (ex. Claude) raspunsul din materialul brut.
"""

import argparse
import asyncio

from lightrag import QueryParam
from kb_lib import build_rag, QUERY_MODEL


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("intrebare", help="intrebarea ta, in romana")
    ap.add_argument("-m", "--mode", default="mix",
                    choices=["mix", "local", "global", "hybrid", "naive"])
    ap.add_argument("--no-refs", action="store_true", help="fara lista de surse")
    ap.add_argument("--context", action="store_true",
                    help="intoarce doar dovezile regasite, fara raspuns generat")
    args = ap.parse_args()

    rag = await build_rag(for_query=True)
    try:
        param = QueryParam(
            mode=args.mode,
            include_references=not args.no_refs,
            response_type="Multiple Paragraphs",
            only_need_context=args.context,
        )
        if not args.context:
            print(f"\n[model: {QUERY_MODEL} | mod: {args.mode}]\n")
        ans = await rag.aquery(args.intrebare, param=param)
        print(ans)
    finally:
        await rag.finalize_storages()


if __name__ == "__main__":
    asyncio.run(main())
