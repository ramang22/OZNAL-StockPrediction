# OZNAL-StockPrediction

# Project BattlePlan

## Toto treba vsetko odovzdat
- [x] Project in R (10b)
- [ ] Písomná správa
- [ ] Vyčistené raw data
- [ ] Kód, okomentovaný, knitted

## Data (10b)

- [x] Opisat odkial mame data a ake su to data
- [ ] Opisat ako sme jednotlive data spracovali a vycistili
- [ ] Dostat bonus 5 bodov za to ze sme sa kaslali so sparkom a velkym mnozstvom dat
- [ ] Dalsie bonus body za to ze ziskavame data z textu (ticker) a jednotlivy sentiment toto treba zahrnut do docu
- [ ] Treba tu opisat ako sme minili jednotlive iteracie datasetu, resp. co sme menili to je ez. Pridavali sme stlpce a tak

## Prieskumná analýza dát a definícia pracovných hypotéz (20b)

- [ ] Hypotézy
- [ ] Základný opis dát + charakteristika (počet záznamov, počet atribútov, typ, význam a distribúcia)
- [ ] Dokázať že naše dáta sú reprezentatívne
- [ ] Dokázať že prečo je náš dataset unikátny
- [ ] Identifikácia problémov v dátach + riešenie problémov v dátach - A.K.A analyzovat stlpce samostatne
- [ ] Párová analýza dát
- [ ] Argumenty pre hypothesis-free vs hypothesis-driven vs endpointy 

## Čistenie dát pre ďalšie analýzy (10b)

- [ ] Vycistit data podla problemov, ktore sme identifikovali. Ak nieco zmeni data znova analyza pre dane data
- [ ] Integráciu  všetkých  dát,  prípadne  deduplikácia.  Čistenie  šumu  a  odstraňovanie extrémnych hodnôt.  
- [ ] Vytvorenie trening data set a test dataset
- [ ] Znova analyza dat a povedat co sa zmenilo v distribucii

##  Štatistické učenie, zhlukové analýzy a nachádzanie vnútorných vzorcov v dátach (15b) 

- [ ] Natrenovat aspon 4 modely
- [ ] Model statistickeho ucenia
- [ ] Model zhlukovej analyzy
- [ ] Model Bayesovej techniky
- [ ] Model klasifikacneho algoritmu
- [ ] ASPOŇ 4 hypotezy pre statisicke ucenie a zhlukovu analyzu, analyticke kroky na uskutocnenie, analyticku komplexnost
- [ ] Toto nemam sajnu

V  prípade,  že  budete  hypotézy  dokazovať  technikami  redukcie  dimenzionality  dát, 
porovnajte  ich  výsledky  oproti  analýze  používajúcu  stromové  štruktúry  a  zhlukovú 
analýzu. Viete popísať hlavné rozdiely vo výsledkoch? Zmenila sa granularita výsledkov? 
Zmenilo  sa  preusporiadanie  výsledných  skupín?  Aké  analytické  parametre  podľa  vás 
predstavujú  zlatú  strednú  cestu  a  prečo  im  veríte?  Ovplyvňuje  použitie  náhodného 
samplovania vstupných dát výsledky alebo nie? 

- [ ] Toto nemam sajnu 2

Za  predpokladu,  že  je  vás  vstupný  dátaset  reprezentatívny,  viete  identifikovať  závislé 
premenné ktoré bude možné použiť ako vhodné priory na hľadanie výstupov, na ktoré 
nemáme priame dáta, ale môžu pomôcť dokázať vase hypotézy?   

## Bayesovská štatistika (15b) 

- [ ] identifikova ASPON 2 procesy v nasich datach a namodelovat ich pomocou Bayesa
- [ ] Ak sa da porovnat hierarchicky a nehierarchicky MCMC model
- [ ]  Ak  vami  vytvorený  hierarchický model nie je konvergentný, uveďte v správe dôvody a vysvetlite techniky, ako by bolo možné dodatočnú konvergenciu zabezpečiť (napríklad doplnením priorov)
- [ ]   Je možné pre váš dataset použiť na predikciu Metropolis ‐ Hastings algoritmus, ak áno ako, ak nie ‐ prečo

## Zdroje

* https://towardsdatascience.com/downloading-historical-stock-prices-in-python-93f85f059c1f
* https://www.kaggle.com/unanimad/reddit-rwallstreetbets
* https://www.kaggle.com/mattpodolak/rwallstreetbets-posts-and-comments?select=wallstreetbets_posts.csv
* https://www.kaggle.com/gpreda/reddit-wallstreetsbets-posts

## Mozno pomoze 
* https://bookdown.org/rdpeng/exdata/exploratory-graphs.html
* https://github.com/johnmyleswhite/ML_for_Hackers
