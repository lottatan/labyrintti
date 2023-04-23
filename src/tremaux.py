import random

class Tremaux:
    def __init__(self, labyrintti):
        self.labyrintti = labyrintti
        self.korkeus = len(self.labyrintti)
        self.leveys = len(self.labyrintti[0])
        
        self.aloituskorkeus, self.aloitusleveys = self.aloituskohta()


    def aloituskohta(self):
        """Tässä metodissa etsitään labyrintin ensimmäiseltä riviltä aloituskohta"""
        for i in range(0, self.leveys):
            if self.labyrintti[0][i] == ".":
                alkukorkeus, alkuleveys = 0, i
        
        return alkukorkeus, alkuleveys
    
    def ratkaise(self):
        """Tässä metodissa ratkaistaan algoritmi niin, että tehdään taulukko, jossa pidetään kirjaa vierailluista solmuista. Taulukko alustetaan niin, että jokainen
        solmu saa arvoksi 0. Kun solmussa vieraillaan, vaihdetaan taulukon arvoksi 1. Kuljettua polkua pidetään muistissa pinossa. Jos tullaan risteykseen, missä on monta suuntaa, mihin ei olla kuljettu,
        niin arvotaan suunta, johon mennään"""

        alku = (self.aloituskorkeus, self.aloitusleveys)

        pino = [alku]
        vierailtu = [[0 for i in range(self.leveys)] for j in range(self.korkeus)]
        vierailtu[alku[0]][alku[1]] = 1

        while pino:
            atm = pino[-1]
            korkeus = atm[0]
            leveys = atm[1]

            if korkeus == self.korkeus-1 and self.labyrintti[korkeus][leveys] == ".":
                return(pino)

            ei_vierailtu = []

            if 0 <= korkeus < self.korkeus-1:
                if self.labyrintti[korkeus+1][leveys] == "." and vierailtu[korkeus+1][leveys] == 0:
                    ei_vierailtu.append((korkeus+1, leveys))
            if 0 < korkeus <= self.korkeus-1:
                if self.labyrintti[korkeus-1][leveys] == "." and vierailtu[korkeus-1][leveys] == 0:
                    ei_vierailtu.append((korkeus-1, leveys))
            if 0 <= leveys < self.leveys-1:
                if self.labyrintti[korkeus][leveys+1] == "." and vierailtu[korkeus][leveys+1] == 0:
                    ei_vierailtu.append((korkeus, leveys+1))
            if 0 < leveys <= self.leveys-1:
                if self.labyrintti[korkeus][leveys-1] == "." and vierailtu[korkeus][leveys-1] == 0:
                    ei_vierailtu.append((korkeus, leveys-1))

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
                 
        return ("Ei ratkaisua")
