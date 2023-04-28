def aloituskohta(labyrintti):
    """Tässä metodissa etsitään labyrintin ensimmäiseltä riviltä aloituskohta"""
    for i in range(0, len(labyrintti[0])):
        if labyrintti[0][i] == ".":
            alkuy, alkux = 0, i
        
    return alkuy, alkux
    
    
def onko_umpikuja(labyrintti, korkeus, leveys, y, x):
    """Tässä metodissa tutkitaan, onko kyseinen kohta umpikuja. Annetut parametrit ovat labyrintti sillä ratkaisuhetkellä, sen hetkinen koordinaatti ja labyrintin
    korkeus ja leveys"""
    laskuri = 0
    
    if labyrintti[korkeus][leveys] == '.':

        if 0 <= korkeus < y-1:
            if labyrintti[korkeus+1][leveys] == '#':
                laskuri += 1
                   
        if 0 < korkeus <= y-1:
            if labyrintti[korkeus-1][leveys] == '#':
                laskuri += 1

        if 0 <= leveys < x-1:
            if labyrintti[korkeus][leveys+1] == '#':
                laskuri += 1

        if 0 < leveys <= x-1:
            if labyrintti[korkeus][leveys-1] == '#':
                laskuri += 1

        if laskuri == 3:
            labyrintti[korkeus][leveys] = '#'
            return True
   
    return False



def ratkaise(labyrintti):
    """Tämä metodi ratkaisee labyrintin dead-end filling metodilla. Labyrintissä kuljetaan askel kerrallaan ja tutkitaan, onko kyseinen kohta umpikuja."""
    y = len(labyrintti)
    x = len(labyrintti[0])

    polku = True

    while polku:
        polku = False
        for korkeus in range(y):
            for leveys in range(x):
                if onko_umpikuja(labyrintti, korkeus, leveys, y, x):
                    polku = True
    
    ratkaisu = labyrintti
    return ratkaisu