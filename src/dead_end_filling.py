
class DeadEndFilling:
    def __init__(self, labyrintti):
        self.labyrintti = labyrintti
        self.korkeus = len(self.labyrintti)
        self.leveys = len(self.labyrintti[0])


    def aloituskohta(self):
        """Tässä metodissa etsitään labyrintin ensimmäiseltä riviltä aloituskohta"""
        for i in range(0, self.leveys):
            if self.labyrintti[0][i] == ".":
                alkukorkeus, alkuleveys = 0, i
        
        return alkukorkeus, alkuleveys
    
    def onko_umpikuja(self, korkeus, leveys):
        """Tässä metodissa tarkastetaan, onko kyseinen kohta umpikuja tarkastamalla, onko viereisestä neljästä solmusta kolme seinää.
        Jos on, niin muutetaan myös kyseinen kohta seinäksi"""

        laskuri = 0

        if self.labyrintti[korkeus][leveys] == '.':

            if 0 <= korkeus < self.korkeus-1:
                if self.labyrintti[korkeus+1][leveys] == '#':
                    laskuri += 1
                   
            if 0 < korkeus <= self.korkeus-1:
                if self.labyrintti[korkeus-1][leveys] == '#':
                    laskuri += 1

            if 0 <= leveys < self.leveys-1:
                if self.labyrintti[korkeus][leveys+1] == '#':
                    laskuri += 1

            if 0 < leveys <= self.leveys-1:
                if self.labyrintti[korkeus][leveys-1] == '#':
                    laskuri += 1

            if laskuri == 3:
                self.labyrintti[korkeus][leveys] = '#'
                return True
   
        return False
            

    def ratkaise(self):
        """Tämä metodi ratkaisee kaikki polut, joilla on mahdollista päästä ulos labyrintistä"""
        polku = True

        while polku:
            polku = False
            for korkeus in range(self.korkeus):
                for leveys in range(self.leveys):
                    if self.onko_umpikuja(korkeus, leveys):
                        polku = True
        
        ratkaisu = self.labyrintti
        return ratkaisu


if __name__ == "__main__":
    labyrintti = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#'],
        ['#', '.', '#', '.', '#', '#', '.', '#', '.', '.', '#', '#', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '.', '.', '.', '#', '#', '.', '.', '#', '#'],
        ['#', '.', '#', '.', '#', '#', '#', '#', '.', '#', '.', '.', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '.', '#', '.', '#', '#', '.', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '.', '#', '#', '.', '#', '.', '#', '.', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '.', '#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '#', '#', '.', '#', '#', '.', '#', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '.', '#', '.', '.', '#', '#', '#', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '#', '#', '.', '#', '#', '.', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '#', '#', '.', '#', '#', '.', '.', '.', '#']
        ]
    
    laby = DeadEndFilling(labyrintti)
    laby.ratkaise()
