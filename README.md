# Bellmanův–Fordův algoritmus

Jde o algoritmus, který na základě prohledávání grafu nalezne nejkratší cestu do všech uzlů z jednoho startovního. Tedy počítá nejkratší cestu v ohodnoceném grafu z jednoho uzlu do uzlu dalšího. Velkou výhodou tohoto algoritmu oproti běžně užívanému Djikstrovu je, že dokáže procházet graf se záporně ohodnocenými hranami. Tento algoritmus je užit v RIP (Routing Information Protocol). Tento protokol patří mezi nejstarší používané směrovací protokoly v sítích IP. Avšak své uplatnění pořád nachází v menších sítích. Je to z důvodu jednoduchosti a jeho nenáročné konfiguraci. [zdroj] (https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)

## Průběh algoritmu

Oproti zmíněnému Djikstrovu (D) algoritmu je B-F pomalejší. Ale dokáže procházet graf se záporně ohodnocenými hranami. K zjištění nejkratší cesty je použita metoda relaxace hran. Díky relaxaci je možné zjistit vždy nejkratší vzdálenost od uzlu, který je označen jako START (0).  Pokud je zjištěno, že hodnota je nižší než vzdálenost, kterou má uzel jako původní, pak je původní hodnota nahrazena novou – nižší. Zásadní rozdíl oproti D je v způsobu procházení grafu. [zdroj] (https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)

## Zlepšení procházení grafu

Program byl zlepšen na základě implementace Shortest Path Faster Algorithm, která byla poprvé uvedena Edwardem F. Moorem v roce 1959. Zrychlení iterací spočívá v tom, že pokud uvažovaný uzel při relaxaci nezmění hodnotu, pak nejsou hrany z něj vycházející dále uvažovány. Dojde k jejich přeskočení, a proto je takt programu urychlen.

## Jednotlivé skripy

### bellman_ford.py

Jednoduchý skript, který vznikl, při implementaci B-F. 3lo o jakousi testovací jednoduchou verzi, na které měly být podchyceny možné problémy. Ovšem jedná se o funkční prográmek, a proto byl zanechán.

### generate_graph.py

Jde o generátor cvs souboru, které slouží jako vstup pro hlavní program. V csv souborech jsou uloženy informace vždy o konkrétním grafu, který má být prohledán. Má v něm být nalezena nejkratší cesta pomocí B-F algoritmu. Hlavní omezení v tomto programu jsou:

* Uzel má nejvýše 5 sousedů (je napojen maximální 5ti hranami)
* Generuje se méně záporných hodnot hran
* Mezi dvěma uzly vede pouze jedna hrana

### graph.py

### run.py

## Příklad výstupu

## Spuštění 