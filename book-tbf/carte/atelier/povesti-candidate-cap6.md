# Povești candidate — capitolul 6 (Output & Audit)

Rezultatul rundei de research din august 2026. Cinci linii lansate; **trei livrate integral, una parțial
(bucata NHS), două încă în lucru** (Deepwater Horizon / NASA / Alcoa · Volkswagen / Boeing / Nokia).
Se completează când vin.

**Cum se citește:** fiecare candidat are un verdict — ✅ de folosit · ⚠️ de folosit cu condiție ·
❌ de eliminat. Plus riscul de proveniență, pentru că auditul de surse ne cere să nu ne sprijinim pe
anecdotele-semnătură ale altor autori.

**Constrângere de mediu care a modelat totul:** bugetul de căutare web al sesiunii s-a epuizat devreme.
Aproape tot ce urmează vine din **fetch direct pe surse primare** — depuneri SEC, PubMed, NASA, DOJ,
rapoarte oficiale de anchetă, site-uri corporative. Asta a încetinit munca dar a îmbunătățit
proveniența. Consecința: unde nu s-a putut verifica, e marcat explicit, și nu se tipărește.

---

## A. Camera în care se poate spune adevărul

### ✅ ASRS — originea, nu doar sistemul
**Cea mai bună descoperire a rundei. Proveniență aproape zero — nu e anecdota-semnătură a nimănui.**

