import unittest
from luo_labyrintti import Labyrintti

class TestLabyrintti(unittest.TestCase):
    def setup(self):
        self.labyrintti = Labyrintti(15, 15)

    def test_luo_labyrintti(self):
        self.labyrintti.luo_labyrintti()
        self.assertEqual(len(self.labyrintti), 15)
        self.assertEqual(len(self.labyrintti[0]), 15)

    def test_yksi_sisaanpaasy(self):
        laskuri = 0
        for i in (0, 15):
            if self.labyrintti[0][i] == ".":
                laskuri += 1
        
        self.assertEqual(laskuri, 1)
        
        
