# Jurnal — Smart Goals, Stupid Company

## 2026-06-27 — Fundație + primul draft (sesiune mare)

**Ce s-a făcut:**
- Research de craft pe structura non-fiction extraordinară → `carte-internationala/RAPORT-STRUCTURA-nonfiction.md` (nou).
- Decizii fixate cu Razvan: limba = **română** (draft; EN ulterior); framing/titlu = **„Smart Goals, Stupid Company"**.
- Schelet creat: `book-bible.json`, `outline.md`, `voice-profile.md`, acest `progress.md`, `manuscris/`, `interviuri/`, `intrebari/`.
- Transcript salvat brut: `interviuri/transcrieri/2026-06-27-discutie-prieten-obiective-vs-experimente.txt`.
- Cernere (gold panning): `interviuri/procesate/2026-06-27-extractie.md` — toate poveștile, cifrele, frazele, obiecțiile, golurile.
- Arhitectură fixată la material: Introducere + 13 capitole + Concluzie, 4 părți (vezi outline).
- Două rapoarte de research preexistente (de la Razvan) folosite ca sursă de studii + poziționare:
  `RAPORT-RESEARCH-goals-must-die.md` și `research-carte-obiective-vs-experimente.md`.

**Transcrieri consumate:** `2026-06-27-discutie-prieten-obiective-vs-experimente.txt` (procesată integral în extracție).

**Principiu de lucru (din advisor):** material-first. Scriem bogat unde există material real (transcript + cele 1.536 fundamente via `tbf-knowledge` + studii din rapoarte), marcăm vizibil golurile cu `[EXEMPLU PERSONAL NECESAR]` / `[DE VERIFICAT]` și le transformăm în următorul set de întrebări. Fără umplutură.

**Status manuscris:** toate capitolele `gol` la pornire; se scrie acum primul draft, capitol cu capitol, în vocea lui (prin `raz-style-lesson`), cu `tbf-knowledge` ca pas per-capitol.

## 2026-06-27 (continuare) — PRIMUL DRAFT COMPLET

**Realizat:** toate cele 15 capitole (00–14) scrise. Total manuscris: **~46.200 cuvinte.**
- Scrise de mine (spina, voce + fire-exemplu blocate): 00 Introducere, 01 Suma zero, 05 Harta sau busola.
- Scrise prin subagenți cu brief strict (material assigned-only + `raz-style-lesson` + gardă anti-invenție), apoi verificate: 02, 03, 04, 06, 07, 08, 09, 10, 11, 12, 13, 14.
- Firul-exemplu business (recrutare-depozit) împărțit pe beat-uri ca să nu se suprapună: 07=blocajul · 08=design-ul celor 2 experimente · 09=concluziile/datele · 10=codificarea în proces.

**Verificări:** scan anti-AI curat (zero „nu doar X ci și Y", zero generalități de tip „în era digitală", zero concluzii moi). Toate cifrele de studii marcate `[DE VERIFICAT]` cu trimitere la rapoarte. Golurile reale marcate `[EXEMPLU PERSONAL NECESAR]`.

**Status capitole (toate `draft`, acoperire ~60%):**
| # | Titlu | Cuvinte |
|---|---|---|
| 00 | Introducere — Ultimul om… | 2194 |
| 01 | Jocul cu sumă zero | 2031 |
| 02 | De ce ne punem obiective | 2801 |
| 03 | Partea întunecată | 3719 |
| 04 | Steelman | 3156 |
| 05 | Harta sau busola | 2028 |
| 06 | Mașinăria | 2897 |
| 07 | Auditul mașinăriei | 3399 |
| 08 | Experimentul | 3900 |
| 09 | Datele, nu eroul | 3114 |
| 10 | Codifici procesul | 3569 |
| 11 | De la frică la curiozitate | 4472 |
| 12 | Mașinăria vieții | 3569 |
| 13 | Da, dar… (obiecțiile) | 3428 |
| 14 | Concluzie — Luni dimineață | 1949 |

**Goluri prioritare → `intrebari/urmatoarele.md` (runda 2):** metodologia experimentului pas-cu-pas (Cap 8), auditul în practică (Cap 7), cifre reale din cele 7 companii (Intro/11), pivotul ca scenă (Intro), evaluarea pe experimente (Cap 9), verdictul experimentelor cu relația (Cap 12), un exemplu real de corodare a culturii (Cap 3), cartea de budgeting + studiul „90% revin la greutate".

