import time
import luo_labyrintti
import tremaux
import dead_end_filling
import ui

def main():
    """Rakennetaan labyrintti"""
    korkeus, leveys = ui.tervetuloa()
    labyrintti = luo_labyrintti.Labyrintti(leveys, korkeus)
    laby = labyrintti.luo_labyrintti()

    ui.nayta_labyrintti(laby)

    """Ratkaistaan ensin trémauxin algoritmilla"""
    tremaux_aloitus = time.time_ns()
    tre = tremaux.Tremaux(laby)
    tremaux_ratkaisu = tre.ratkaise()
    tremaux_lopetus = time.time_ns()
    tre_kulutus = tremaux_lopetus - tremaux_aloitus

    """Sillä Trémauxin algoritmi antaa meille listana polun koordinaatit, muodostetaan samankokoinen labyrintti, joka on pelkästään seinää
    ja muutetaan saadut koordinaatit poluksi"""
    seina_labyrintti = [["#" for i in range(leveys)] for i in range(korkeus)]
    for (i, j) in tremaux_ratkaisu:
        seina_labyrintti[i][j] = "."

    ui.tre_ratkaisu(seina_labyrintti, tre_kulutus)

    """Ratkaistaan sitten dead-end filling algoritmilla"""
    dead_end_aloitus = time.time_ns()
    dead_end = dead_end_filling.DeadEndFilling(laby)
    dead_end_ratkaisu = dead_end.ratkaise()
    dead_end_lopetus = time.time_ns()

    dead_end_kulutus = dead_end_lopetus - dead_end_aloitus

    ui.dead_end_ratkaisu(dead_end_ratkaisu, dead_end_kulutus)
    
    """Tulostetaan lopputulos"""

    if dead_end_kulutus > tre_kulutus:
        ui.lopputulos("Trémaux")
    elif dead_end_kulutus < tre_kulutus:
        ui.lopputulos("Dead End Filling")
    elif dead_end_kulutus == tre_kulutus:
        ui.lopputulos("yhtä nopeasti")

if __name__ == "__main__":
    main()