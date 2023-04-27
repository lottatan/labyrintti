# Testausdokumentti

## Projektin testaus

Tämä projekti on testattu yksikkötestauksella unittestin avulla. Testaus kattaa src-kansion tiedostot poislukien index.py tai ui.py tiedostot. Testejä on yhteensä kahdeksan, ja ne testaa eri ohjelman toiminnan kannalta tärkeiden funktioiden toimintoja. Nämä testit testaavat muun muassa labyrintin luomista, sen eri ratkaisuja ja ratkaisualgoritmeien eri toimintoja. Testit voidaan suorittaa komennolla `` pytest src ``. 

![coverage-report](coverage-report1.png)

## Pylint virheet ja koodin laatu

Pylint antaa koodin arvosanaksi 10/10 ja arvosanan voi suorittaa komennolla `` poetry run invoke lint ``.

## Järjestelmän toiminta

Järjestelmä antaa virheilmoituksen aina, jos käyttäjä syöttää liian suuren tai pienen luvun.

## Suorituskyky

Testaamalla ohjelman toimintaa nxn kokoisilla syötteillä, saadaan luotua kaaviot, jotka kuvaavat algoritmien nopeutta eri kokoisilla syötteillä.
Seuraavassa taulukossa on tieto syötteiden koosta ja kummankin algoritmin ratkaisunopeudesta. Nopeus on ilmaistu nanosekunteina.

![taulukko](taulukko.png)

Seuraavassa taulukossa on kuvaus Trémauxin algoritmin nopeudesta:

![Trémaux-kaavio](tremaux1.png)


Seuraavassa taulukossa on kuvaus Dead-End-Filling algoritmin nopeudesta:

![Dead-End-Filling-kaavio](dead-end-filling1.png)

Kun laitetaan molemmat kaaviot yhteen, huomataan, että Dead-End Filling -algoritmi on reilusti Trémauxin algoritmia hitaampi.

![molemmat](molemmat.png)