Deja în `structura.md` §9, actualizat. Ce s-a adăugat: originea (octombrie 1974, un raport identic
există dar *„shared within company only"*; decembrie 1974, TWA 514 se prăbușește), textul verbatim al
FAA despre de ce NASA ține datele, cifrele la zi (2.321.050 de rapoarte, 8.069 alerte), și fâșia de
identificare pe care NASA o ștampilează și o trimite înapoi înainte de a distruge originalul.

### ✅ Mary McClinton — Virginia Mason, 4 noiembrie 2004
**Scena umană care lipsea capitolului. Complet sursată din presa contemporană.**

Spitalul schimbase antisepticul de la unul maroniu cu iod la unul incolor, identic la vedere cu
substanța de contrast. Într-o procedură pentru anevrism cerebral, soluția incoloră a ajuns într-un
pahar nemarcat identic cu cel de contrast și a fost injectată. Amputație sub genunchi în încercarea
de a o salva. A murit pe 23 noiembrie, la 69 de ani.

- Memo-ul intern (Dr. Mindy Cooper, Robert Mecklenburg): eroarea e un **„systems problem"**; niciun
  individ nu e responsabil, dar **„all of us"** suntem. Și: *„We have injured her so badly that she may
  never again regain the life she enjoyed."*
- Șeful siguranței pacienților: *„We just can't say how appalled we are at ourselves."*
- **Răsucirea care o face mai bună decât o poveste curată:** statul Washington l-a acuzat oricum pe
  tehnicianul de radiologie de conduită neprofesională, riscând să-și piardă licența. **Cultura
  non-punitivă internă a coexistat cu un regulator extern punitiv.** Avertisment onest despre limitele
  lui „blameless" când există un al treilea actor.
- Sistemul de alerte, cifre peer-reviewed: **de la 3 alerte pe lună în 2002 la 285 pe lună în 2006**;
  6.112 în total. Majoritatea procesate în 24h, rezolvate în 2–3 săptămâni.
- **Contrastul de zece ani mai târziu:** focarul cu duodenoscoape — 39 de infecții, 18 morți între 2012
  și 2014, detectate intern, **neraportate la timp** către stat. Kaplan public: *„The system it set up
  lagged in informing the public."* Simetric cu Amazon (vezi mai jos).

⚠️ **De nu tipărit:** reducerea de 74% a primelor de asigurare — declarată de companie, netrasabilă.
⚠️ **Proveniență medie:** există o carte întreagă despre ei (Kenney, 2010) și un caz HBS. Unghiurile
proaspete sunt cifrele Furman & Caplan, acuzarea tehnicianului, și contrastul duodenoscoape.

### ✅ Etsy — coloana `why_surprised`
Schema tabelului de postmortem-uri din codul public Etsy conține o coloană numită literalmente
**`why_surprised`**. Nu „cine e vinovat". *De ce am fost surprinși.* O linie de SQL care duce tot
argumentul, nefolosită în nicio carte de business.

Și cifra depusă legal: în prospectul de listare la SEC, martie 2015, Etsy scrie sub răspundere de
securities law că *„blameless post-mortems drive a significant percentage of our development."*
Plus: *„We update our code as often as every 20 minutes, and as many as 70 times per day, with more
than 10,000 deploys during the year ended December 31, 2014."*

**Onestitatea cronologiei:** la 26 de luni după acel prospect, Etsy a tăiat 22% din personal și a
schimbat CEO-ul. Allspaw a plecat. Practica a supraviețuit companiei care a inventat-o. Spusă
întreagă, e o poveste mai bună.

### ✅ Regula lui Treynor Sloss (Google)
Ce transformă „blameless" din sentiment în artefact impus, de la un vicepreședinte cu nume:
> *„To our users, a postmortem without subsequent action is indistinguishable from no postmortem.
> Therefore, all postmortems which follow a user-affecting outage must have at least one P[01] bug
> associated with them. I personally review exceptions. There are very few exceptions."*

Plus avertismentul de design al stimulentelor: *„If you reward engineers for writing postmortems, but
not for closing the associated action items, you risk an unvirtuous cycle of unclosed postmortems."*

⚠️ **Google nu publică NICIO cifră de rezultat.** Am verificat ambele capitole SRE. „Fewer outages",
„more reliable systems" — fără cifre. Dacă ne trebuie „cu X% mai puține incidente", numărul nu există.

### ⚠️ After Action Review — de folosit ca lecție despre limite, nu ca poveste de succes
**Scena e excelentă și e scrisă în doctrină:** comandanții de eșalon superior stau pe flancuri și în
spate, comandantul de batalion în spatele ultimului rând, *„It is important that the atmosphere of the
AAR be one of open discussion, not one stifled by rank consciousness."* Colonelul stă în spate.
Plus: *„An AAR is not a critique"* și *„An AAR does not grade success or failure."*

**Dar răspunsul la întrebarea noastră e nu:** separarea de evaluarea ofițerilor e **practică și
retorică, nu regulament**. Același manual spune la pagina 1 că AAR-ul e *„the keystone of the
evaluation process."* Cearta e documentată cu nume — comandantul TRADOC se temea în 1984 că devine
*„a final report card on a battalion commander"*; un colonel senior spunea în 1986 că implicarea
lanțului de comandă e *„the best thing that has happened to the Army."* **Amândoi cu dreptate.**

**Și lecția de fond, care ne servește mai mult decât un succes:** Armata a construit cea mai bună
mașină de debrief din lume și n-a putut muta ce învăța dincolo de unitatea care învățase. Centrul de
lecții învățate, în propriul manual: *„The irritation of every LL specialist is seeing important
lessons collected and never being shared or resolved"* · *„often there is no obvious 'owner' of the
lesson identified."* GAO: aceleași liste de probleme în 1982 și 1985; în 1993, tot fără proceduri de
urmărire. **Ritualul e necesar și insuficient.**

❌ **Rata de victorie OPFOR: folclor.** NTC nu ține scor, prin politică. Urma se oprește la Tom Clancy,
1994, *„something like 80%"*, fără citare. Cifrele reale, RAND 1987: ~63% pe 113 bătălii. În plus,
11th ACR a devenit OPFOR abia în 1994 — „Blackhorse-ul bate 95% din unități din 1980" e anacronic.

⚠️ **Proveniență mare:** articolul HBR din 2005 al lui Darling, Parry & Moore are exact cârligul nostru,
iar Moore e fost comandant al 11th ACR. Plus Garvin, *Learning in Action*. Nu e teritoriu proaspăt.

---

## B. Mecanica ședinței — cum arată un audit care funcționează

### ✅ Amazon Weekly Business Review — mecanica, NU memo-ul
❌ **Interdicția PowerPoint: de sărit.** Un singur lanț de custodie, un blog mort, niciodată confirmată
de Amazon. Emailul spune **„4 page memo", nu șase**. E anecdota-semnătură din *Working Backwards* și
apare în cinci alte cărți. Dacă totuși o folosim, singura mișcare proaspătă e să-i semnalăm noi
proveniența șubredă — ceea ce modelează chiar onestitatea despre care e capitolul.

✅ **Ce e proaspăt și exact ce ne trebuie:**
- **Regula variației.** Variația de rutină primește o privire de o secundă. Discuția e **exclusiv pe
  excepții**. Cel care deține o metrică mișcată anormal fie prezintă cauza-rădăcină investigată, fie
  spune **„nu știm și investigăm"**. **Ce nu e permis e să speculeze.** Un executiv Amazon:
  *„Guessing or making things up will result in criticism."*
- **Finance are autoritate independentă de audit peste fiecare metrică.** Cel care verifică cifrele nu
  e cel care le deține. **Ăsta e controllerul operațional din capitolul 5, într-o companie reală, ca
  mecanism anti-gaming structural.**
- **Fără strategie și fără rezolvare de probleme în încăpere.** Facilitatorul are voie să întrerupă.
- **Graficul standard „6-12":** aceeași axă cu o pauză vizuală — stânga ultimele 6 săptămâni, dreapta
  ultimele 12 luni. Aceleași culori, aceleași fonturi, în fiecare săptămână. *„You're only able to build
  fingertip-feel for your data if you receive the data in exactly the same colours... each week."*
- **Iterația metricii de „selecție":** număr de pagini de produs → vizualizări → % pagini în stoc →
  % pagini în stoc livrabile în două zile. **Prima metrică pe care o alegi e aproape întotdeauna
  greșită.** Argumentul întreg pentru revizuire periodică, într-o linie.
- Bezos: **„When the anecdotes and the data disagree, the anecdotes are usually right."**
- Bryar & Carr, pentru diagnostic-vs-verdict: *„The key to these meetings is to create a balance between
  extremely high standards and an atmosphere where people feel comfortable talking about mistakes."*

**Ce compromite povestea — și o face mai ascuțită:** raportul Senatului american, iulie 2024. La Prime
Day 2019, rata de accidentări **raportate** a depășit 10 la 100 de lucrători (media industriei 4,8).
Rata urmărită **intern** era aproape **45 la 100**. **Amazon avea intern un număr mult mai onest decât
cel raportat extern. Instrumentația a funcționat. Divulgarea, nu.** Iar procesul de analiză a erorilor
rulează doar pe evenimente tehnice cu impact la client — nu există unul pentru o încheietură ruptă.
**Mecanismul e real și e mărginit, iar granița e exact acolo unde stimulentul de a minți e cel mai
puternic.**

### ✅ Correction of Error (AWS) — cel mai proaspăt material din tot dosarul
De pe slide-ul oficial AWS: *„A mechanism to: Identify and fix problems / Drive ownership of action
items / Maximize lessons learned / Prevent recurrence. **Not to blame. Not to punish.**"*
Și explicit: *„**Don't: Apply blame — Don't use names.**"*

Reguli verbatim: *„Owner and due date are nonnegotiable."* · *„**Lack of metrics is a valid action
item.**"* · la 5 Whys: *„Be concise. Don't justify."* · declanșator: *„Any event that reveals an
opportunity for improvement."* · întrebarea repetată de trei ori: *„How can we cut the time to
detection / diagnosis / mitigation in half?"*

**Scena concretă:** postmortem-ul public al căderii S3 din 28 februarie 2017 — *„one of the inputs to
the command was entered incorrectly and a larger set of servers was removed than intended"* — plus
admiterea meta-eșecului, că panoul de stare nu putea fi actualizat pentru că depindea de S3.
**Operatorul uman nu e numit niciodată. Postmortem-ul public *este* un COE, trecut prin regula
„no names".**

⚠️ Numărul de COE-uri pe an nu e public. Nu se tipărește o cifră.

---

## C. Output-ul citit greșit · ținta care corupe măsurătoarea

### ✅ Bevan & Hood — taxonomia, și e cea mai bine documentată bucată din tot research-ul
Trei categorii împrumutate direct din sistemul sovietic:
- **Efect de clichet** — ținta de anul viitor se bazează pe performanța de anul ăsta, deci nimeni nu
  depășește. *„A wise director fulfils the plan 105 per cent, but never 125 per cent."*
- **Efect de prag** — cei sub țintă urcă, cei peste lasă performanța să alunece la standard. Graficul se
  numește **„Crowding towards the target"**.
- **Distorsiuni de output** — atingi ținta pe seama a ce nu se măsoară.
- **Și capcana care închide ieșirea:** dacă bazezi țintele pe performanța trecută accentuezi clichetul;
  dacă folosești ținte de sistem accentuezi pragul. **Nu există design care să scape de amândouă.**

**Trei artefacte care merg direct în capitol:**
1. **Cele patru rezultate imposibil de distins.** Când numărul vine verde, nu poți ști dacă: totul e
   bine · e bine pe măsurat și dezastruos pe nemăsurat · cifra e atinsă și scopul ratat · ținta n-a fost
   atinsă și datele au fost manipulate. **Argumentul întreg pentru „output-ul e dovadă, nu verdict".**
2. **„Tin openers rather than dials"** — indicatorii nu dau răspunsuri, deschid o cutie cu viermi și cer
   investigație. Distincția noastră, formulată în 1995.
3. **Legea lui Gresham aplicată la ținte.** Patru tipuri de actori: sfinți · încercători onești · jucători
   reactivi · maniaci raționali. Iar mecanismul: *„actors of types (1) and (2) learn the costs of not
   gaming the system and shift towards type (3)."* **Oamenii onești învață costul onestității și se
   mută.** E mai precis decât orice aveam despre cum un sistem convertește oameni buni.

**Cifrele dure, din raportul Curții de Conturi britanice (2001):** nouă spitale au ajustat necorespunzător
listele, trei dintre ele peste trei ani, **aproape 6.000 de fișe**. Surrey & Sussex 1.800 într-un an.
Guy's & St Thomas' patru ani, *„likely to be considerable"*. La Barts, 22 de pacienți peste 18 luni.
- **În cinci din nouă cazuri a ieșit la iveală doar din exterior** — plângeri, un parlamentar, un
  documentar TV. Și: *„It is not possible to say whether or when the problems... would have been
  identified had these complaints or publicity not occurred."*
- Auditorii numesc cauza, în 2001: *„the adjustments were made in the context of pressure on trusts and
  particularly Chief Executives to meet key departmental targets."*
- **Detaliul cel mai urât:** patru directori au plecat cu compensații de peste **£260.000 acoperite de
  clauze de confidențialitate**. Patru dintre angajații suspendați au fost reangajați în sistem.

**Efectul de prag, măsurat** (*BMJ* 2005, **428.593 de episoade clinice**): 12,3% dintre pacienți au
petrecut **între 220 și 239 de minute** — ținta era 240. **Unul din opt pacienți era mutat afară în
ultimele douăzeci de minute.** Și erau semnificativ mai în vârstă: 56,5 ani față de 48,9.

**Urmărirea din 2012:** pe măsură ce ținta s-a înăsprit, cohorta de ultimele 20 de minute s-a dublat,
proporția vârstnicilor din ea a urcat de la 7,4% la 17,3%, timpul până la primul medic s-a îmbunătățit
cu **un minut**, iar șederea totală a pacienților internați a crescut cu **treizeci de minute**.

**Cazul care închide argumentul:** la un spital din Bristol, ținta pentru **prima** programare la
oftalmologie a fost atinsă prin anularea programărilor **de control**, care nu figurau în nicio țintă.
**25 de pacienți și-au pierdut vederea în doi ani** — și cifra e probabil o subestimare. Nicio fraudă,
niciun răufăcător, niciun titlu de ziar. A ieșit la iveală doar pentru că cineva completa formulare pe
care nu i le cerea nimeni.

Și confirmarea că instrumentul nu vedea nimic: un spital cu trei stele putea conține *„a scandalously
poor clinical service"*; **niciunul dintre marile scandaluri clinice ale perioadei n-ar fi afectat
ratingul instituțiilor implicate.**

**Contrapunderea onestă, obligatorie:** îmbunătățirile au fost reale — pacienții care așteptau peste 12
luni au scăzut de la 67.000 la **24**. Autorii: *„Nobody would want to return to the NHS performance
before the introduction of targets."* Bevan însuși a argumentat trei ani mai târziu partea pro-țintă.
Există și o lucrare într-un jurnal de top care nu găsește deloc efecte disfuncționale.
Și concluzia lor, care e cea mai bună propoziție pentru noi: *„although there were indeed dramatic
improvements in reported performance, **we do not know the extent to which these were genuine or offset
by gaming**."* Nimeni n-a auditat vreodată sistemul de audit.

✅ **CORECTURĂ LA O CORECTURĂ ANTERIOARĂ.** Spusesem că „coridoarele reclasificate ca saloane" nu se
susține. **Se susține — doar că sursa e alta.** Raportul comisiei parlamentare pentru administrație
publică din 2003, paragraful 58, verbatim: *„targets for A and E maximum waiting times were being
circumvented by imaginative fixes where **trolleys either had their wheels removed or were re-designated
as 'beds on wheels' and corridors and treatment rooms are re-designated as 'pre-admission units'**."*
**Roțile scoase de pe targă ca să devină pat. Coridorul redenumit „unitate de pre-internare".**

### ★ Materialul suplimentar din a doua trecere pe ținte publice — cel mai puternic din tot dosarul

**1. GRUPUL DE CONTROL PERFECT — serviciile de ambulanță.** Numărul de trusturi englezești care atingeau
ținta de 75% în opt minute:
- **Apeluri de categoria A — cu țintă, inclusă în ratingul cu stele: de la 3 la 26** trusturi în patru ani.
- **Apeluri de categoria B și C — aceleași opt minute, aceleași echipaje, fără nicio țintă: de la 1 la 1.**
  Iar capătul de jos al intervalului a **scăzut**, de la 35% la 27%.

**Același personal, aceleași mașini, aceleași opt minute, alt tablou de marcaj.** Nu are nevoie de nicio
acuzație de necinste și e mult mai greu de contestat decât un vârf pe un grafic.

**2. ACELAȘI AN, ACEEAȘI CALE FERATĂ, DOUĂ ADEVĂRURI.** După ce autoritatea de reglementare feroviară a
schimbat definiția punctualității — de la „a ajuns la destinația finală în 5 sau 10 minute" la „la minut,
în fiecare stație" — cifrele pentru **același an** au fost: **87,0% punctualitate** după vechea măsură,
**64,7%** după cea nouă. **O prăpastie de 22 de puncte creată exclusiv de o alegere de definiție.**

Și autoritatea recunoaște în propria metodologie efectul de prag: o a doua măsură a fost creată *„to
ensure trains were not **'written off'** by controllers or signallers **once they exceeded their PPM
threshold**"* — odată ce un tren rata pragul, metrica nu mai dădea nimănui niciun motiv să-i pese, așa că
trenurile erau abandonate sau întoarse din drum.

**3. CEA MAI BUNĂ FORMULARE OFICIALĂ A ÎNTREGULUI CAPITOL.** Directorul medical național al NHS, scrisoare
către ministru, 13 iulie 2017, despre de ce se desființează ținta de opt minute:
> *„The clock is 'stopped' by the arrival of the first vehicle, not the arrival of the vehicle that the
> patient actually needs. **A quarter of all patients who require hospital treatment have the clock stopped
> by a vehicle – often a motorbike – which is in fact incapable of taking them anywhere. There are few
> better examples of hitting the target and missing the point.**"*

Și: *„**Most worryingly, the target can increase response times and cost lives.** Multiple vehicles are
often dispatched to the same patient **in a race to 'stop the clock'**."*
Cifra: **3,7 milioane de vehicule trimise și apoi anulate într-un singur an**, între 4% și 46% din
incidente în funcție de trust.

**4. CAZUL BRISTOL, ÎN CUVINTELE MEDICULUI, NU ÎN REZUMAT.** Directorul clinic al spitalului de oftalmologie:
> *„The waiting time targets for new outpatient appointments have been achieved **at the expense of
> cancellation and delay of follow-up appointments. At present we cancel over 1,000 appointments per
> month.** Some patients have waited 20 months longer than the planned date... **there have been 25 in the
> past 2 years** [who lost vision]. **This figure undoubtedly underestimates the true incidence.**"*

Și cazul individual, care e scena: *„One particularly sad case was that of an elderly lady who was
completely deaf and relied upon signing and lip-reading... Her follow-up appointment for glaucoma was
delayed several times and during this time her glaucoma deteriorated and **she became totally blind**."*

Într-o altă zonă: **19.500 de programări de control anulate în șase luni** ca să fie atinsă ținta pentru
pacienți noi. Verdictul comisiei: *„**When targets put target setting before clinical need, they are
clearly inverting priorities rather than advancing them.**"*

**5. MĂRTURIA SUB JURĂMÂNT.** O asistentă de la Mid Staffordshire, în fața comisiei de anchetă:
> *„**Nurses were expected to break the rules as a matter of course in order to meet target**... Rather
> than 'breach' the target, **the length of waiting time would regularly be falsified on notes and computer
> records.** I was guilty of going along with this if the wait time was only being breached by 5 or 10
> minutes and the patient had been treated... but when wait times were being breached by 20–30 minutes or
> more and the patient had still not been seen, I was not prepared to go along with what was expected."*

Și de ce: *„if you as the nurse in charge in that particular shift had had an excessive amount of
breaches, **you were then held responsible and had to explain it**."*

**6. Și medicul căruia i s-a spus să abandoneze un pacient:** *„**Dr Beal, like other doctors present, was
directed to abandon one patient, and move to another who was shortly due to have been waiting for four
hours.**"* Curtea de Conturi prevăzuse asta cu patru ani înainte, în scris.

### 🔴 CORECȚII MAJORE la ce circulă — și una ne privește direct

❌ **„Raportul Francis a găsit între 400 și 1.200 de morți în plus la Mid Staffordshire" — FALS.** Agentul
a căutat cifra în textul integral: **nu apare nicăieri în raport.** Francis scrie explicit, paragraful
5.29: *„**it is not possible to say that any specific number or proportion of deaths was from an avoidable
cause.**"* Cifra vine din presa care a acoperit un raport din 2009.

**Și constatarea lui reală e mai bună pentru noi decât cifra**, paragraful 5.2:
> *„**It is clear that this debate distracted not only the Trust's management but also** [toate
> autoritățile de deasupra] **from taking the steps necessary to protect patients.**"*

