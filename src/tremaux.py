import random

class Tremaux:
    def __init__(self, labyrintti):
        self.labyrintti = labyrintti
        self.y = len(self.labyrintti)
        self.x = len(self.labyrintti[0])
        
        self.aloitusy, self.aloitusx = self.aloituskohta()


    def aloituskohta(self):
        """Tässä metodissa etsitään labyrintin ensimmäiseltä riviltä aloituskohta"""
        for i in range(0, self.x):
            if self.labyrintti[0][i] == ".":
                alkuy, alkux = 0, i
        
        return alkuy, alkux
    
    def ratkaise(self):
        """Tässä metodissa ratkaistaan algoritmi niin, että tehdään taulukko, jossa pidetään kirjaa vierailluista solmuista. Taulukko alustetaan niin, että jokainen
        solmu saa arvoksi 0. Kun solmussa vieraillaan, vaihdetaan taulukon arvoksi 1. Kuljettua polkua pidetään muistissa pinossa. Jos tullaan risteykseen, missä on monta suuntaa, mihin ei olla kuljettu,
        niin arvotaan suunta, johon mennään. Lopussa palautetaan kuljetun polun koordinaatit."""

        alku = (self.aloitusy, self.aloitusx)

        pino = [alku]
        vierailtu = [[0 for i in range(self.x)] for j in range(self.y)]
        vierailtu[alku[0]][alku[1]] = 1
        polku = []

        while pino:
            atm = pino[-1]
            y = atm[0]
            x = atm[1]

            polku.append((y, x))

            if y == self.y-1 and self.labyrintti[y][x] == ".":
                return(pino, polku)

            ei_vierailtu = []

            if 0 <= y < self.y-1:
                if self.labyrintti[y+1][x] == "." and vierailtu[y+1][x] == 0:
                    ei_vierailtu.append((y+1, x))
            if 0 < y <= self.y-1:
                if self.labyrintti[y-1][x] == "." and vierailtu[y-1][x] == 0:
                    ei_vierailtu.append((y-1, x))
            if 0 <= x < self.x-1:
                if self.labyrintti[y][x+1] == "." and vierailtu[y][x+1] == 0:
                    ei_vierailtu.append((y, x+1))
            if 0 < x <= self.x-1:
                if self.labyrintti[y][x-1] == "." and vierailtu[y][x-1] == 0:
                    ei_vierailtu.append((y, x-1))

            if len(ei_vierailtu) == 1:
                seuraava = ei_vierailtu[0]
                vierailtu[seuraava[0]][seuraava[1]] = 1
                pino.append(seuraava)
            elif len(ei_vierailtu) > 1:
                seuraava = ei_vierailtu[random.randint(0, len(ei_vierailtu)-1)]
                vierailtu[seuraava[0]][seuraava[1]] = 1
                pino.append(seuraava)
            else:
                pino.pop()
