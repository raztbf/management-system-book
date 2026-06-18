---
titlu: McCoy, Yao, Friedman, Hardy & Griffiths (2024) — Embers of Autoregression Show How Large Language Models Are Shaped by the Problem They Are Trained to Solve
consensus_id: ac8810406a1d56d29ec9bc73a85a0520
url: https://consensus.app/papers/details/ac8810406a1d56d29ec9bc73a85a0520/
autori: R. Thomas McCoy, Shunyu Yao, Dan Friedman, Mathew D. Hardy, Thomas L. Griffiths
an: 2024
jurnal: Proceedings of the National Academy of Sciences (PNAS)
citari: 146
tip-studiu: empiric (evaluare pe 5 LLM-uri, 11 sarcini)
---

# McCoy et al. (2024) — „Tăciunii Autoregresiei"

## Ce spune (abstract)

Ca să înțelegem un LLM, trebuie să ne uităm la PROBLEMA pentru care a fost antrenat: predicția următorului cuvânt
peste text de pe Internet. Această „abordare teleologică" prezice că acuratețea LLM-ului depinde de probabilitatea
sarcinii, a output-ului-țintă și a input-ului. Testând 5 LLM-uri (GPT-3.5, GPT-4, Claude 3, Llama 3, Gemini 1.0) pe
11 sarcini, găsesc dovezi robuste că LLM-urile sunt influențate de probabilitate exact cum prezice teoria. Exemplul
izbitor: acuratețea GPT-4 la decodarea unui cifru simplu e 51% când output-ul e o propoziție cu probabilitate mare,
dar doar 13% când e cu probabilitate mică — deși sarcina e DETERMINISTĂ, unde probabilitatea n-ar trebui să conteze.

## Cifre și citate citabile

* „GPT-4's accuracy at decoding a simple cipher is 51% when the output is a high-probability sentence but only 13% when
  it is low-probability, even though this task is a deterministic one for which probability should not matter." [abstract]
  _(trad.) acuratețea GPT-4 la decodarea unui cifru simplu e 51% când output-ul e o propoziție cu probabilitate mare,
  dar doar 13% când e cu probabilitate mică, deși sarcina e una deterministă pentru care probabilitatea n-ar trebui să
  conteze._
* „we should not evaluate LLMs as if they are humans but should instead treat them as a distinct type of system — one
  that has been shaped by its own particular set of pressures." [abstract]
  _(trad.) n-ar trebui să evaluăm LLM-urile ca și cum ar fi oameni, ci ca pe un tip distinct de sistem — unul modelat de
  propriul set de presiuni._