**Cearta de doi ani despre metodologia statisticii e chiar lucrul care a împiedicat pe cineva să se ducă
să se uite în saloane.** Asta e o poveste mai bună și e adevărată.

❌ **„Trenurile sar stații ca să atingă ținta de punctualitate" — contrazis de regula însăși.** Ratarea unei
stații programate e automat un eșec al indicatorului. Niciun document oficial. **De înlocuit cu efectul de
prag de mai sus, care e recunoscut de autoritate.**
❌ **„Padding-ul de orar ca să flateze cifrele" — neverificat.** Niciun document oficial. De renunțat.
❌ **„Hello nurse" — metrică greșită, deceniu greșit.** A manipulat un indicator din 1997 despre timpul până
la prima evaluare, desființat tocmai pentru că era manipulat. **Dar e o anecdotă mai bună așa:** guvernul a
desființat indicatorul pentru că era jucat, apoi trei ani mai târziu a construit un ceas nou cu același
defect.
❌ **Ținta de patru ore nu a fost niciodată 98% la început. A fost 100%.** 98% e o concesie din decembrie
2003. 95% e din iunie 2010.

### ⚠️ CONTRAPUNDEREA ONESTĂ, care trebuie pusă de noi în text

- **Comisia care a investigat falsificările de la ambulanțe a cuantificat manipularea la 2–6%, față de o
  îmbunătățire reală de până la 20%.** În cuvintele ei: *„These alterations have, in effect, **'gilded the
  lily' of genuine improvement**."*
- **Inspectoratul de poliție a căutat explicit dovezi de manipulare deliberată și aproape că nu a găsit**,
  deși a constatat că **19% din infracțiuni nu erau înregistrate** (33% la violență, 26% la infracțiuni
  sexuale). Formularea lor: *„We looked for hard evidence of improper practices... **relatively little was
  found**"*, dar forțele au recunoscut că *„the culture of chasing targets as ends in themselves had
  distorted crime-recording decisions."*

  **Mecanismul e mai plictisitor și mai util decât frauda: o cultură de ținte îndoaie instinctele unei
  organizații întregi despre ce contează ca real, fără ca cineva să trebuiască să decidă să mintă.** Asta
  e exact teza noastră, și e mai greu de respins decât o poveste cu falsificatori.
- **Teza lui Bevan și Hamblin nu e „țintele distrug tot".** E că **ranking-ul reputațional a funcționat** —
  Anglia a atins ținta tocmai pentru că ratingul cu stele făcea eșecul rușinos, în timp ce Scoția, Țara
  Galilor și Irlanda de Nord, fără rating, au rămas sub 60%. **Nu supralicita împotriva propriei surse.**
❌ **„See and treat" nu apare în niciuna dintre lucrări.** Nu se atribuie lor.
⚠️ **Proveniență mare** — 1.561 de citări; e originea unor anecdote care circulă acum fără sursă.
**Mișcarea de dezamorsare: citează sursele primare pe care nu le folosește nimeni** — raportul Curții de
Conturi și studiul cu 428.593 de episoade. Acolo versiunea noastră încetează să sune ca a tuturor.

### ★ DEEPWATER HORIZON — cea mai bună poveste pentru „ai măsurat output-ul greșit"

**De ce e cea mai bună: avem literalmente ambele instrumente pe aceeași masă, în aceeași seară.**

❌ **Folclorul e fals.** Nu au fost „șapte directori BP care au adus un premiu de siguranță". Au fost
**patru**, doi de la BP și doi de la Transocean, într-un *„management visibility tour"*. **Niciun raport
oficial nu menționează vreo ceremonie de premiere.**

**Scena, ora 19:00, sala de conferințe de la etajul trei, cu două ore înainte de explozie.** Un
vicepreședinte BP: platforma era *„the best performing rig that we had in our fleet... one of the top
performing rigs in all the BP floater fleets from the standpoint of safety and drilling performance."*

> ***„Despite all the crew's troubles with this latest well, they had not had a single 'lost-time
> incident' in seven years of drilling."***

**Și în aceeași ședință, în aceeași oră, al doilea instrument:** un audit BP de siguranță din septembrie
2009 produsese **o listă de 30 de pagini cu 390 de poziții de mentenanță restantă, însumând 3.545 de
ore-om.** Ședința a discutat obiecte căzute și răniri personale.

**Un instrument spunea „excelent". Celălalt spunea „platforma se degradează". Erau pe aceeași masă.**

**Documentul care încheie discuția — și e auto-incriminare în scris, într-o depunere la SEC.** Transocean,
declarație către acționari, 1 aprilie 2011:
> *„…notwithstanding the tragic loss of life in the Gulf of Mexico, we achieved an exemplary statistical
> safety record... **As measured by these standards, we recorded the best year in safety performance in
> our Company's history**."*

Iar mecanica bonusului, din același document: siguranța valora 25% din bonus, iar formula a calculat
**un payout de 115% pe componenta de siguranță — în anul în care au murit unsprezece oameni pe platforma
lor.** A fost nevoie de intervenție discreționară umană ca să fie adus la zero. **Și chiar și după
intervenție s-a plătit 67,4%.**

**LECȚIA FUSESE DEJA PUBLICATĂ. DE DOUĂ ORI.**
- **2000, Grangemouth.** BP scrie ea însăși, în dialog cu autoritatea britanică: *„The use of occupational
  safety indicators such as 'Days Away From Work Case Frequency' **can obscure other factors, and provide
  a false sense of security if it indicates an overall improving trend**."*
- **2007, raportul Baker după Texas City**, constatarea formală: ***„BP mistakenly interpreted improving
  personal injury rates as an indication of acceptable process safety performance at its U.S. refineries...
  created a false sense of confidence."***

**Publicată în 2000. Repetată în 2007. Neaplicată în 2010.**

**Fraza care articulează tot capitolul**, de la comisia americană de investigare a accidentelor chimice:
> ***„History has repeatedly proven that good personal safety statistics have, in fact, often preceded
> major accident events, yet industry and regulators still rely on personal safety metrics to indicate
> good process safety performance."***

**Și semnalul dinainte.** Cu opt luni înainte, președintele Transocean scria intern:
> *„I am not convinced at all that we have the right leading indicators. The leading indicators we report
> today are **all just different incident metrics — they have nothing to do with actually preventing
> accidents**."*

**Aprilie 2010, trei catastrofe în trei săptămâni, toate cu instrumente de siguranță care arătau bine:**
Tesoro Anacortes pe 2 aprilie (7 morți, **la câteva săptămâni după ce câștigase un premiu național de
siguranță**), Upper Big Branch pe 5 aprilie (29 de morți), Deepwater Horizon pe 20 aprilie (11 morți).

Plus catalogul comisiei: Phillips 66 Houston 1989, 23 de morți, *„several million work hours without a
lost time incident"* · Valero McKee 2007 · Bayer CropScience 2008 · CITGO Corpus Christi, recunoaștere
națională pentru siguranță pe baza anului în care avusese un incendiu major.

✅ **Proveniență scăzută.** Nu e poveste-semnătură din nicio carte populară.
⚠️ **Nu supra-simplifica:** BP a fost și un caz de subinvestiție și presiune de cost, nu doar de măsurare
greșită. Iar cifra de șapte ani vine dintr-o mărturie orală, nu dintr-un registru.

