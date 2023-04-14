from colorama import init
from colorama import Fore

def tervetuloa():
    """Ohjelman aloitusnäkymä"""

    print("Labyrintin ratkaisusovellus")
    print('\n')
    print("Ensimmäiseksi, valitaan labyrinttimme koko")

    try:
        korkeus = int(input("Valitse labyrintin korkeus (vähintään 5 ruutua): "))
        if korkeus < 5:
            raise ValueError
    except ValueError:
        print("Valitse suurempi luku")
    
    try:
        leveys = int(input("Valitse labyrintin leveys (vähintään 5 ruutua): "))
        if leveys < 5:
            raise ValueError
    except ValueError:
        print("Valitse suurempi luku")

    print('\n')
    print("Labyrinttimme luomisessa valitaan arpomalla aloituskohta ja verrataan Trémaux- ja dead-end filling-algoritmeja, kumpi niistä ratkaisee labyrintin nopeammin!")
    print('\n')

    return korkeus, leveys

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

def tre_ratkaisu(ratkaisu, aika):
    """Tämä funktio näyttää Trémauxin suorittaman ratkaisun, sekä ajan, joka kului labyrintin ratkaisemiseen"""

    print("Trémauxin algoritmin ratkaisu:")
    for i in range(0, len(ratkaisu)):
        for j in range(0, len(ratkaisu[0])):
            if ratkaisu[i][j] == ".":
                print(Fore.GREEN + str(ratkaisu[i][j]), end=" ")
            if ratkaisu[i][j] == "#":
                print(Fore.RED + str(ratkaisu[i][j]), end= " ")
        print('\n')

    print(Fore.WHITE + f"Trémauxin algoritmi ratkaisi labyrintin {aika} sekunnissa.")
    print('\n')

def dead_end_ratkaisu(ratkaisu, aika):
    """Tässä funktiossa näytetään, kuinka paljon aikaa kumpikin algoritmi käytti"""
    
    print("Dead End Filling -algoritmin ratkaisu:")
    for i in range(0, len(ratkaisu)):
        for j in range(0, len(ratkaisu[0])):
            if ratkaisu[i][j] == ".":
                print(Fore.GREEN + str(ratkaisu[i][j]), end=" ")
            if ratkaisu[i][j] == "#":
                print(Fore.RED + str(ratkaisu[i][j]), end= " ")
        print('\n')
    
    print(Fore.WHITE + f"Dead End Filling -algoritmilla meni labyrintin ratkaisemiseen {aika} sekuntia")
    print('\n')


def lopputulos(lopputulos):
    if lopputulos == "Dead End Filling":
        print("Dead End Filling -algoritmi ratkaisi labyrintin nopeammin!")
    elif lopputulos == "Trémaux":
        print("Trémauxin algoritmi ratkaisi labyrintin nopeammin!")
    elif lopputulos == "yhtä nopeasti":
        print("Molemmat algoritmit ratkaisivat labyrintin yhtä nopeasti!")