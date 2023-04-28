import random

class Labyrintti:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.aloitus_y = 0
        self.aloitus_x = 0

        self.labyrintti = []
        self.seinat = []


    def alusta_labyrintti(self):
        """Ensin tehdään "tyhjä" labyrintti"""

        for i in range(0, self.y):
            self.labyrintti.append([])
            for j in range(0, self.x):
                self.labyrintti[i].append("X")

    def aloitus_kohta(self):
        """Valitaan satunnainen aloituskohta labyrintille ja varmistetaan, että se ei ole labyrintin reunassa"""
        self.aloitus_x = int(random.randint(1, self.x-2))
        self.aloitus_y = 1

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

        self.labyrintti[self.aloitus_y][self.aloitus_x] = "."
        
        self.seinat.append([self.aloitus_y-1, self.aloitus_x])
        self.seinat.append([self.aloitus_y, self.aloitus_x-1])
        self.seinat.append([self.aloitus_y, self.aloitus_x+1])
        self.seinat.append([self.aloitus_y+1, self.aloitus_x])

        self.labyrintti[self.aloitus_y-1][self.aloitus_x] = "#"
        self.labyrintti[self.aloitus_y][self.aloitus_x-1] = "#"
        self.labyrintti[self.aloitus_y][self.aloitus_x+1] = "#"
        self.labyrintti[self.aloitus_y+1][self.aloitus_x] = "#"

        while self.seinat:
            """Luodaan labyrintti tarkastamalla seinä kerrallaan"""
            random_seina = self.seinat[int(random.random()*len(self.seinat))-1]

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
                            if [random_seina[0]-1, random_seina[1]] not in self.seinat:
                                self.seinat.append([random_seina[0]-1, random_seina[1]])

                        """Alin piste"""
                        if random_seina[0] != self.y-1:
                            if self.labyrintti[random_seina[0]+1][random_seina[1]] != ".":
                                self.labyrintti[random_seina[0]+1][random_seina[1]] = "#"
                            
                            if [random_seina[0]+1, random_seina[1]] not in self.seinat:
                                self.seinat.append([random_seina[0]+1, random_seina[1]])

                        """Vasemmanpuoleisin piste"""
                        if random_seina[1] != 0:
                            if self.labyrintti[random_seina[0]][random_seina[1]-1] != ".":
                                self.labyrintti[random_seina[0]][random_seina[1]-1] = "#"

                            if [random_seina[0], random_seina[1]-1] not in self.seinat:
                                self.seinat.append([random_seina[0], random_seina[1]-1])
                                
                    for seina in self.seinat:
                        if seina[0] == random_seina[0] and seina[1] == random_seina[1]:
                            self.seinat.remove(seina)

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
                            if [random_seina[0]-1, random_seina[1]] not in self.seinat:
                                self.seinat.append([random_seina[0]-1, random_seina[1]])
                        
                        """Vasemmanpuoleisin piste"""
                        if random_seina[1] != 0:
                            if self.labyrintti[random_seina[0]][random_seina[1]-1] != ".":
                                self.labyrintti[random_seina[0]][random_seina[1]-1] = "#"
                            if [random_seina[0], random_seina[1]-1] not in self.seinat:
                                self.seinat.append([random_seina[0], random_seina[1]-1])

                        """Oikeanpuoleisin piste"""
                        if random_seina[1] != self.x-1:
                            if self.labyrintti[random_seina[0]][random_seina[1]+1] != ".":
                                self.labyrintti[random_seina[0]][random_seina[1]+1] = "#"
                            if [random_seina[0], random_seina[1]+1] not in self.seinat:
                                self.seinat.append([random_seina[0], random_seina[1]+1])
                
                    for seina in self.seinat:
                        if seina[0] == random_seina[0] and seina[1] == random_seina[1]:
                            self.seinat.remove(seina)
                        
                    continue

            """Tarkastetaan, onko kyseessä alin seinä"""
            if random_seina[0] != self.y-1:
                if self.labyrintti[random_seina[0]+1][random_seina[1]] == "X" and self.labyrintti[random_seina[0]-1][random_seina[1]] == ".":
                    polut = self.viereiset_polut(random_seina)

                    if polut < 2:
                        self.labyrintti[random_seina[0]][random_seina[1]] = "."

                        """Ylin piste"""
                        if random_seina[0] != self.y-1:
                            if self.labyrintti[random_seina[0]+1][random_seina[1]] != ".":
                                self.labyrintti[random_seina[0]+1][random_seina[1]] = "#"
                            if [random_seina[0]+1, random_seina[1]] not in self.seinat:
                                self.seinat.append([random_seina[0]+1, random_seina[1]])
                                
                        """Vasemmanpuoleisin piste"""
                        if random_seina[1] != 0:
                            if self.labyrintti[random_seina[0]][random_seina[1]-1] != ".":
                                self.labyrintti[random_seina[0]][random_seina[1]-1] = "#"
                            if [random_seina[0], random_seina[1]-1] not in self.seinat:
                                self.seinat.append([random_seina[0], random_seina[1]-1])

                        """Oikeanpuoleisin piste"""        
                        if random_seina[1] != self.x-1:
                            if self.labyrintti[random_seina[0]][random_seina[1]+1] != ".":
                                self.labyrintti[random_seina[0]][random_seina[1]+1] = "#"
                            if [random_seina[0], random_seina[1]+1] not in self.seinat:
                                self.seinat.append([random_seina[0], random_seina[1]+1])
                    
                    for seina in self.seinat:
                        if seina[0] == random_seina[0] and seina[1] == random_seina[1]:
                            self.seinat.remove(seina)
                        
                    continue

            """Tarkistetaan, onko kyseessä oikeanpuoleisin seinä"""
            if random_seina[1] != self.x-1:
                if self.labyrintti[random_seina[0]][random_seina[1]+1] == "X" and self.labyrintti[random_seina[0]][random_seina[1]-1] == ".":
                    polut = self.viereiset_polut(random_seina)

                    if polut < 2:
                        self.labyrintti[random_seina[0]][random_seina[1]] = "."

                        """Oikeanpuoleisin piste"""
                        if random_seina[1] != self.x-1:
                            if self.labyrintti[random_seina[0]][random_seina[1]+1] != ".":
                                self.labyrintti[random_seina[0]][random_seina[1]+1] = "#"
                            if [random_seina[0], random_seina[1]+1] not in self.seinat:
                                self.seinat.append([random_seina[0], random_seina[1]+1])
                        
                        """Ylin piste"""
                        if random_seina[0] != self.y-1:
                            if self.labyrintti[random_seina[0]+1][random_seina[1]] != ".":
                                self.labyrintti[random_seina[0]+1][random_seina[1]] = "#"
                            if [random_seina[0]+1, random_seina[1]] not in self.seinat:
                                self.seinat.append([random_seina[0]+1, random_seina[1]])

                        """Vasemmanpuoleisin piste"""
                        if random_seina[0] != 0:
                            if self.labyrintti[random_seina[0]-1][random_seina[1]] != ".":
                                self.labyrintti[random_seina[0]-1][random_seina[1]] = "#"
                            if [random_seina[0]-1, random_seina[1]] not in self.seinat:
                                self.seinat.append([random_seina[0]-1, random_seina[1]])

                    for seina in self.seinat:
                        if seina[0] == random_seina[0] and seina[1] == random_seina[1]:
                            self.seinat.remove(seina)
                    
                    continue
            
            for seina in self.seinat:
                if seina[0] == random_seina[0] and seina[1] == random_seina[1]:
                            self.seinat.remove(seina)

        
        """Merkataan mahdolliset jäljelle jääneet vierailemattomat osat seinäksi"""
        for i in range(0, self.y):
            for j in range(0, self.x):
                if self.labyrintti[i][j] == "X":
                    self.labyrintti[i][j] = "#"
        
        ulospaasyt = []
        """Tehdään labyrinttiin yksi ulospääsykohta"""
        for i in range(0, self.x):
            if self.labyrintti[self.y-2][i] == ".":
                ulospaasyt.append((self.y-1, i))
        
        ulospaasy = random.choice(ulospaasyt)

        self.labyrintti[ulospaasy[0]][ulospaasy[1]] = "."

        """Tehdään labyrinttiin yksi sisäänpääsykohta"""
        self.labyrintti[self.aloitus_y-1][self.aloitus_x] = "."
        
        return self.labyrintti
