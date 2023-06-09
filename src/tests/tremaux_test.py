import unittest
from tremaux import Tremaux

labyrintti = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#'],
        ['#', '.', '#', '.', '#', '#', '.', '#', '.', '.', '#', '#', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '.', '.', '.', '#', '#', '.', '.', '#', '#'],
        ['#', '.', '#', '.', '#', '#', '#', '#', '.', '#', '.', '.', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '.', '#', '.', '#', '#', '.', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '.', '#', '#', '.', '#', '.', '#', '.', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '.', '#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '#', '#', '.', '#', '#', '.', '#', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '.', '#', '.', '.', '#', '#', '#', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '#', '#', '.', '#', '#', '.', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '#', '#', '.', '#', '#', '.', '.', '.', '#']
        ]

class TestTremaux(unittest.TestCase):
    def setUp(self):
        self.labyrintti = Tremaux(labyrintti)

    def test_loytaa_aloituskohdan(self):
        aloitus = self.labyrintti.aloituskohta()

        aloituskorkeus = aloitus[0]
        aloitusleveys = aloitus[1]

        self.assertEqual(aloituskorkeus, 0)
        self.assertEqual(aloitusleveys, 12)

    def test_ratkaise(self):
        ratkaisu, polku = self.labyrintti.ratkaise()

        self.assertNotEqual(ratkaisu, "Ei ratkaisua")
        self.assertNotEqual(0, len(polku))