**Pas de coerență (post-draft, 2026-06-27):**
- Repetiții fan-out reparate: „flight or fight" redus de la 5 capitole la 2 (03 owner + 08); „unde dai și unde crapă" lăsat doar în 09 (scos din 08, cu pointer înainte); cold open-ul cap. 09 de-clonat de structura „două X" din 06/08.
- Cifre reconciliate cu rapoartele (NU cu transcriptul, care le garblează — ex. transcript „1,30" vs raport 1,36): toate d-urile corecte în text (0,09 / 0,44 / 1,36 / 1,11 / 1,53 / 0,76 / 0,42); „~15x" corect; Kaizen −46%/+137% corect. Zero garble în manuscris.
- `[DE VERIFICAT]` rămase: pentru citările academice servesc acum doar ca reminder de format la copyedit (numerele sunt confirmate din rapoarte). Confirmare EXTERNĂ reală mai e nevoie doar la: cifrele Valve/Google (vin din transcript, nu din rapoarte), cartea de budgeting (Harvard), studiul „90% revin la greutate".
- Seam-uri verificate: fără leak al concluziilor depozitului în 07/08 (concluziile apar doar în 09, codificarea în 10).

**Cea mai valoroasă mutare următoare (fără Razvan): îmbogățire din `tbf-knowledge`.**
Rezervorul de 1.536 fundamente a fost atins o singură dată (o interogare largă). Pas per-capitol prin `tbf-knowledge` ar aduce formulările lui reale pe: suma zero/prosperitate, bucle de feedback (#0205), faliment=invalidare (#0085), separarea R&D (#0901), MVP→MRP (#0540). Asta e diferența dintre „draft solid" și „extraordinar". (Launcher-ul `tbf-kb` are calea veche `0-kb-tbf` — rulează direct `lightrag/.venv/bin/python lightrag/kb.py`.)

## 2026-06-27 (continuare) — Pas de îmbogățire din `tbf-knowledge`

Am interogat graful LightRAG (3 interogări tematice) și am cernut formulările VERBATIM ale lui Razvan din fundamente, apoi le-am țesut chirurgical (eu, nu subagenți — ca să țin vocea sub control). Tot ce s-a inserat e material real, scris de el:
- **Cap. 1** — am înlocuit „volum de menținere" abstract cu mecanismul lui real din bodybuilding (mușchiul încăpățânat + ceilalți pe volum de menținere, la jumătate/o treime) + aforismul „nu plăti succesul financiar cu ruină personală". Acum payoff-ul capitolului de deschidere e concret și în vocea lui.
- **Cap. 8** — (a) faliment = „modalitate mult mai scumpă de a invalida o idee" în formularea lui exactă (am închis `[DE VERIFICAT fundament-0085]`); (b) AM UMPLUT parțial golul operațional central: distincția lui verbatim „o singură variabilă e pentru rafinarea unei variante bune; ca s-o DESCOPERI, testezi 3-4 concepte foarte diferite — întâi conceptul, apoi incrementalul". Marcajul `[EXEMPLU PERSONAL NECESAR]` rămas e îngustat la ce chiar lipsește (alegerea metricii, pragul numeric, formatul de documentare).
- **Cap. 11** — am adăugat două idei mari care lipseau, ambele verbatim: „investește 10-20% din resurse în lucruri care s-ar putea să nu funcționeze" (extinde proactiv „nu tăia experimente") + „scopul afacerii se descoperă pe parcurs" (Airbnb/Netflix/Apple n-au ajuns unde plecaseră).
- **Cap. 10** — „înainte să fii diferit, fii la fel / nu modifica rețeta înainte s-o gătești" — se mulează perfect pe standard-înainte-de-Kaizen, în vocea lui nativă.

Total manuscris: **~46.900 cuvinte.** Recheck: zero tipare AI noi, zero coliziuni de frază din inserții.
Rezervorul de fundamente mai are de dat (suma zero/„oare a meritat", strategie emergentă, shiny-object-syndrome, execuție-peste-idei/Jamie Dimon, identifică-jocul) — material salvat în scratchpad-ul sesiunii; un al doilea pas de îmbogățire ar mai adăuga la Intro, Cap. 3, 4, 6 și Concluzie.

## Ce urmează (recomandare):
1. Razvan răspunde la runda 2 de întrebări (umple golurile reale) → `/carte-proceseaza`.
2. Pas de șlefuire a vocii pe capitolele scrise de subagenți (pasaje de tranziție, ritm) — opțional, după ce conținutul e complet.
3. Decizie titlu final + subtitlu. Apoi traducere EN pentru piața internațională.
4. Verificarea finală a tuturor `[DE VERIFICAT]` contra rapoartelor de research înainte de orice publicare.
