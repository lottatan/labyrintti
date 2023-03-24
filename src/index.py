import time
import luo_labyrintti
import ui

def main():
    korkeus, leveys = ui.tervetuloa()
    labyrintti = luo_labyrintti.Labyrintti(korkeus, leveys)
    labyrintti.luo_labyrintti()