### 🔴 TENSIUNEA DIN CAPITOL PE CARE TREBUIE SĂ O REZOLVĂM

**O'Neill a organizat Alcoa în jurul ratei de zile-muncă pierdute — exact categoria de indicator de
siguranță personală pe care raportul Baker și comisia americană o demontează la Deepwater Horizon.**

Dacă folosim ambele povești în același capitol fără să tratăm asta, un cititor atent ne prinde.

**Și rezolvarea nu e să tăiem una — e chiar miezul argumentului.** Alcoa însăși oferă dovada: rată record
de accidentări în 2003 **și patru morți în același an**, cu propria conducere concluzionând că
indicatorul nu prindea ce omora oamenii. Deci: **același indicator, folosit de un om care l-a tratat ca
pe o precondiție și nu ca pe o țintă, a produs ceva real — și tot nu a văzut evenimentele rare și
catastrofale.** Asta e o lecție mai fină și mai adevărată decât oricare dintre cele două povești luate
separat.

### ★ MID STAFFORDSHIRE — cel mai pur mecanism din tot dosarul

Indicatorul era HSMR — raportul dintre decesele observate și cele așteptate, exact structura
output-vs-viziune. Valorile spitalului: **127 în 2005/06** — cu 27% mai multe decese decât se așteptau.

**Și acum ce a făcut spitalul, în propriile cuvinte, raportat autorității de reglementare:**
> *„Its mortality rate has improved **from 127 in 05/06 to c 101 between May and August 2007 as a result
> of significant focus on coding and mortality**."*

**Au reparat codificarea, nu îngrijirea.** Auditul lor a găsit că **80% dintre diagnostice necesitau
recodificare.**

Iar concluzia oficială a anchetei publice:
> *„The Trust, the West Midlands Strategic Health Authority and the Department of Health **all focused
> attention on coding issues, at the expense of considering whether a high HSMR indicated concerns about
> patient care**."*

**Organizația a atacat instrumentul, nu lucrul măsurat.** Nu există o ilustrare mai curată în tot dosarul.

Și fraza care merită să fie citată ca atare:
> ***„It took false assurance from good news, and yet tolerated or sought to explain away bad news."***

Plus omul care a fost ignorat: un director al autorității regionale propunea o analiză independentă cu
motivația *„to understand this, not to explain it away."*

### ★ ATLANTA PUBLIC SCHOOLS — scena umană, și efectul de clichet documentat

Superintendenta a fost numită **Superintendent Național al Anului în 2009**. Ancheta guvernatorului a
găsit fraudă în **44 din 56 de școli examinate**, a identificat **178 de educatori**, dintre care
**82 au recunoscut** — și **38 erau directori de școală.**

> *„**Many of the accolades, and much of the praise, received by APS over the last decade were
> ill-gotten.**"*

**Mecanismul, dintr-o secțiune a raportului numită literalmente „TARGETS":** *„The unreasonable pressure
to meet annual 'targets' was the **primary motivation** for teachers and administrators to cheat."*
Formularea ei: *„No exceptions. No excuses."* Și: *„I will find someone who will meet targets."* A
înlocuit 90% dintre directori.

**Efectul de clichet, explicit:** dacă anul trecut 60% dintre elevi au atins standardul, anul acesta ținta
devine 63% — setată pe cohorta de anul trecut, nu pe copiii care sunt efectiv în clasă.

**Și scena, gata făcută:** la adunarea anuală din Georgia Dome, **școlile care au atins țintele stau pe
teren. Cele care nu, sunt trimise în sectoarele de la ultimul nivel al stadionului.**

**Onestitatea anchetatorilor, pe care trebuie s-o preluăm:** *„**We do not express any opinion as to the
merits of targets.** However, targets were implemented in such a way that teachers and administrators
believed that they had to choose between cheating to meet targets or failing to meet targets and losing
their jobs."*

⚠️ **Superintendenta a murit înainte de proces — nu a fost niciodată judecată.** Nu o numi „condamnată".
Și există o contra-narațiune publicată despre severitatea sentințelor și dimensiunea rasială a procesului.
Menționarea ei ne face mai credibili.

### ⚠️ GOODHART — legea nu e stabilă nici sub memoria propriului autor

**Fraza originală, verificată, e o propoziție subordonată în interiorul unei fraze mai lungi**, nu un
aforism: *„any observed statistical regularity will tend to collapse once pressure is placed upon it for
control purposes"*. Iar Goodhart scrie **„Goodhart's law" la persoana a treia deja în 1975** — numele
circula deja printre colegi.

**Goodhart despre propria lege**, într-o enciclopedie pe care a scris-o el însuși:
> *„It was intended as a **humorous, throwaway line**, and... was not based on some deeper underlying
> analysis, just some limited empirical observation."*

❌ **Fraza celebră nu e a lui.** *„When a measure becomes a target, it ceases to be a good measure"* e a
lui **Marilyn Strathern (1997)**, derivată din parafraza lui **Keith Hoskin (1996)**. Goodhart o
validează public în 2015, dar nu a scris-o niciodată.

**Și cadoul pentru un capitol despre măsurare:** în propria autobiografie, Goodhart **se citează greșit pe
sine** — numește textul „a jocular footnote" deși în ambele ediții tipărite e text curent, și reformulează
legea altfel. *„That quip... **seems to lead a life of its own**, is the only memorable thing about my
work!"*

**Legea lui Goodhart nu e stabilă nici măcar sub memoria autorului ei.**

### ⚠️ Fabrica sovietică de cuie — se poate folosi, dar NU ca eveniment

**E în lucrarea originală a lui Campbell din 1976**, ca exemplu ilustrativ: *„If weight, then factories
would produce only their heaviest item (e.g., the largest nails in a nail factory). If number of items,
then only their easiest item to produce (e.g., the smallest nails)."*

**Dar Campbell scrie „e.g.", nu descrie o fabrică anume, și își declară el însuși dovezile ca fiind
„predominantly anecdotal".** Formularea sigură: *„Donald Campbell dădea, în 1976, exemplul fabricii de
cuie…"* — nu *„a existat o fabrică sovietică unde…"*
❌ **Caricatura din Krokodil: netrasabilă.** Nu o prezenta ca artefact documentat.
❌ **Efectul cobrei: de eliminat complet.** Lanțul de citare se termină într-un **manual de creștere
bisericească** din 1996. Niciun document colonial nicăieri. Iar istoricul care a studiat subiectul spune:
*„I'm pushing for the rat effect, in lieu of the cobra effect."* Și noi am folosit deja Hanoi în capitolul 1.

✅ **Campbell, exemplul cu body count-ul din Vietnam** — cel mai puternic al lui: *„**There was thus
created a new military goal, that of having bodies to count**, a goal that came to function instead of or
in addition to more traditional goals, such as gaining control over territory."*

✅ **Steven Kerr (1975), orfelinatele:** finanțarea și prestigiul directorului depind de numărul de copii
înscriși, deci *„it becomes rational for them to make it difficult for children to be adopted. **After
all, who wants to be the director of the smallest orphanage in the state?**"*

### ⚠️ ALCOA / Paul O'Neill — de folosit DOAR în varianta corectată. Cea populară e falsă.

**Vestea bună: există o sursă pre-Duhigg, cu O'Neill povestind singur.** O relatare din presa de
specialitate, aprilie 2001, despre un discurs ținut la Georgetown pe când era secretar al Trezoreriei —
**cu unsprezece ani înainte de cartea lui Duhigg.** Confirmă independent numărul de telefon de acasă,
accidentul mortal, „we killed him", cifra de 1,86 și cele trei întrebări. **Nu trebuie să ne sprijinim pe
Duhigg pentru nimic esențial.**

🔴 **CAPCANA CEA MAI PERICULOASĂ: „transcriptul discursului din 1987" care circulă online ESTE proza lui
Duhigg.** Agentul a comparat cuvânt cu cuvânt — **identic**, inclusiv fraza celebră despre siguranță ca
indicator al schimbării obiceiurilor. A fost spălat printr-un blog de marketing corporativ și re-etichetat
ca sursă primară. **A-l cita ca dovadă independentă e cel mai sigur mod de a fi prins.**

⚠️ Și O'Neill era deja director general de patru luni în octombrie 1987 — nu era prima lui zi.

🔴 **CIFRELE FINANCIARE DISTRUG POVESTEA POPULARĂ.** Din depunerile SEC, profit net:
**944,9 milioane (1989) → 295,2 → 62,7 → PIERDERE DE 1,14 MILIARDE (1992) → 4,8 milioane (1993).**
Vânzările au scăzut de la 10,9 la 9,1 miliarde. **La șase ani de la lansarea programului de siguranță,
compania era la profit net aproximativ zero.**

Iar profitul urmărea îndeaproape prețul aluminiului: 0,92 → 0,75 → 0,67 → 0,59 → 0,56 dolari pe livră,
revenind la 0,77 în 2000. **Cea mai curată complicație cauzală disponibilă, direct din depunerile
companiei.**

Și cifra triumfală de 1,484 miliarde din 2000 **nu e a lui O'Neill** — Belda era director general din mai
1999. Saltul de venituri de la 16,3 la 22,9 miliarde e achiziții, nu creștere organică: activele totale
s-au dublat aproape într-un an. Iar creșterea capitalizării a fost parțial **cumpărată cu acțiuni nou
tipărite** — de la 88,8 milioane de acțiuni în 1994 la 866,3 milioane în 2001.

🔴 **COMPLICAȚIA CARE E CHIAR TEZA NOASTRĂ, din raportul propriu al Alcoa:**
- **În 2000 — ultimul an al lui O'Neill ca președinte al consiliului — au murit nouă oameni** la Alcoa
  (3 angajați + 6 contractori).
- **În 2003, Alcoa raportează „cea mai bună rată de zile-muncă pierdute din istoria companiei" (0,12) — și
  patru morți în același an.** Propriile cuvinte: *„Regrettably, despite this improvement, we experienced
  four fatalities."*
