"""
Configurare partajata pentru baza de cunostinte TBF (LightRAG).

Aici se decide: ce modele OpenAI folosim, cum embeddings, in ce limba extragem
si ce tipuri de entitati cautam in scrierile lui Razvan + studiile legate.

Folosit de ingest.py (indexare) si kb.py (interogare).
"""

import os
from functools import partial

from dotenv import load_dotenv
from lightrag import LightRAG
from lightrag.llm.openai import openai_complete_if_cache, openai_embed
from lightrag.utils import EmbeddingFunc

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"), override=False)

# --- Cai ---
HERE = os.path.dirname(os.path.abspath(__file__))
WORKING_DIR = os.getenv("WORKING_DIR", os.path.join(HERE, "rag_storage"))
CONTENT_ROOT = os.getenv("CONTENT_ROOT", os.path.join(os.path.dirname(HERE), "content"))

# --- Modele (vezi .env) ---
EXTRACT_MODEL = os.getenv("EXTRACT_MODEL", "gpt-5.4")   # construieste graful (fundatia)
QUERY_MODEL = os.getenv("QUERY_MODEL", "gpt-5.4")       # genereaza raspunsurile
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-large")
EMBEDDING_DIM = int(os.getenv("EMBEDDING_DIM", "3072"))

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

# Limba in care se rezuma/eticheteaza tot ce intra in graf.
SUMMARY_LANGUAGE = os.getenv("SUMMARY_LANGUAGE", "Romanian")

# --- Ce tipuri de entitati extragem ---
# Adaptat domeniului lui Razvan (management/business/psihologie) + studiilor.
# Inlocuieste tipurile implicite (Person/Location/...) care ar fragmenta graful.
ENTITY_TYPES_GUIDANCE = """Clasifica fiecare entitate cu unul dintre tipurile de mai jos. Daca niciunul nu se potriveste, foloseste `Altele`.

- Concept: idee, notiune sau distinctie de business/management/psihologie (ex: "nerezonabilul", "norma pietei", diferentiere, brand, X-factor). Pastreaza numele exact folosit in text, nu il traduce in engleza.
- Principiu: regula sau maxima de actiune ("nu lauda omul, lauda comportamentul").
- Metoda: procedura, tehnica, proces sau sistem aplicabil (ex: sistemul TBF de management, proces de vanzare, bugetare).
- CadruConceptual: model, teorie sau framework numit (ex: leverage points, loss aversion).
- Autor: cercetator sau autor citat intr-un studiu (ex: Aaker, Donella Meadows).
- Studiu: o lucrare/cercetare academica anume (cu an si jurnal cand exista).
- Organizatie: companie, institutie, grup.
- Persoana: individ uman (altul decat un autor citat).
- Metrica: indicator, cifra, statistica relevanta.
- Altele: orice nu se incadreaza mai sus."""


def make_llm_func(model_name: str):
    """Construieste o functie LLM legata la un model OpenAI anume."""

    async def _llm(prompt, system_prompt=None, history_messages=None, **kwargs):
        # Modelele gpt-5.x de reasoning accepta doar temperature implicita (1).
        # Eliminam orice temperature trimisa de LightRAG ca sa evitam erori.
        kwargs.pop("temperature", None)
        return await openai_complete_if_cache(
            model_name,
            prompt,
            system_prompt=system_prompt,
            history_messages=history_messages or [],
            api_key=API_KEY,
            base_url=BASE_URL,
            **kwargs,
        )

    return _llm


def make_embedding_func() -> EmbeddingFunc:
    return EmbeddingFunc(
        embedding_dim=EMBEDDING_DIM,
        max_token_size=int(os.getenv("MAX_EMBED_TOKENS", "8192")),
        func=partial(
            openai_embed.func,  # functia neimpachetata, ca sa nu dublam EmbeddingFunc
            model=EMBEDDING_MODEL,
            api_key=API_KEY,
            base_url=BASE_URL,
        ),
    )


async def build_rag(for_query: bool = False) -> LightRAG:
    """Creeaza si initializeaza o instanta LightRAG gata de folosit.

    for_query=True -> foloseste QUERY_MODEL; altfel EXTRACT_MODEL.
    """
    if not API_KEY:
        raise RuntimeError(
            "OPENAI_API_KEY lipseste. Exporta-l in shell sau pune-l in lightrag/.env"
        )

    os.makedirs(WORKING_DIR, exist_ok=True)
    model = QUERY_MODEL if for_query else EXTRACT_MODEL

    rag = LightRAG(
        working_dir=WORKING_DIR,
        llm_model_func=make_llm_func(model),
        llm_model_name=model,
        llm_model_max_async=int(os.getenv("MAX_ASYNC_LLM", "4")),
        embedding_func=make_embedding_func(),
        embedding_func_max_async=int(os.getenv("MAX_ASYNC_EMBED", "8")),
        max_parallel_insert=int(os.getenv("MAX_PARALLEL_INSERT", "2")),
        entity_extract_max_gleaning=int(os.getenv("MAX_GLEANING", "1")),
        addon_params={
            "language": SUMMARY_LANGUAGE,
            "entity_types_guidance": ENTITY_TYPES_GUIDANCE,
        },
    )
    await rag.initialize_storages()
    return rag
