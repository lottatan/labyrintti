import time
import luo_labyrintti
import ui

def main():
    """Rakennetaan labyrintti"""
    korkeus, leveys = ui.tervetuloa()
    labyrintti = luo_labyrintti.Labyrintti(leveys, korkeus)
    labyrintti.luo_labyrintti()

    """Ratkaistaan ensin trémauxin algoritmilla"""
    tremaux_aloitus = time.time()
    # tulevaa koodia
    tremaux_lopetus = time.time()

    """Ratkaistaan sitten dead-end fillinf algoritmilla"""
    dead_end_aloitus = time.time()
    # tulevaa koodia
    dead_end_lopetus = time.time()

    
