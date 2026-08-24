# Fișa de Multiplicare — analiză și propuneri

## 1. Ce trebuie să facă fișa, dedus din tot ce avem

Fișa de experiment are o treabă precisă: **schimbă ce datorează omul la termen — din rezultat, în dovadă.**
Fiecare câmp de pe ea servește asta.

Fișa de multiplicare are o treabă complet diferită, și dacă nu o numim clar o să iasă o listă de
sarcini. Din tot materialul, treaba ei e asta:

> **Să te oprească din a copia ce se vede și să te oblige să numești ce face treaba.**

Pentru că modul în care eșuează multiplicarea nu e lipsa de efort. E o companie care copiază tot ce poate
**vedea** — layout-ul, scriptul, titlurile, echipamentul, brandul — și scapă tăcut exact partea pe care
n-a văzut-o, pentru că nimeni nu o identificase vreodată drept cauză.

---

## 2. Cele șapte moduri în care multiplicarea eșuează (toate documentate deja în carte)

| # | Modul de eșec | De unde | Ce câmp îl prinde |
|---|---|---|---|
| 1 | **Multiplici ceva care nu e level 2** | Webvan · Ron Johnson · farmacia (70% din fazele 2 pică în faza 3) | Poarta de intrare |
| 2 | **Copiezi artefactul, nu condițiile** | Van Nuys — cordonul andon instalat fără nimic din jurul lui. *„Fără ele, cordonul e o bucată de sfoară."* | Ingrediente active |
| 3 | **Ingredientul invizibil, pe care nimeni nu l-a scris** | Fremont — muncitorii își pierduseră slujbele. *Nimeni de la GM n-a scris „forța de muncă trebuie să fi pierdut deja fabrica o dată" în blueprint, pentru că nimeni nu știa că e acolo.* | Ingrediente active |
| 4 | **Împrăștii purtătorii în loc să-i trimiți** | GM a trimis artefactul și a împrăștiat oamenii care învățaseră. Toyota trimite purtătorii (*mother plant*). | Purtători |
| 5 | **Raritatea era portantă** | Krispy Kreme — a multiplicat tot ce se vedea și a dizolvat exact lucrul care nu se vedea, pentru că **ocazia era ingredientul.** Nu exista nicio limită scrisă nicăieri. | Plafon |
| 6 | **Distrugi unitatea-sursă extrăgând din ea** | Riscul din propria ta metodă: scoți doi oameni din echipa care funcționează | Purtători / backfill |
| 7 | **Unești înainte ca noua unitate să țină standardul** | *„Build beside the machine. Validate. Then merge."* · Starbucks, costul reparării după multiplicare | Criteriu de merge |

**Concluzia analizei:** o fișă care nu are câmp pentru **ingredientele active** și pentru **plafon** nu
prinde jumătate din modurile de eșec din propria ta carte.

---

## 3. Trei lucruri prin care multiplicarea diferă structural de un experiment

Astea decid designul.

**1. Metoda e cunoscută — deci cifrele și datele sunt legitime aici.**
Pe fișa de experiment, a cere un rezultat cu termen ar fi o greșeală. **Pe fișa de multiplicare e exact
ce trebuie cerut**, pentru că omul primește un blueprint validat. Aici standardul nu e presiune, e
specificație.

**2. Sunt DOUĂ unități în joc, și una dintre ele funcționează deja.**
Multiplicarea e singura operațiune din tot sistemul care **pune în pericol o parte sănătoasă a
mașinăriei.** Un experiment rulează lângă mașinărie și nu poate strica nimic. O multiplicare scoate
oameni dintr-o echipă care livrează.
Iar în metoda ta asta e și un test gratuit: **dacă echipa-sursă poate pierde doi oameni și revine la
standard, procesele ei chiar erau level 2 — și tocmai ai dovedit-o.**

**3. Are un final definit.**
Un experiment se termină cu o constatare. **O multiplicare se termină cu un merge** — momentul în care
noua unitate încetează să fie proiect și devine parte din mașinărie. Momentul ăla trebuie decis **înainte**,
exact ca KPI-urile pe fișa de experiment.