- Iar concluzia conducerii Alcoa e exact ce ne trebuie: era nevoie de *„the detection and elimination of
  **low probability events with potential for serious injury or death**"* — **o recunoaștere explicită că
  indicatorul de zile-muncă pierdute nu prindea ce omora oamenii.**

**Aceasta e distincția siguranță personală / siguranță de proces, în cuvintele companiei.** Aceeași ca la
Deepwater Horizon. Și e cel mai bun material din tot dosarul pentru „ai măsurat output-ul greșit".

🔴 **Și descoperirea originală:** agentul a căutat în patru rapoarte anuale depuse la SEC — **rata de
accidentări nu apare în niciunul.** „Safety" apare doar în clauze despre răspundere de mediu și litigii.
**Indicatorul despre care O'Neill spunea că e felul în care ar trebui judecată compania nu a intrat
niciodată în documentele prin care compania era judecată efectiv, legal.** Trăia în discursurile lui și
într-un sistem intern.

⚠️ Plus: rata de zile-muncă pierdute e **cea mai ușor de manipulat statistică de siguranță din industrie**,
pentru că dacă o accidentare costă o zi de muncă e o clasificare discreționară.

✅ **DOUĂ REGULI ALE LUI O'NEILL, verificate și mai bune decât cea cu 24 de ore:**
> **„Safety is not a priority at Alcoa, it is a precondition."** Dacă un pericol trebuie reparat, *„you do
> it today. You don't budget for it next year."*

> **„If you ever try to calculate how much money we save in safety, you're fired."**

A doua e superbă pentru noi: **a refuzat să lase siguranța să fie citită ca reducere de costuri.** Mai
ascuțită decât orice e la Duhigg, și verificabil a lui.

✅ **Și teoria lui reală, documentată înainte de Duhigg — mai bună decât „keystone habit":** o organizație
mare e una în care fiecare om poate răspunde „da" la trei întrebări în fiecare zi — *sunt tratat cu
demnitate și respect de toată lumea, indiferent de grad · mi se dau lucrurile de care am nevoie ca să
contribui într-un fel care dă sens vieții mele · sunt recunoscut pentru ce fac de către cineva la care
țin.* Iar siguranța e **singurul indicator care nu poate fi falsificat** și care îți spune dacă răspunsurile
sunt da.
> *„Safety is a tangible way to show that human beings really matter."*

❌ **De eliminat:** „o douăzecime din media americană" (graficul propriu Alcoa dă ~o unsprezecime) ·
„0,23" (nu corespunde niciunui an) · „200 de milioane profit în 1987" (neverificabil, pre-EDGAR) ·
numele muncitorului mort — **e nenumit în toate sursele; nu inventăm unul.**

⚠️ **Proveniență:** e povestea-semnătură a lui Duhigg. **Dar nu există nicio demontare publicată** — agentul
a căutat-o explicit. Literatura secundară e uniform hagiografică. **Critica de mai sus, asamblată din
depuneri și din raportul propriu al companiei, nu e tipărită nicăieri.** Ăsta e avantajul: nu repovestim
Duhigg, îl corectăm.

### ⚠️ NASA — normalizarea devianței. Material excelent, dar cu trei capcane.

**Ideea, și e exact teza noastră despre output:** garniturile erodate și bucățile de spumă desprinse au
fost observate în mod repetat, iar **fiecare zbor care nu s-a terminat în catastrofă a fost citit ca
dovadă de siguranță, nu ca semnal.**

**Cel mai bun pasaj din tot dosarul**, raportul comisiei Columbia, p. 195:
> *„Engineers and managers **incorporated worsening anomalies into the engineering experience base, which
> functioned as an elastic waistband, expanding to hold larger deviations from the original design.**
> Anomalies that did not lead to catastrophic failure were treated as a source of valid engineering data
> that justified further flights."*

Și mecanismul care face ca semnalul să nu se acumuleze niciodată, p. 196:
> *„An incident of O-ring erosion or foam bipod debris would be followed by several launches where the
> machine behaved properly, **so that signals of danger were followed by all-clear signals.**"*

**Cauza organizațională, din rezumatul executiv, p. 9:** *„**reliance on past success as a substitute for
sound engineering practices**."*

**Feynman, verificat pe textul oficial NASA:**
> *„For a successful technology, reality must take precedence over public relations, for nature cannot be
> fooled."*

Și pasajul care e literalmente argumentul nostru despre output:
> *„**The acceptance and success of these flights is taken as evidence of safety.** But erosion and blow-by
> are not what the design expected. **They are warnings that something is wrong.**"* · *„Erosion was not
> something from which safety can be inferred."* · *„When playing Russian roulette the fact that the first
> shot got off safely is little comfort for the next."*

**Vocabularul instituțional e o comoară.** Definiția formală NASA: *„**In Family:** A reportable problem
that was previously experienced, analyzed, and understood."* Iar judecata comisiei: *„**'In-family' was a
strange term indeed for a violation of system requirements.**"* Plus reclasificarea: spuma a ajuns să fie
tratată *„more as a turnaround or **maintenance issue**, and less as a hazard to the vehicle and crew."*

Și comisia Challenger, direct: *„NASA and Thiokol accepted escalating risk apparently because they
**'got away with it last time.'**"* Plus imaginea: o analiză de 18 pagini redusă, la revizuirea de
pregătire de zbor, la un singur grafic pe care scria *„acceptable risk because of limited exposure and
redundancy."*

**Cifre verificate:** erodare a garniturilor pe **14 din 24** de zboruri (toate îmbinările) sau **7 din
24** (doar îmbinările de câmp) — ⚠️ **nu „15 din 24"**, cifră care nu apare în raport. Pierdere de spumă
pe **peste 80%** din cele 79 de misiuni cu imagini disponibile.

🔴 **TREI CAPCANE, în ordinea gravității:**

