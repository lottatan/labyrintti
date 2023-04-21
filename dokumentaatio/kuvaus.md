# Ohjelman kuvaus

Ohjelma luo labyrintin käyttäjän antamien tietojen perusteella. Käyttäjä antaa labyrintille leveyden ja korkeuden väliltä 5-30. Ohjelma luo labyrintin ja käyttää kahta eri algoritmia sen ratkaisemiseen. Käytettävät algoritmit ovat Dead End Filling- ja Trémaux-algoritmit. Labyrintti alkaa ensimmäiseltä riviltä ja viimeisellä rivillä on mahdollisesti monta ulospääsyä.


## Algoritmit

### Dead End Filling

Dead End Filling -algoritmi, nimensäkin mukaisesti, täyttää labyrintistä kaikki umpikujat. Tämä jättää jäljelle kaikki mahdolliset reitit ulos labyrintistä.

### Trémaux

Trémauxin algoritmi pitää kirjaa taulukkomuodossa siitä, missä solmuissa on vierailtu. Vierailemattomien solmujen arvo on 0 ja jos solmussa vieraillaan, sen koko kasvaa. Kun algoritmissä päästään risteykseen, jossa on monta vaihtoehtoa, mihin suuntaan kuljetaan, valitaan se suunta, jonka arvo on taulukossa pienin, jos mahdollista. Jos kaikilla mahdollisilla suunnilla on sama arvo, arvotaan niistä jokin kulkusuunta. Algoritmi antaa käyttäjälle yhden mahdollisen reitin ulos labyrintistä.


Molemmat algoritmit olivat minulle entuudestaan vieraita.