**Și un al patrulea lucru, care merită o decizie de la tine:**
Nivel 3 = *„procesele pe care am putut să le multiplicăm cel puțin o dată și avem un proces validat de
multiplicare."* Deci **prima multiplicare a unui proces e ea însăși jumătate experiment** — validezi
metoda de transfer, nu doar procesul. A doua e multiplicare pură.
👉 *Propun un marcaj mic în antet: **prima multiplicare** sau **repetare**. Vezi §7.*

---

## 4. PROPUNEREA A — „Geamănul strict"

Oglindește exact fișa de experiment: două câmpuri în antet, șase blocuri în două rânduri, trei câmpuri
în subsol. Cel mai ușor de predat alături de cealaltă.

```
MULTIPLICATION WORKSHEET
Multiplication                    WHAT WE ARE MULTIPLYING | BOTTLENECK IT SOLVES

┌─ Process ──────────────┬─ Evidence ─────────────┬─ Active ingredients ───┐
│ where it runs today    │ why we believe it      │ what actually makes    │
│                        │ transfers              │ it work                │
├─ Carriers ─────────────┼─ Standard ─────────────┼─ Constraints ──────────┤
│ who moves, who backfills│ what the copy must    │ budget, time, ceiling  │
│                        │ produce, and by when   │                        │
└────────────────────────┴────────────────────────┴────────────────────────┘

OWNER | TEAM | DEADLINE                              MULTIPLICATION PLAN
```

**Ce prinde:** toate cele șapte moduri de eșec, cu merge-ul strecurat în *Standard*.
**Ce pierde:** poarta de intrare e un bloc printre altele. Cea mai importantă regulă din tot sistemul —
*multiplici doar level 2 și peste* — arată la fel de important ca „buget".

---

## 5. PROPUNEREA B — „Poarta" ⭐ *recomandarea mea*

Identică cu A, **plus o bandă orizontală între antet și blocuri**: trei căsuțe care trebuie bifate
înainte ca restul foii să poată fi completat.

```
MULTIPLICATION WORKSHEET
Multiplication                    WHAT WE ARE MULTIPLYING | BOTTLENECK IT SOLVES

┌─ BEFORE YOU FILL THIS IN ──────────────────────────────────────────────┐
│ ☐ It has produced the result repeatedly, under conditions that varied   │
│ ☐ It is written down — someone who was not there could follow it        │
│ ☐ We can name what makes it work, not only what it looks like           │
│                                                                         │
│ If any box is empty, this is not a multiplication.                      │
│ It is a Level 1 process, and next quarter's work is an experiment.      │
└─────────────────────────────────────────────────────────────────────────┘

┌─ Process ──────────────┬─ Active ingredients ───┬─ Carriers ─────────────┐
│ where it runs today    │ what must be true for  │ who moves across,      │
│                        │ this to work           │ who backfills          │
├─ Standard ─────────────┼─ Merge ────────────────┼─ Constraints ──────────┤
│ what the copy must     │ when it stops being a  │ budget, time, ceiling  │
│ produce, and by when   │ project                │                        │
└────────────────────────┴────────────────────────┴────────────────────────┘

OWNER | TEAM | DEADLINE                              MULTIPLICATION PLAN
```

**De ce o recomand:**
- **Poarta e regula cea mai încălcată din carte, făcută fizică.** Nu poți completa foaia fără să te uiți
  la ea. Iar cele trei căsuțe sunt exact cele trei condiții de level 2+: repetat · sub condiții variate ·
  standardizat. Plus a treia, care e Van Nuys.
- **Eliberează un bloc** pentru *Merge*, care altfel se pierde.
- E singura variantă în care textul de sub casete face muncă de predare: *dacă o căsuță e goală, asta nu
  e o multiplicare — e un proces level 1, și treaba trimestrului viitor e un experiment.* Aia e chiar
  regula din structura ta, tipărită pe unealtă.

**Ce pierde:** simetria perfectă cu fișa de experiment. Cred că merită.

---

## 6. PROPUNEREA C — „Două unități"