1. **Definiția faimoasă a lui Vaughan nu e a lui Vaughan.** Citatul care circulă peste tot („people within
   the organization become so much accustomed to a deviation that they don't consider it as deviant...")
   apare pe **un slide NASA din 2014**, fără trimitere la pagină, într-o engleză care sună a traducere, și
   nu a putut fi găsit în niciun text scris de ea. **Nu se tipărește.** Același slide NASA lipește și două
   fraze ale lui Feynman aflate la ~460 de rânduri distanță într-un singur „citat" continuu. **NASA e ea
   însăși vector de folclor.**
   ✅ **Înlocuitori verificați**, din recenzia lui Gladwell la cartea ei: *„No fundamental decision was made
   at NASA to do evil. Rather, a series of seemingly harmless decisions were made that incrementally moved
   the space agency toward a catastrophic outcome."* · *„At NASA, problems were the norm. The word
   'anomaly' was part of everyday talk."* · *„It was not amorally calculating managers violating rules that
   was responsible for the tragedy. **It was conformity.**"*

2. **Problema retrospectivei — și e recunoscută chiar în raportul oficial**, p. 197: *„Feynman famously
   compared launching Shuttles with known problems to playing Russian roulette. But **that characterization
   is only possible in hindsight.** It is not how NASA personnel perceived the risks as they were being
   assessed, one launch at a time."* Și: *„**Taken one at a time, each decision seemed correct.**"*
   **Trebuie pus în text de noi**, altfel scriem o poveste morală despre oameni care „au ignorat semnalele".

3. **PROVENIENȚĂ: Gladwell a scris recenzia cărții lui Vaughan** în *The New Yorker*, ianuarie 1996, iar
   eseul e reluat în *What the Dog Saw*. **Scriem o carte în stilul lui Gladwell — nu putem folosi o
   poveste pe care a analizat-o el, în forma în care a analizat-o el.** Mai mult: teza lui e că **nu există
   niciun răufăcător și nicio lecție curată**, aproape opusul felului în care e folosită povestea în
   cărțile de business. Dacă o folosim, trebuie să mergem unde nu merge el.

⚠️ **Alte două lucruri care ne-ar putea contrazice:** inginerii de la Thiokol **chiar au obiectat, clar și
în scris** — există o lucrare co-semnată de unul dintre ei care respinge direct teza populară că aveau
datele și doar le-au prezentat prost. Iar „toată lumea a normalizat treptat" se ciocnește de înregistrarea
din seara dinaintea lansării, unde e o poveste de management-care-suprascrie-inginerii. **Ambele sunt
adevărate; o carte care spune doar una spune jumătate.**
⚠️ **Cele două temperaturi se confundă constant:** 51°F e ambientul celei mai reci lansări anterioare;
53°F e temperatura garniturii. Nu sunt același lucru.
⚠️ O sinteză sistematică din 2023 constată că, după ~30 de ani, conceptul e aproape exclusiv studii de caz
și comentariu, **nu teorie testată.**

✅ **Alternativa empirică, dacă vrem mecanismul dovedit și nu doar ilustrat:** Dillon & Tinsley,
*Management Science* 2008 — experimental, arată că **rezultatele reușite care conțin near-miss-uri cresc
asumarea ulterioară de risc.** E exact mecanismul nostru, testat, nu povestit.

### ✅ 3M — indicele de vitalitate devenit țintă de bonus
Partea cunoscută, integral primară din *BusinessWeek*, 11 iunie 2007: McNerney vine de la GE, impune
Six Sigma **inclusiv în laboratoare**, profituri +22%/an, marjă de la 17% la 23% — și proporția
vânzărilor din produse mai noi de cinci ani scade de la o treime la un sfert.

- Buckley: *„Invention is by its very nature a disorderly process. You can't put a Six Sigma process into
  that area and say... I'm going to schedule myself for three good ideas on Wednesday and two on Friday."*
- Un vicepreședinte din cercetare, despre mecanism: metrica devenise **câte proiecte black-belt și
  green-belt ai finalizat**, așa că *„people were going around dreaming up green-belt programs to fill
  their quota."* Și: *„We were letting the process get in the way of doing the actual invention."*
- **Nuanță:** Buckley **nu** a desființat Six Sigma. A eliminat **obligația cercetătorilor** de a se
  conforma obiectivelor Six Sigma. Restul companiei a rămas. **Asta e mai bună — e literalmente teza:
  unealta pentru cunoscut rămâne unde e cunoscutul.**

**Și partea nouă, din depunerile la SEC.** 3M măsoară explorarea printr-un New Product Vitality Index.
În februarie 2010 l-a transformat în **țintă de bonus** — 20% din acțiunile de performanță ale
executivilor. Apoi a urcat ștacheta de la 29% la 33%, apoi la 34%. Rezultatul, în cuvintele companiei:
**„No shares were earned based on 2015 and 2016 performance for this metric."** Iar după 2017 cuvântul
„vitality" **dispare complet** din depunerile 3M.

Au măsurat explorarea. Au făcut din măsurătoare o țintă. Au ratat-o. Au renunțat la măsurătoare.
**Goodhart documentat în depuneri semnate.**

**Perechea care transformă anecdota în tipar:** Nardelli și McNerney au concurat amândoi pentru
succesiunea lui Welch la GE. Amândoi au pierdut. **Amândoi au devenit CEO în decembrie 2000** — Nardelli
la Home Depot, McNerney la 3M. Același playbook. Home Depot: venituri de la 45,7 la 81,5 miliarde,
profit dublat — și acțiunea plată, în timp ce Lowe's se dubla.

### ✅ Toyota — compania care și-a omorât propria metrică
Toyota publică pe site-ul japonez un tabel an cu an, 1951–2011. Vârful: **1986, 2.648.710 de sugestii,
47,7 per persoană eligibilă.** În **1993: 929.257.**

De ce a căzut la mai puțin de jumătate în doi ani? Din istoria TQM proprie a companiei: *„competitive
fever over proposal quantity made it difficult for supervisors to guide subordinates through improvement
activities"* — așa că Toyota **a desființat țintele numerice la nivel de companie** și a trecut de la
cantitate la calitatea conținutului.

**Compania cea mai citată din lume pentru o metrică și-a omorât metrica pentru că metrica începuse să
o mintă.** Complet nefolosit în engleză. Candidat serios pentru finalul capitolului.

❌ **„2 milioane de sugestii pe an" — adevărat ultima oară în 1991.** Cifra actuală: ~810.000, 14,4 per
persoană, și doar pentru muncitorii calificați din fabrici.
❌ **Rata de implementare de 95%+ — fără sursă primară.** Singurele cifre publicate vreodată de Toyota
sunt dintr-un comunicat din 1973: peste 70% adoptate, în creștere de la 29% în 1956. Iar sursa cea mai
acreditată pentru „98%" e un fost manager Toyota care **o marchează el însuși ca zvon**.
✅ **Citatul lui Eiji Toyoda despre de unde au luat sistemul:** *„I got a copy of the pamphlet that they
were using at Ford... But when I visited Ford later, they told me that they had stopped using the
suggestion system; that it didn't work."* Ford l-a inventat și a renunțat. Toyota l-a ținut 75 de ani.

**Ce compromite povestea, verificat și devastator:** penalitatea DOJ de 1,2 miliarde din martie 2014.
Detaliul operațional: pe 21 octombrie 2009 inginerii Toyota au anulat o instrucțiune de schimbare de
design; personalul a fost anunțat **oral** și *„were also instructed not to put anything about the
cancellation in writing"* — *„contrary to TOYOTA's own standard procedures"*, ca *„to prevent NHTSA from
learning about the sticky pedal problem."*
**Compania construită pe scoaterea imediată a problemelor la suprafață a instituit o procedură
deliberată fără urmă pe hârtie ca să ascundă una.**
Și Akio Toyoda în fața Congresului, în limbajul propriului sistem: *„We pursued growth over the speed at
which we were able to develop our people and our organization."*

❌ **Tragerile de andon pe zi: netrasabile.** Am verificat sursa canonică — nu conține niciun număr.
✅ **Înlocuitorul, sursat, despre uzinele GM care au copiat hardware-ul fără cultura:** *„In some of the
factories where they installed the andon cord, workers got yelled at when they pulled it. **A few plants
even cut the cords down.**"*

---

## D. Cifre record în timp ce capabilitatea se distruge

### ✅ Kraft Heinz — cea mai curată, integral din SEC
Între 2016 și 2018: publicitatea de la **708 la 584 de milioane**, cercetarea de la 120 la 93 — în timp
ce **marja operațională urca de la 21,1% la 23,1% pe vânzări în scădere.**

**21 februarie 2019:** deprecieri de **15,4 miliarde într-un singur trimestru**, în principal pe mărcile
Kraft și Oscar Mayer. Pierdere netă pe trimestru de 12,6 miliarde.

**Detaliul care face povestea, nespus nicăieri:** publicitatea a fost repusă imediat — 976 de milioane
în 2019, **1.070 în 2020**, peste un miliard în fiecare an de atunci. **Economia nu fusese economie.
Fusese amânare.** În 2025 compania s-a desfăcut înapoi în părțile din care fusese asamblată.

⚠️ **De spus în text:** există o anchetă SEC din octombrie 2018 pe zona de achiziții, separată de
deprecieri. Teza noastră e „cifrele au fost oneste" — trebuie precizat explicit că ancheta viza altceva.

### ⚠️ Boeing — o singură frază, nu mai mult
**64 de miliarde către acționari între 2013 și 2019** (43,4 răscumpărări + 20,8 dividende), apoi
**35,7 miliarde pierderi cumulate în 2019–2024.** Cheltuiala de cercetare la minimul deceniului în 2014,
exact în anii cu răscumpărări maxime.

Cifra e curată. Dar povestea completă include ascundere deliberată față de autoritatea de reglementare,
deci nu mai e „cifre oneste, afacere golită" și ne diluează teza. **O frază, atât.**

### ✅ Adobe — inversul, și singurul candidat care satisface criteriul „deliberat"
**13 decembrie 2012**, comunicat intitulat *„Adobe Reports Record Quarterly and Annual Revenue."* În
același comunicat, CFO-ul: *„we are confident fiscal 2013 will be the pivotal year for the transition."*

Profitul net: de la 833 de milioane (2012) la **290 (2013)** — minus 65% — și patru ani până la
revenire. În tot acest timp abonamentele creșteau cu 402.000 într-un singur trimestru.

⚠️ **Nuanța onestă, care e mai bogată decât varianta simplă:** Adobe **nu a spus niciodată** că va fi o
afacere mai proastă. **A schimbat unitatea de măsură** — a învățat piața să citească abonamente și venit
recurent în loc de profit GAAP. Fiecare comunicat din acei ani are titlu triumfal. Pentru capitol asta e
util: **poți rata fiecare cifră din viziune doar dacă ai dinainte o altă dovadă pe care să o citești.**
Dacă scriem „Adobe le-a spus investitorilor că cifrele vor fi mai proaste", ne expunem.

❌ **Lego și Netflix/Qwikster — nu satisfac criteriul.** Lego nu a acceptat nimic deliberat; era în
faliment iminent. E turnaround, categorie diferită și mult mai comună. Qwikster a fost un eșec de
execuție urmat de o scuză.

---

## E. Ținta fără metodă

### ★ TOSHIBA — piesa centrală. Mai bună decât Sears.

**De ce e disponibilă:** raportul comisiei independente de anchetă are 303 pagini și **nu a fost tradus
niciodată în engleză.** Toshiba a promis o traducere în iulie 2015; agentul a sondat 465 de poziții de
URL în arhiva lor de relații cu investitorii — nu a apărut niciodată. **Fiecare „citat" englez care
circulă azi e redarea neatribuită a unui jurnalist.** Materialul e practic neexploatat în Occident.

Comisia a fost prezidată de **Koichi Ueda**, fost Procuror-Șef al Parchetului de pe lângă Înalta Curte
din Tokyo.

**SCENA DE DESCHIDERE — raportul are un titlu de secțiune dedicat, la pagina 228:**
> **„Cerere de îmbunătățire a profitului cu 12,0 miliarde de yeni, cu 3 zile rămase (T2 2012)"**

27 septembrie 2012, Ședința Lunară a Președintelui. Divizia raportează că pierderea operațională
semestrială s-a deteriorat la minus 24,8 miliarde de yeni. Președintele **Norio Sasaki** cere ferm o
îmbunătățire de **12 miliarde de yeni în cele trei zile rămase**, și rezultatul deliberărilor a doua zi.

Directorii au lucrat toată noaptea. Au prezentat la 12:10, apoi la 14:00 în fața lui Sasaki. Au propus
11,9 miliarde de „măsuri", din care **10,4 miliarde erau ficțiune contabilă**. Nu mai era timp nici
măcar să renegocieze cu furnizorii, așa că Toshiba și-a vândut propriul stoc propriilor filiale, la
prețuri mascate, ca să înregistreze marja.

**Nume, dată, cifră. Principiul vine după. E scena Gladwell pe care o căutam.**

**Și avantajul decisiv: compania însăși a dat mecanismului un nume — „Challenge".** Nu trebuie să-l
inventăm noi.

**Constatarea comisiei despre ce era Challenge, p. 42:**
> *„Ceea ce în mod propriu nu era decât o cifră aproximativă de prognoză — un buget, o țintă — **devenise,
> fără ca cineva să observe, un număr de profit obligatoriu de atins**, iar compania era împinsă într-o
> situație în care nu avea de ales decât să se năpustească să-l realizeze."*

**Și de ce nu exista metodă, p. 52 — teza noastră, scrisă de o comisie oficială de anchetă:**
> *„Acest «Challenge» **era adesea emis la Ședințele Lunare ținute când mai rămânea foarte puțin până în
> ultima zi a trimestrului.** Ca urmare, compania căreia i se dădea un «Challenge» constata că, în
> firimitura de timp rămasă, **era imposibil să producă vreo îmbunătățire mare de profit prin chiar și cel
> mai mare efort comercial** — și astfel era împinsă în situația de a nu avea altă opțiune decât metoda
> improprie de a umfla profitul aparent."*

**MOMENTUL EXACT ÎN CARE O PROBLEMĂ DE CUNOAȘTERE DEVINE UNA DE PRESIUNE — p. 188, februarie 2014.**
Președintele Tanaka: *„Adu-l la zero orice ar fi. După toată restructurarea, o pierdere de 4,6 miliarde
nu e ceva ce pot accepta."* Șeful de divizie:
> ***„Pe capacitate reală ne lipsesc 2,3 miliarde... Vă rog să-mi dați puțin mai mult timp."***

Tanaka: ***„Orice s-ar întâmpla, adu-l la cel mult minus 2,0 miliarde."***

**Omul a rostit decalajul de capacitate cu voce tare. Răspunsul a fost din nou cifra.**

**Trei dovezi că nu e o poveste cu ticăloși:**
1. **Directorul general nu credea că ordonă o fraudă.** Mărturia lui Sasaki, p. 231: știa că profiturile
   veneau din tranzacțiile respective, *„dar niciodată n-am instruit pe cineva să umfle profiturile... e
   nesănătos ca afacere și le tot spuneam să reducă volumul."* **Comisia acceptă că a spus asta — și
   constată că i-a încolțit oricum**, pentru că a impus Challenge-uri mari și a refuzat să lase umflarea
   să fie desfăcută. Niciun răufăcător necesar.
2. **Bucla de escaladare, în cuvintele comisiei, p. 64:** profitul tras în față face mai grea înregistrarea
   în perioada următoare, iar *„pentru că un Challenge excesiv era stabilit și în acele perioade, o
   contabilitate improprie și mai mare devenea inevitabilă. **Prin repetarea acestui ciclu, amploarea ei
   s-a extins."*** Cifrele confirmă: soldul umflat era 14,3 miliarde în 2008, **27,3 când a plecat un
   director general, 65,4 când a plecat următorul.**
3. **Nimeni nu a semnalat nimic, șapte ani.** Linia internă de raportare primea zeci de sesizări pe an.
   **Nici măcar un singur element legat de această chestiune nu a fost vreodată raportat.**

**Constatarea despre cultură, p. 278**, titlu de secțiune dedicat: *„La Toshiba **exista o cultură
corporativă în care nu era posibil să mergi împotriva voinței superiorilor tăi.**"*

**Cifre verificate:** ⚠️ **224,8 miliarde de yeni** e restatement-ul final total (comunicat Toshiba,
7 septembrie 2015). Cifra de 151,8 care circulă e **doar subsetul din mandatul comisiei.** Penalitate
recomandată: 7,37 miliarde de yeni. **Nouă demisii pe 21 iulie 2015**, inclusiv președintele și doi
foști președinți.

⚠️ **Ce compromite povestea, și trebuie spus în text:** e fraudă contabilă, deci cititorul sosește
gândind „escroci" — mărturia lui Sasaki îl mută. Directorii generali nu erau oameni obișnuiți — ține
camera pe șeful de divizie. Și 40–45% din remunerația directorilor era evaluată de la **0× la 2×** pe
rezultatele de final de perioadă, deci e **parțial și o poveste de stimulente, nu pur una de cunoaștere.**
Spune asta.

✅ **Proveniență scăzută spre moderată — punctul dulce.** Scandalul e cunoscut; **mecanismul nu.** Căutări
în literatura academică: Toshiba apare ca eșec *de guvernanță*, dar **nicio lucrare nu dezvoltă „Challenge"
ca patologie de stabilire a țintelor.**

### ★ DAIHATSU (2023) — al doilea caz, și mai bun pe „oameni obișnuiți"

Raport de 162 de pagini, comisie prezidată de un fost președinte de tribunal. **174 de nereguli în 25 de
categorii de teste, 64 de modele.** Cel mai vechi caz: **1989.** Producția internă în ianuarie 2024:
**zero unități.** Nicio amendă.

**Fraza care depășește orice oferă Toshiba pe tema vinovăției:**
> *„Angajații implicați în abateri pot fi considerați **sacrificați de conducere și nu pot fi puternic
> blamați.** Prin urmare, cei care trebuie blamați în primul rând nu sunt angajații din prima linie, ci
> directorii de vârf."*

Și: *„angajați absolut obișnuiți."*

**Mecanismul:** graficele erau construite *„cu absolut nicio marjă de reacție dacă apărea o problemă"*.
Graficul era *„tratat în interiorul Daihatsu ca absolut"*, iar schimbarea lui cerea din partea conducerii
*„un act de curaj excepțional"*.

**SONDAJUL ANGAJAȚILOR E COMOARA.** 3.696 chestionați, **3.642 de răspunsuri — rată de 98,54%** — iar
comisia a reprodus textul liber **needitat.**

> **„Graficul-provocare devine treptat graficul-obligatoriu."**

Nouă cuvinte care conțin tot capitolul. Și, mai lung:
> *„Informația despre grafice și despre insuficiența orelor-om **chiar ajunge la conducerea superioară.**
> Dar din cauza climatului de «Și, ce ai de gând să faci?», soluțiile de a lungi programul sau de a adăuga
> oameni sunt excluse din capul locului."*

Și de ce onestitatea era opțiunea scumpă:
> *„Dacă ridici mâna, ești îngropat în explicații: «de ce nu ajungi la timp», «cum ai putea ajunge», «ce
> vei face»... **Nu pot spune că nu înțeleg impulsul de a recurge la o mutare interzisă.»"***

⚠️ **Ce compromite:** frauda precedă doctrina dezvoltării scurte cu 22 de ani — ținta a **industrializat**
un comportament existent, nu l-a creat. Și comisia numește *cultura organizațională*, nu graficul, drept
cea mai mare cauză reală. **Nu supralicita împotriva propriei surse.**

✅ **Proveniență foarte scăzută.** Zero lucrări academice. Nicio traducere engleză. Presa anglofonă are
cifrele-titlu și nimic din sondaj.

### 🔴 RAFINAREA TEZEI pe care o impune materialul

Daihatsu forțează o precizare, și e o îmbunătățire reală. Ce s-a întâmplat acolo **nu a fost o căutare** —
organizația a **interzis** căutarea, pentru că a raporta un rezultat negativ te costa personal, în timp ce
trișatul nu costa nimic.

**Formularea mai puternică, pe care ambele cazuri japoneze o documentează rând cu rând:**
> *O țintă fixată pe teren unde nimeni nu cunoaște metoda produce o căutare. Iar o organizație care
> pedepsește căutarea o împinge în subteran, de unde se întoarce ca fraudă.*

### ⚠️ Comisia Regală australiană (Hayne) — citatul celebru NU există în raportul final

**Cea mai importantă avertizare din tot dosarul.** Citatul despre *„greed / short term profit / basic
standards of honesty"* a fost căutat în toate cele trei volume: **zero rezultate.** Provine din **Raportul
Interimar**, a cărui gazdă a dispărut. **Versiunea care circulă provine dintr-o transcriere Wikipedia care
alterează timpul verbal.** Nu se tipărește ca verbatim fără o copie de bibliotecă.

Și *„too big to be governed"* **nu e Hayne** — absent din toate volumele.

✅ **Înlocuitori verificați, din raportul final:** *„Rewarding misconduct is wrong. Yet **incentive, bonus
and commission schemes throughout the financial services industry have measured sales and profit, but not
compliance with the law and proper standards.**"* (vol. 1, p. 2) Și: *„Focusing only on what is to be sold
is not enough. **How the employee does the job is at least as important as what the employee does.**"*
(vol. 1, p. 368)

🔴 **Două lucruri care ne contrazic și pe care trebuie să le punem NOI în text:**
1. **O bancă a rulat experimentul nostru și a obținut răspunsul greșit.** ANZ a eliminat țintele
   individuale de vânzări într-un district timp de 15 luni. Satisfacția clienților a crescut, implicarea
   angajaților a fost bună — **și vânzările au scăzut**, sub media națională. Banca a concluzionat că
   există „un rol pentru țintele de vânzări." (vol. 1, p. 372)
2. **Hayne respinge explicit încadrarea noastră:** *„it is those who engaged in misconduct who are
   responsible for what they did and for the consequences that followed."* (vol. 1, p. 4) Dacă morala
   noastră e „vinovată e ținta, nu oamenii", argumentăm împotriva Comisarului în timp ce îl citam.

### ❌ Post Office / Horizon — nu se potrivește, de renunțat
Coloana cauzală e un sistem informatic defect, o clauză contractuală și o instituție care a urmărit penal
în loc să investigheze. **Nu există o țintă numerică ambițioasă pe teren necunoscut.**

### ✅ Amagasaki, Japonia, 25 aprilie 2005
Un mecanic de 23 de ani intră într-o curbă limitată la 70 km/h cu **116**. Deraiere. **107 morți, 562 de
răniți.** Recupera **șaizeci de secunde** de întârziere.

Mecanismul: operatorul rula un program de „reeducare" numit *nikkin kyōiku* — plivit iarbă, abuz verbal,
rapoarte de căință scrise, pentru mecanicii care întârziau. **Comisia oficială de anchetă a stabilit că
sistemul de reeducare a fost o cauză probabilă a accidentului.**

Ținta era punctualitatea. Metoda era pedeapsa pentru întârziere. Nimeni nu a evaluat vreodată ce produce
metoda. **Dacă se confirmă la raportul original, e mai puternică decât Sears.**

⚠️ **De ridicat la sursa primară** (raportul comisiei japoneze de anchetă) înainte de tipar. Faptele
materiale sunt solide și consistente, dar agentul nu a citit raportul original.
✅ **Proveniență scăzută** — nu e în nicio carte mare de business.

---

## F. Experimentul ca înlocuitor al obiectivului

### ✅ Skunk Works — cortul de circ
Nu era spațiu în clădirea Lockheed, așa că echipa a lucrat **într-un cort de circ închiriat, lângă o
fabrică ce puțea.** E literalmente „lângă mașinărie, nu înăuntrul ei", și e o imagine pe care cititorul
o vede instantaneu. Verificat din paginile oficiale Lockheed.

**Regula 5 din cele 14 ale lui Kelly Johnson, cea mai valoroasă pentru noi:** *„There must be a minimum
number of reports required, but important work must be recorded thoroughly."* Distincția dintre
raportare (obligație către mașinărie) și dovadă (produsul experimentului).

Și: **143 de zile** pentru XP-80, cu șapte mai puțin decât cele 150 cerute. Contractul formal a sosit la
patru luni **după** ce începuse munca.

### ✅ Chesbrough pe Xerox — dovada rece, pe 35 de cazuri
A studiat 35 de organizații desprinse din Xerox între 1979 și 1998. **Spin-off-urile cu un om din Xerox
ca CEO au performat mai slab; cele cu investitori externi în consiliu, mai bine.** Iar practicile Xerox
*„caused its spin-offs to search locally near Xerox's own business, while spin-offs governed by outside
investors' practices searched a broader space."*

**Nu e anecdotă. E măsurat: proximitatea de mașinărie îngustează spațiul de căutare.** Cel mai riguros
suport empiric din tot research-ul pentru „construiește lângă mașinărie".

### ✅ Bank of America — cel mai bun exemplu de ce ai nevoie de grup de control
După instalarea monitoarelor TV la coadă, supraestimarea timpului de așteptare a scăzut de la **32% la
15%** în sucursala de test — dar în **sucursala de control a crescut de la 15% la 26%** în aceeași
perioadă. Fără control, ai fi crezut că e o îmbunătățire modestă.

Plus mecanica: ~20 de sucursale din Atlanta convertite în laborator; 200 de idei generate, **40 lansate
ca experimente formale**; o sucursală-prototip la sediu unde se repeta și se cronometra fiecare operațiune
**înainte** de testul cu clienți reali; regula de aur — problemele de design se rezolvă off-line.

❌ **„Ținta de eșec de 30%" — folclor, netrasabil.** Indiciile sugerează **inversul**: eșuau doar ~10%,
iar asta era discutată ca **problemă**.
⚠️ **Corecție la ce credeam:** articolul relevant e din **aprilie 2003**, nu 2001; numărul e **~20 de
sucursale, nu 25**.
⚠️ **Semnal de proveniență serios:** un singur cercetător a scris cazul Harvard, teaching note-ul,
articolul și două cărți pe temă. **Nu există relatare independentă.** Iar în 2022 a co-publicat cu
Loveman — deci două dintre poveștile candidate au **același cronicar**, care a ajuns să semneze împreună
cu unul dintre subiecții lui.

### ✅ Project Oxygen — o companie își testează propria credință fundamentală și pierde
Google credea că managerii nu contează: *„We are a company built by engineers for engineers."* În 2002
Page și Brin au eliminat managerii de inginerie. A durat câteva luni. Apoi au testat credința cu date
proprii. Scorurile de favorabilitate ale managerilor: de la 83% la 88% între 2010 și 2012; un
vicepreședinte de la 46% la 86% în două cicluri.

**E singurul caz din tot dosarul în care s-a testat o convingere, nu un buton.** Asta e diferența dintre
optimizare și explorare.
⚠️ Lista celor opt comportamente în ordine nu s-a putut verifica — site-ul re:Work e retras.

### ✅ Tesco — replica scurtă și non-americană
Președintele Tesco, după ce consiliul vede primele rezultate ale programului de fidelitate:
> *„What scares me about this is that you know more about my customers after three months than I know
> after 30 years."*

Cea mai curată ilustrare a punctului despre câmpul Source: **compania nu știa dacă instinctele ei sunt
bune, până când cineva a măsurat.**

### ⚠️ Capital One — contrapunctul care salvează capitolul de naivitate
Cifrele sunt reale și primare, din scrisorile către acționari: **14.000 de teste în 1997, 27.000 în 1998,
36.114 în 1999, peste 45.000 în 2000.**

**Dar concluzia e mai valoroasă decât povestea eroică:** e optimizare industrială **înăuntrul** modelului,
nu explorare a spațiului din jurul lui. Funcția-obiectiv era fixă și explicită în propriul 10-K —
*„maximizing returns on investment within given underwriting parameters."*

Și n-au văzut venind nimic. **16 iulie 2002:** autoritățile impun un memorandum de înțelegere; acțiunea
cade **39,8% într-o singură ședință**. Capitolul unu al memorandumului se numește *„Policies, Procedures,
Systems and Controls."* **Compania cu 45.000 de teste științifice pe an, pusă sub supraveghere pentru
proceduri și controale.**

Plus critica unei foste angajate: experimentele permit *„applying its findings as a profit-maximizing
mandate without giving the strategy a name such as, oh, 'predatory lending.'"*

Și **Capital One a încetat să publice numărul după 2000.**

❌ **„20 de bănci l-au refuzat" — folclor.** Sursele dau 20, „peste 20", ~30. Nu se dă un număr.
❌ **„Grupuri de control" la Capital One — inferență, nu citare.** Documentele publice spun „test
programs", „scientific testing protocol". Nu se pune în ghilimele.

### ❌ Harrah's — de folosit doar ca avertisment despre proveniența citatelor
**Citatul faimos nu există în articolul din 2003.** Agentul a obținut textul integral. Versiunea
auto-declarată de Loveman are **trei** elemente: *„theft, sexual harassment, and running an experiment
without a control group"* — MIT Technology Review, 18 februarie 2011.

**Citatul despre rigoare experimentală a fost el însuși transmis fără control, prin cărți de business, și
a pierdut un element pe drum.** E cea mai bună glumă pe care ne-o oferă materialul și susține exact
punctul despre câmpul Source.

Și compania: faliment în 2015 cu ~18 miliarde datorie; pierderi cumulate de ~8,8 miliarde între 2010 și
2014. **Cel mai disputat activ din faliment nu au fost clădirile, ci baza de date de clienți** — adică
exact produsul programului de experimentare.

---

## G. Coloana academică

- **Benner & Tushman**, *Administrative Science Quarterly* 2002 — **„Our results suggest that exploitation
  crowds out exploration."** 20 de ani de date pe brevete și certificări, două industrii.
- **Benner & Tushman**, *Academy of Management Review* 2003 (Best Article 2003, Decade Award 2013) —
  **„process management activities must be buffered from exploratory activities."** Teza noastră despre
  „construiește lângă mașinărie", formulată academic, cu premiu de deceniu.
- **Deniz** — adoptarea testării A/B **scade** probabilitatea schimbării radicale. **Nuanța anti-naivitate:
  un program de experimentare poate degenera exact ca Six Sigma la 3M.** Capital One e dovada.
- **Bagian et al.** — un premiu **fără bani** a dus completarea la timp a analizelor de cauză-rădăcină de
  la **52% la 94%**, și calitatea acțiunilor corective de la **34% la 70%**. Plus principiul: sistemul
  trebuie să fie *„a tool for learning and not accountability... not a counting exercise of the number
  of reports."*
- **Kachalia et al.**, *Annals of Internal Medicine* 2010 — după ce spitalul a început să recunoască
  erorile deschis și să ofere compensație din proprie inițiativă: procesele au scăzut de la 2,13 la 0,75
  la 100.000 de consultații, costurile totale de răspundere cu ~60%.

---

## H. LISTA DE ELIMINARE — cifre și citate care nu rezistă

Toate au fost verificate și niciuna nu se trasează la o sursă primară.

| Afirmație | Ce e de fapt |
|---|---|
| Rata de victorie a OPFOR la NTC (orice procent) | Centrul nu ține scor, prin politică. Urma se oprește la Tom Clancy, 1994, fără citare. Cifrele reale: ~63%. |
| Toyota implementează 95%+ din sugestii | Fără sursă primară. Singurele cifre publicate: >70% în 1973. Sursa cea mai acreditată o marchează ea însăși ca zvon. |
| Toyota primește 2 milioane de sugestii pe an | Adevărat ultima oară în 1991. Acum ~810.000. |
| Tragerile de andon pe zi (1.000 / 3.500) | Sursa canonică nu conține niciun număr. Netrasabil. |
| „De ce să te concediez? Tocmai am investit X milioane în educația ta" | Zero apariții în corpusul Google. Atribuirea canonică e Thomas Watson, cu suma plutind între 600.000 și 10 milioane — marker clasic de fabricație. |
| Loveman: „două lucruri te pot da afară" | Versiunea lui are trei elemente. Varianta cu două e nesursată. |
| Bank of America: ținta de eșec de 30% | Netrasabil. Indiciile sugerează inversul. |
| Capital One: „20 de bănci l-au refuzat" | 20 / >20 / ~30, în funcție de sursă. |
| Capital One: 28.000 de teste în 1999 | Coruptelă a lui 27.000 din 1998. |
| Coridoare NHS reclasificate ca saloane | Targa reclasificată drept pat. Coridorul e doar unde a fost pusă. |
| Buurtzorg înjumătățește costurile | Evaluarea KPMG: costul total per pacient a fost **mediu** când se includ costurile de cămin, medic și spital. |
| Novo Nordisk — funcția de „facilitator" | Neconfirmată. Nu apare în nicio pagină corporativă actuală. **Nu se scrie până nu se citește lucrarea academică din 2009.** |
| „91% dintre companiile cu Six Sigma au rămas sub S&P" | Sursa e o firmă de consultanță care vinde o metodologie concurentă. |

---

## I. Ce a rămas neacoperit

- **Deepwater Horizon · NASA / normalizarea devianței · Alcoa · Goodhart la sursă** — linia încă rulează.
- **Volkswagen · Boeing 737 MAX · Nokia · manifestările de zi cu zi, non-scandaloase** — linia încă rulează.
- **Pierdute** când un agent a picat la generarea raportului: SUBSAFE (programul de siguranță al
  submarinelor americane), Facilitated Learning Analysis din pompieri, studiile pe portavioane, Pixar
  Braintrust. **SUBSAFE și FLA erau cele mai promițătoare** — merită o rundă separată.
- **De verificat manual, valoare mare:** Bolger, *Dragons at War*, pp. 66–73 — singura scenă de debrief
  militar la persoana întâi, cu nume și dată. Necesită exemplar fizic.
