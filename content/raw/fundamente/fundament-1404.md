---
numar: 1404
data: 2025-11-17
---

De prea multe ori un singur KPI (indicator) nu reflectă realitatea. Avem nevoie de o combinație de 3-4-5 indicatori pentru a arăta realitatea într-un mod corect.

Problema?

3-4 indicatori creează o complexitate atât de mare încât mintea noastră se oprește să mai analizeze și preferă să ia decizii emoționale bazate pe unul singur, care "sare de pe pagină".

Soluția?

Comasează cei 3-4 indicatori într-unul singur. Mai precis, construiește un indicator compus.

1. Decide ponderea pe care fiecare indicator o va avea în indicatorul compus.
2. Stabilește punctul minim și cel maxim ale fiecărui indicator. Minim înseamnă cel mai prost rezultat posibil, iar maxim înseamnă cel mai bun rezultat posibil pentru acel indicator.
3. Construiește formula de calcul pentru indicatorul compus.

**Exemplu:**

Indicatorii folosiți:

- Timp de livrare vs. deadline
- Calitatea livrării (scor QA)
- Costuri per proiect
- Satisfacția clientului (NPS)

Ponderi:

- Timp livrare: 30%
- Calitate: 30%
- Costuri: 20%
- NPS: 20%

Praguri minim–maxim:

- Timp livrare: minim 150% din deadline (foarte întârziat), maxim 80% din deadline (livrat înainte de termen)
- Scor QA: minim 60 din 100, maxim 95 din 100
- Costuri: minim 4.000 euro (cel mai prost), maxim 2.000 euro (cel mai bun, cost mai mic)
- NPS: minim 20, maxim 80

Notă: pentru costuri se inversează logica, pentru că un cost mai mic înseamnă performanță mai bună.

Indicatorul compus:

- Normalizezi fiecare indicator între minim și maxim.
- Apoi înmulțești fiecare indicator normalizat cu ponderea lui și le aduni.
- Indicator final = 30% x timp + 30% x calitate + 20% x costuri + 20% x NPS (toate normalizate la 0–1 înainte).