Cea mai originală, și singura care face vizibil riscul asupra unității-sursă. Foaia se împarte pe
verticală: stânga = ce dăm, dreapta = ce construim.

```
MULTIPLICATION WORKSHEET
Multiplication                    WHAT WE ARE MULTIPLYING | BOTTLENECK IT SOLVES

        SOURCE UNIT                    │            NEW UNIT
┌───────────────────────────────────┐  │  ┌───────────────────────────────────┐
│ What it produces today            │  │  │ Standard it must reach, and when  │
│ the range, the standard, the proof│  │  │ same range, defined period        │
├───────────────────────────────────┤  │  ├───────────────────────────────────┤
│ What actually makes it work       │  │  │ What it needs to get there        │
│ visible AND invisible             │  │  │ people, training, resources       │
├───────────────────────────────────┤  │  ├───────────────────────────────────┤
│ What we are taking from it        │  │  │ When it merges                    │
│ carriers · backfill · protection  │  │  │ the criterion, decided now        │
└───────────────────────────────────┘  │  └───────────────────────────────────┘

CEILING what must not be exceeded          OWNER | TEAM | DEADLINE
```

**Ce face cel mai bine:** e imposibil să completezi foaia asta fără să te gândești la ce pățește echipa
din care extragi. Și **rândul de jos, „What we are taking from it", e testul tău gratuit de level 2**,
tipărit.
**Ce pierde:** poarta de intrare. Și e o formă vizuală diferită de toate celelalte fișe din sistem — ceea
ce ar putea fi bine (multiplicarea *chiar* e diferită) sau prost (patru fișe, patru gramatici).

---

## 7. Detalii de decis, indiferent de variantă

**a. Primul câmp din antet.** Pe fișa de experiment scrie *EXPERIMENT NAME*. Aici propun
**WHAT WE ARE MULTIPLYING**, nu *MULTIPLICATION NAME* — pentru că forțează un răspuns specific.
*„Procesul de vânzare B2B, echipa Cluj"* trece. *„Vânzări"* nu trece, și se vede imediat că nu trece.

**b. Marcajul „prima multiplicare / repetare".** Două căsuțe mici lângă antet:
`☐ First multiplication ☐ We have done this before`
Dacă e prima, foaia are un rol suplimentar: **produci și metoda de multiplicare**, adică treci procesul
la level 3. Merită o linie pe foaie care spune asta, pentru că schimbă așteptările — prima e mai lentă
și mai scumpă, și e normal să fie.

**c. Ce scrie sub „Active ingredients".** Sugestia mea de hint, pentru că întrebarea contează mai mult
decât eticheta: ***what must be true here, not just what we do*** — ca să scoată condițiile, nu pașii.
Alternativă mai directă: ***what would break this if it were missing***.

**d. Plafonul.** Nu e același lucru cu constrângerile de buget și timp. E întrebarea Krispy Kreme:
**cât e prea mult?** Densitate, canibalizare, limita de brand, sănătatea unității-sursă. Poate fi o linie
în blocul Constraints sau un câmp propriu. **Recomand câmp propriu dacă alegem C, linie dedicată dacă
alegem A sau B.**

**e. Criteriul de merge.** Formularea care funcționează: *noua unitate ține intervalul din standard timp
de N perioade, fără intervenție din echipa-sursă și fără fondator.* Trebuie completat **înainte**, exact
ca KPI-urile pe fișa de experiment. Altfel merge-ul se face din entuziasm.

---

## 8. Ce mai lipsește după asta

Dacă adăugăm fișa de multiplicare, sistemul are patru fișe pentru cinci stații ale buclei:
**Vision · Audit · Experiment · Multiplication** — și `the-machine.pdf`, care există dar nu e folosit
încă în manuscris.

**Rămâne descoperit un singur lucru:** momentul în care rezultatul unui experiment sau al unei
multiplicări **rescrie viziunea**. E a treia ieșire a auditului, promisă în capitolul 1 și nescrisă
nicăieri. Nu cred că are nevoie de o fișă proprie — probabil e o secțiune pe fișa de viziune, sau o
linie pe fișa de audit. **De discutat separat.**
