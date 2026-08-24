# The Business Framework

Carte de management scrisă în stilul *The Tipping Point*: poveste întâi, teoria curge din poveste.

**Regula folderului:** cine deschide `manuscris/` citește cartea. Nimic altceva nu intră acolo.

---

## 📖 [`manuscris/`](manuscris/) — cartea

Doar capitole terminate, în ordinea în care se citesc.

| Capitol | Cuvinte | Deschide pe |
|---|---|---|
| [01 — The Loop](manuscris/01-the-loop.md) | 8.601 | Ingineri NASA care merg la muzeu ca să măsoare un motor F-1 |
| [02 — The Hero and the Architect](manuscris/02-hero-and-architect.md) | 9.528 | Două expediții pleacă spre aceeași bucată de gheață, octombrie 1911 |
| [03 — The Vision](manuscris/03-the-vision.md) | 7.329 | Buzz Aldrin, treizeci și nouă de ani, se întoarce de pe Lună |
| [04 — The Machine](manuscris/04-the-machine.md) | 7.676 | Doi frați cumpără o firmă de imobiliare falimentară și o botează după un râu |
| [05 — The Anatomy](manuscris/05-the-anatomy.md) | 6.813 | Doi frați închid un restaurant profitabil ca să deseneze bucătăria cu creta |
| [06 — The Audit](manuscris/06-the-audit.md) | 6.707 | Direct în cele patru fișe — și întrebarea pe care o pune oricine le vede: „de ce nu punem pur și simplu obiective?" |

**Total: ~47.000 de cuvinte.** Circa 175 de pagini.

Fiecare capitol se termină cu o punte de o linie care deschide capitolul următor.

> **Istoric cap. 6:** scris pe structura dictată de Răzvan (22 aug 2026), un singur capitol în locul perechii obiective+audit, de la pagină albă. Cele trei versiuni respinse și atelierul lor: `arhiva/` + [`atelier/RESET-cap6-7.md`](atelier/RESET-cap6-7.md).

### Ce urmează

**Discovery · Multiplication · Standardization.** Blocate până când secțiunile corespunzătoare din `raz/structura.md` sunt scrise. Candidat nou pentru deschiderea Discovery, pe lângă Langley/Wright: premiul Kremer / Gossamer Condor (fișă verificată în `audit-surse.md`).

Poveștile-ancoră pentru Discovery sunt deja scrise și neconsumate: Langley vs. frații Wright și Pixar, în [`raz/stories/05-discovery-extra.md`](../raz/stories/05-discovery-extra.md). Pentru Multiplication: Rovio și Supercell, în același fișier.

---

## 🔧 [`atelier/`](atelier/) — unelte de scriere

Nimic din ce e aici nu ajunge în carte.

| Fișier | Ce e | Când îl deschizi |
|---|---|---|
| [`todo.md`](atelier/todo.md) | Coada de modificări în așteptare, plus ce s-a făcut deja | Cel mai des. Începe de aici |
| [`plan-de-scriere.md`](atelier/plan-de-scriere.md) | Contractul de stil, alocarea poveștilor pe capitole, structura fiecăruia | Înainte să scrii un capitol nou |
| [`audit-surse.md`](atelier/audit-surse.md) | De unde vine fiecare poveste, ce trebuie creditat, unde e risc | Înainte de publicare. Și când adaugi o poveste nouă |
| [`brief-rescriere-model.md`](atelier/brief-rescriere-model.md) | Brief autonom pentru delegarea unei rescrieri către agenți fără context | Când vrei mai multe variante ale aceluiași pasaj |
| [`propuneri-capitolul-masinaria.md`](atelier/propuneri-capitolul-masinaria.md) | Structura cap. 4-5, tăierile, controllerul operațional, research nou | Când scriem capitolul 5 |
| [`material-rezervat-model-de-business.md`](atelier/material-rezervat-model-de-business.md) | Cele 4 întrebări, diferențiatorul, regula 90/10, limitele arhitecturii | Dacă decidem un capitol despre modelul de business |
| [`build-docx.sh`](atelier/build-docx.sh) | Generează `export/…docx` din tot ce e în `manuscris/` | După orice rundă de modificări |

---

## 📤 [`export/`](export/) — pentru citit și trimis

[`The-Business-Framework.docx`](export/The-Business-Framework.docx) — toate capitolele într-un singur document Word, cu cuprins, schița sistemului și pagini separate per capitol.

**Se regenerează** după orice modificare în manuscris:

```bash
bash carte/atelier/build-docx.sh
```

---

## 📦 [`arhiva/`](arhiva/) — nimic nu se șterge

| Fișier | De ce e aici |
|---|---|
| [`04-the-machine-VECHI.md`](arhiva/04-the-machine-VECHI.md) | 9.659 de cuvinte scrise pe informație incompletă. Poveștile sunt verificate și recuperabile |
| [`variante-cap1/`](arhiva/variante-cap1/) | Patru rescrieri ale deschiderii capitolului 1. **D e cea adoptată** |

> Excepție de la „nimic nu se șterge”: variantele capitolului 6 au fost șterse la cerere, ca să se poată porni de la zero. Ideile bune din ele sunt în `raz/structura.md`.

---

## Unde mai e material

- **`../raz/structura.md`** — sursa de adevăr. Gândirea brută a lui Răzvan. Când e conflict, ea câștigă.
- **`../raz/stories/`** — 47 de povești verificate, cu surse. Vezi [`00-index.md`](../raz/stories/00-index.md) pentru care e folosită unde și care sunt încă neconsumate.
- **`../gpt/`** — două manuscrise vechi. Material de conținut, nu de stil. Conțin o eroare: acolo ramurile se numesc *Optimization / Multiplication*; în sistemul actual sunt **Discovery / Multiplication**.
- **`../examples/the-tipping-point.md`** — modelul de scriere.

---

## Sistemul, pe scurt

```
VISION → THE MACHINE → OUTPUT → QUARTERLY AUDIT → { DISCOVERY | MULTIPLICATION } → înapoi în VISION ↺
```

Regula care ține tot: **construiește lângă mașinărie, validează, apoi unește.**

Bucla se închide în **viziune**, nu în mașinărie — pentru că experimentele și multiplicarea nu produc doar metode, produc și informație despre ce e capabilă afacerea să devină. Metoda validată intră în mașinărie. Cunoașterea validată rescrie viziunea.

Schița oficială: [`manuscris/imagini/sistemul-tbf.png`](manuscris/imagini/sistemul-tbf.png)
