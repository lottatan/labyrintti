def tervetuloa():
    """Ohjelman aloitusnäkymä"""

    print("Labyrintin ratkaisusovellus")
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

    print("Labyrinttimme luomisessa valitaan arpomalla aloituskohta ja verrataan Trémaux- ja dead-end filling-algoritmeja, kumpi niistä ratkaisee labyrintin nopeammin!")

    return korkeus, leveys

