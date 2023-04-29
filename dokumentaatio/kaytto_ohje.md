# Käyttöohje

1. Kloonaa repositorio koneellesi ja siirry repositorion juureen antamalla terminaalissa komento 

``cd labyrintti``

## Käynnistysohje

1. Asenna riippuvuudet seuraavalla komennolla:

`` poetry install ``

3. Asenna colorama moduuli komennolla:

`` pip install colorama ``

3. Käynnistä ohjelma komenolla:

``python3 src/index.py``

Tai virtuaaliympäristössä komennolla:

`` poetry run invoke start``

Virtuaaliympäristöön pääset komennolla:

``poetry shell``

Ohjelma hyväksyy ainoastaan kokonaislukuja 5 ja 60 väliltä. Ohjelman ajamiseen tarvittavat käskyt löytyvät myös tasks.py tiedostosta.