import random

class Labyrintti:
    def __init__(self, leveys, korkeus):
        self.leveys = leveys
        self.korkeus = korkeus
        self.labyrintti = []

        self.aloitus_korkeus = 0
        self.aloitus_leveys = 0

    def alusta_labyrintti(self):
        """Ensin tehdään "tyhjä" labyrintti"""

        for i in range(0, self.korkeus):
            self.labyrintti.append([])
            for j in range(0, self.leveys):
                self.labyrintti[i].append("X")

    def aloitus_kohta(self):
        """Valitaan satunnainen aloituskohta labyrintille ja varmistetaan, että se ei ole labyrintin reunassa"""
        self.aloitus_leveys = int(random.random()*self.leveys)
        self.aloitus_korkeus = int(random.random()*self.korkeus)

        if self.aloitus_korkeus == 0:
            self.aloitus_korkeus += 1
        if self.aloitus_korkeus == self.korkeus-1:
            self.aloitus_korkeus -= 1

        if self.aloitus_leveys == 0:
            self.aloitus_leveys += 1
        if self.aloitus_leveys == self.leveys-1:
            self.aloitus_leveys -= 1

    def viereiset_polut(self, random_seina):
        """Lasketaan viereisten polkujen määrä"""
        polut = 0
        if self.labyrintti[random_seina[0]-1][random_seina[1]] == ".":
            polut += 1
        if self.labyrintti[random_seina[0]+1][random_seina[1]] == ".":
            polut += 1
        if self.labyrintti[random_seina[0]][random_seina[1]-1] == ".":
            polut +=1
        if self.labyrintti[random_seina[0]][random_seina[1]+1] == ".":
            polut += 1

        return polut
    
    def luo_labyrintti(self):
        self.alusta_labyrintti()
        self.aloitus_kohta()

        self.labyrintti[self.aloitus_korkeus][self.aloitus_leveys] = "."
        seinat = []
        seinat.append([self.aloitus_korkeus-1, self.aloitus_leveys])
        seinat.append([self.aloitus_korkeus, self.aloitus_leveys-1])
        seinat.append([self.aloitus_korkeus, self.aloitus_leveys+1])
        seinat.append([self.aloitus_korkeus+1, self.aloitus_leveys])

        self.labyrintti[self.aloitus_korkeus-1][self.aloitus_leveys] = "#"
        self.labyrintti[self.aloitus_korkeus][self.aloitus_leveys-1] = "#"
        self.labyrintti[self.aloitus_korkeus][self.aloitus_leveys+1] = "#"
        self.labyrintti[self.aloitus_korkeus+1][self.aloitus_leveys] = "#"

        while seinat:
            """Luodaan labyrintti tarkastamalla seinä kerrallaan"""
            random_seina = seinat[int(random.random()*len(seinat))-1]

            """Tarkastetaan, onko kyseessä vasemmanpuoleisin seinä"""
            if random_seina[1] != 0:
                if self.labyrintti[random_seina[0]][random_seina[1]-1] == "X" and self.labyrintti[random_seina[0]][random_seina[1]+1] == "." :
                    polut = self.viereiset_polut(random_seina)

                    """Jatketaan polkua ja tehdään uudet merkinnät labyrinttiin"""
                    if polut < 2:
                        self.labyrintti[random_seina[0]][random_seina[1]] = "."
                        
                        """Ylin piste"""
                        if random_seina[0] != 0:
                            if self.labyrintti[random_seina[0]-1][random_seina[1]] != ".":
                                self.labyrintti[random_seina[0]-1][random_seina[1]] = "#"
                            if [random_seina[0]-1, random_seina[1]] not in seinat:
                                seinat.append([random_seina[0]-1, random_seina[1]])

                        """Alin piste"""
                        if random_seina[0] != self.korkeus-1:
                            if self.labyrintti[random_seina[0]+1][random_seina[1]] != ".":
                                self.labyrintti[random_seina[0]+1][random_seina[1]] = "#"
                            
                            if [random_seina[0]+1, random_seina[1]] not in seinat:
                                seinat.append([random_seina[0]+1, random_seina[1]])

                        """Vasemmanpuoleisin piste"""
                        if random_seina[1] != 0:
                            if self.labyrintti[random_seina[0]][random_seina[1]-1] != ".":
                                self.labyrintti[random_seina[0]][random_seina[1]-1] = "#"

                            if [random_seina[0], random_seina[1]-1] not in seinat:
                                seinat.append([random_seina[0], random_seina[1]-1])
                                
                    for seina in seinat:
                        if seina[0] == random_seina[0] and seina[1] == random_seina[1]:
                            seinat.remove(seina)

                    continue
            
            """Tarkastetaan, onko kyseessä ylin seinä"""
            if random_seina[0] != 0:

                if self.labyrintti[random_seina[0]-1][random_seina[1]] == "X" and self.labyrintti[random_seina[0]+1][random_seina[1]] == ".":
                    polut = self.viereiset_polut(random_seina)

                    """Jatketaan polkua ja tehdään uudet merkinnät labyrinttiin"""
                    if polut < 2:
                        self.labyrintti[random_seina[0]][random_seina[1]] = "."
                        
                        """Ylin piste"""
                        if random_seina[0] != 0:
                            if self.labyrintti[random_seina[0]-1][random_seina[1]] != ".":
                                self.labyrintti[random_seina[0]-1][random_seina[1]] = "#"
                            if [random_seina[0]-1, random_seina[1]] not in seinat:
                                seinat.append([random_seina[0]-1, random_seina[1]])
                        
                        """Vasemmanpuoleisin piste"""
                        if random_seina[1] != 0:
                            if self.labyrintti[random_seina[0]][random_seina[1]-1] != ".":
                                self.labyrintti[random_seina[0]][random_seina[1]-1] = "#"
                            if [random_seina[0], random_seina[1]-1] not in seinat:
                                seinat.append([random_seina[0], random_seina[1]-1])

                        """Oikeanpuoleisin piste"""
                        if random_seina[1] != self.leveys-1:
                            if self.labyrintti[random_seina[0]][random_seina[1]+1] != ".":
                                self.labyrintti[random_seina[0]][random_seina[1]+1] = "#"
                            if [random_seina[0], random_seina[1]+1] not in seinat:
                                seinat.append([random_seina[0], random_seina[1]+1])
                
                    for seina in seinat:
                        if seina[0] == random_seina[0] and seina[1] == random_seina[1]:
                            seinat.remove(seina)
                        
                    continue

            """Tarkastetaan, onko kyseessä alin seinä"""
            if random_seina[0] != self.korkeus-1:
                if self.labyrintti[random_seina[0]+1][random_seina[1]] == "X" and self.labyrintti[random_seina[0]-1][random_seina[1]] == ".":
                    polut = self.viereiset_polut(random_seina)

                    if polut < 2:
                        self.labyrintti[random_seina[0]][random_seina[1]] = "."

                        """Ylin piste"""
                        if random_seina[0] != self.korkeus-1:
                            if self.labyrintti[random_seina[0]+1][random_seina[1]] != ".":
                                self.labyrintti[random_seina[0]+1][random_seina[1]] = "#"
                            if [random_seina[0]+1, random_seina[1]] not in seinat:
                                seinat.append([random_seina[0]+1, random_seina[1]])
                                
                        """Vasemmanpuoleisin piste"""
                        if random_seina[1] != 0:
                            if self.labyrintti[random_seina[0]][random_seina[1]-1] != ".":
                                self.labyrintti[random_seina[0]][random_seina[1]-1] = "#"
                            if [random_seina[0], random_seina[1]-1] not in seinat:
                                seinat.append([random_seina[0], random_seina[1]-1])

                        """Oikeanpuoleisin piste"""        
                        if random_seina[1] != self.leveys-1:
                            if self.labyrintti[random_seina[0]][random_seina[1]+1] != ".":
                                self.labyrintti[random_seina[0]][random_seina[1]+1] = "#"
                            if [random_seina[0], random_seina[1]+1] not in seinat:
                                seinat.append([random_seina[0], random_seina[1]+1])
                    
                    for seina in seinat:
                        if seina[0] == random_seina[0] and seina[1] == random_seina[1]:
                            seinat.remove(seina)
                        
                    continue

            """Tarkistetaan, onko kyseessä oikeanpuoleisin seinä"""
            if random_seina[1] != self.leveys-1:
                if self.labyrintti[random_seina[0]][random_seina[1]+1] == "X" and self.labyrintti[random_seina[0]][random_seina[1]-1] == ".":
                    polut = self.viereiset_polut(random_seina)

                    if polut < 2:
                        self.labyrintti[random_seina[0]][random_seina[1]] = "."

                        """Oikeanpuoleisin piste"""
                        if random_seina[1] != self.leveys-1:
                            if self.labyrintti[random_seina[0]][random_seina[1]+1] != ".":
                                self.labyrintti[random_seina[0]][random_seina[1]+1] = "#"
                            if [random_seina[0], random_seina[1]+1] not in seinat:
                                seinat.append([random_seina[0], random_seina[1]+1])
                        
                        """Ylin piste"""
                        if random_seina[0] != self.korkeus-1:
                            if self.labyrintti[random_seina[0]+1][random_seina[1]] != ".":
                                self.labyrintti[random_seina[0]+1][random_seina[1]] = "#"
                            if [random_seina[0]+1, random_seina[1]] not in seinat:
                                seinat.append([random_seina[0]+1, random_seina[1]])

                        """Vasemmanpuoleisin piste"""
                        if random_seina[0] != 0:
                            if self.labyrintti[random_seina[0]-1][random_seina[1]] != ".":
                                self.labyrintti[random_seina[0]-1][random_seina[1]] = "#"
                            if [random_seina[0]-1, random_seina[1]] not in seinat:
                                seinat.append([random_seina[0]-1, random_seina[1]])

                    for seina in seinat:
                        if seina[0] == random_seina[0] and seina[1] == random_seina[1]:
                            seinat.remove(seina)
                    
                    continue
            
            for seina in seinat:
                if seina[0] == random_seina[0] and seina[1] == random_seina[1]:
                            seinat.remove(seina)
        
        """Merkataan mahdolliset jäljelle jääneet vierailemattomat osat seinäksi"""
        for i in range(0, self.korkeus):
            for j in range(0, self.leveys):
                if self.labyrintti[i][j] == "X":
                    self.labyrintti[i][j] = "#"
        
        for i in range(0, self.korkeus):
            print(self.labyrintti[i])

if __name__ == "__main__":
    k = 18
    l = 18
    laby = Labyrintti(l, k)
    laby.luo_labyrintti()