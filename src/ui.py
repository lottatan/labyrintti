from colorama import Fore

def tervetuloa():
    """Ohjelman aloitusnäkymä"""

    print("Labyrintin ratkaisusovellus")
    print('\n')
    print("Ensimmäiseksi, valitaan labyrinttimme koko")

    
    while True:
        try:
            korkeus = int(input("Valitse labyrintin korkeus (kokonaisluku, joka on vähintään 5 ruutua ja enintään 60 ruutua): "))
            ei_ole_kokonaisluku(korkeus)
            liian_pieni_luku(korkeus)
            liian_iso_luku(korkeus)
            break
        except ValueError:
            print("Valitse eri luku")
            continue
    
    while True:
        try:
            leveys = int(input("Valitse labyrintin leveys (kokonaisluku, joka on vähintään 5 ruutua ja enintään 60 ruutua): "))
            ei_ole_kokonaisluku(leveys)
            liian_pieni_luku(leveys)
            liian_iso_luku(leveys)
            break
        except ValueError:
            print("Valitse eri luku")
            continue

    print('\n')
    print("Labyrinttimme luomisessa valitaan arpomalla aloituskohta ja verrataan Trémaux- ja dead-end filling-algoritmeja, kumpi niistä ratkaisee labyrintin nopeammin!")
    print('\n')

    return korkeus, leveys

def liian_pieni_luku(luku):
    if luku < 5:
        raise ValueError

def liian_iso_luku(luku):
    if luku > 60:
        raise ValueError
    
def ei_ole_kokonaisluku(luku):
    if isinstance(luku, int):
        pass
    else:
        raise ValueError


def nayta_labyrintti(labyrintti):
    """Tulostetaan luotu labyrintti"""

    print("Algoritmin luoma labyrintti annetulla korkeudella ja leveydellä:")

    for i in range(0, len(labyrintti)):
        for j in range(0, len(labyrintti[0])):
            if labyrintti[i][j] == ".":
                print(Fore.GREEN + str(labyrintti[i][j]), end=" ")
            if labyrintti[i][j] == "#":
                print(Fore.RED + str(labyrintti[i][j]), end= " ")
        print('\n')

    print(Fore.WHITE + "Seuraavaksi verrataan, kumpi algoritmi ratkaisee labyrintin nopeammin - Dead End Filling vai Trémaux?")
    print('\n')

def tre_ratkaisu(ratkaisu, aika, polku):
    """Tämä funktio näyttää Trémauxin suorittaman ratkaisun, sekä ajan, joka kului labyrintin ratkaisemiseen"""

    print("Trémauxin algoritmin ratkaisu:")
    for i in range(0, len(ratkaisu)):
        for j in range(0, len(ratkaisu[0])):
            if ratkaisu[i][j] == ".":
                print(Fore.GREEN + str(ratkaisu[i][j]), end=" ")
            if ratkaisu[i][j] == "#":
                print(Fore.RED + str(ratkaisu[i][j]), end= " ")
        print('\n')

    print(Fore.WHITE + f"Trémauxin algoritmi ratkaisi labyrintin {aika} nanosekunnissa. Algoritmi kulki labyrintissä tässä järjestyksessä: {polku}")
    print('\n')

def dead_end_ratkaisu(ratkaisu, aika, umpikujat):
    """Tässä funktiossa näytetään, kuinka paljon aikaa kumpikin algoritmi käytti"""
    
    print("Dead End Filling -algoritmin ratkaisu:")
    for i in range(0, len(ratkaisu)):
        for j in range(0, len(ratkaisu[0])):
            if ratkaisu[i][j] == ".":
                print(Fore.GREEN + str(ratkaisu[i][j]), end=" ")
            if ratkaisu[i][j] == "#":
                print(Fore.RED + str(ratkaisu[i][j]), end= " ")
        print('\n')
    
    print(Fore.WHITE + f"Dead End Filling -algoritmi ratkaisi labyrintin {aika} nanosekunnissa. Algoritmi täytti umpikujat tässä järjestyksessä: {umpikujat} ")
    print('\n')


def lopputulos(lopputulos):
    """Tämä funktio näyttää lopputuloksen"""

    if lopputulos == "Dead End Filling":
        print("Dead End Filling -algoritmi ratkaisi labyrintin nopeammin!")
    elif lopputulos == "Trémaux":
        print("Trémauxin algoritmi ratkaisi labyrintin nopeammin!")
    elif lopputulos == "yhtä nopeasti":
        print("Molemmat algoritmit ratkaisivat labyrintin yhtä nopeasti!")
    print('\n')
