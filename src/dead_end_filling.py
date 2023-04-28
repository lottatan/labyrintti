
class DeadEndFilling:
    def __init__(self, labyrintti):
        self.labyrintti = labyrintti
        self.y = len(self.labyrintti)
        self.x = len(self.labyrintti[0])


    def aloituskohta(self):
        """Tässä metodissa etsitään labyrintin ensimmäiseltä riviltä aloituskohta"""
        for i in range(0, self.x):
            if self.labyrintti[0][i] == ".":
                alkuy, alkux = 0, i
        
        return alkuy, alkux
    
    def onko_umpikuja(self, y, x):
        """Tässä metodissa tarkastetaan, onko kyseinen kohta umpikuja tarkastamalla, onko viereisestä neljästä solmusta kolme seinää.
        Jos on, niin muutetaan myös kyseinen kohta seinäksi"""

        laskuri = 0

        if self.labyrintti[y][x] == '.':

            if 0 <= y < self.y-1:
                if self.labyrintti[y+1][x] == '#':
                    laskuri += 1
                   
            if 0 < y <= self.y-1:
                if self.labyrintti[y-1][x] == '#':
                    laskuri += 1

            if 0 <= x < self.x-1:
                if self.labyrintti[y][x+1] == '#':
                    laskuri += 1

            if 0 < x <= self.x-1:
                if self.labyrintti[y][x-1] == '#':
                    laskuri += 1

            if laskuri == 3:
                self.labyrintti[y][x] = '#'
                return True
   
        return False
            

    def ratkaise(self):
        """Tämä metodi ratkaisee kaikki polut, joilla on mahdollista päästä ulos labyrintistä tutkimalla, onko kyseinen kohta umpikuja vai ei. Lopussa palautetaan
        labyrintti sellaisessa muodossa, jossa näkyy kaikki mahdolliset reitit ulos."""
        polku = True

        while polku:
            polku = False
            for korkeus in range(self.y):
                for leveys in range(self.x):
                    if self.onko_umpikuja(korkeus, leveys):
                        polku = True
        
        ratkaisu = self.labyrintti
        return ratkaisu
