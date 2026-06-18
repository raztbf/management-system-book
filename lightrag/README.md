# Baza de cunostinte TBF — LightRAG

Graf de cunoastere + cautare vectoriala peste tot ce e in `../content/`:
scrierile tale (`raw/`) si studiile legate de ele (`papers/`). Pune intrebari in romana,
primesti raspunsuri sintetizate **cu citari**, distingand "ce ai scris tu" de "studiul din spate".

## Setare (o singura data)

Mediul e deja construit in `.venv/`. Cheia OpenAI e citita din shell (`OPENAI_API_KEY`)
si salvata in `.env`. Modele: extractie + raspunsuri pe **gpt-5.4**, embeddings `text-embedding-3-large`.

## Indexare (re-rulabila, incrementala)

```bash
cd lightrag
# pilot (cluster tematic, ~36 fisiere)
.venv/bin/python ingest.py --files pilot_files.txt

# indexarea completa, cand esti gata
.venv/bin/python ingest.py --dirs raw papers

# adaugi continut nou mai tarziu -> reia doar fisierele noi/modificate
.venv/bin/python ingest.py --dirs raw papers
```

Manifestul (`manifest.json`) tine minte ce s-a indexat; fisierele neschimbate sunt sarite.

## Intrebari din terminal

```bash
.venv/bin/python kb.py "Ce am scris despre nerezonabil si ce studii il sustin?"
.venv/bin/python kb.py -m global "Ce pattern-uri apar peste fundamentele mele despre leadership?"
.venv/bin/python kb.py -m local "Ce spune Aaker despre diferentiere?"
```

Sfat: pune un alias in shell —
```bash
alias kb='/Users/raztbf/Work/1-tbf-knowledge/lightrag/.venv/bin/python /Users/raztbf/Work/1-tbf-knowledge/lightrag/kb.py'
# apoi: kb "intrebarea mea"
```

## Moduri de cautare

| mod | pentru ce |
|-----|-----------|
| `mix` (implicit) | graf + vectori, cel mai complet |
| `local` | fapte precise, o entitate anume |
| `global` | teme largi, pattern-uri intre documente |
| `hybrid` | local + global |
| `naive` | doar cautare vectoriala clasica |

## Interfata web + graf vizual (optional)

Pentru a *vedea* graful de concepte si a interoga dintr-un browser:

```bash
.venv/bin/lightrag-server   # apoi deschide http://localhost:9621
```

Serverul citeste acelasi `rag_storage/`, deci vede tot ce ai indexat din terminal.
Tot el expune un API compatibil Ollama (`/api/chat`), prin care poti lega nvim — vezi `nvim/kb.lua`.

## Fisiere

- `kb_lib.py` — configurarea comuna (modele, limba, tipuri de entitati)
- `ingest.py` — indexare incrementala cu pastrarea sursei
- `kb.py` — interogare din terminal
- `pilot_files.txt` — lista pilotului
- `rag_storage/` — graful + indexii (generat; nu se commit-uie)
