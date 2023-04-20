import unittest
import ui

class TestUi(unittest.TestCase):
    def setUp(self):
        self.pieni_numero = 4
        self.hyva_numero = 10

    def test_liian_pieni_numero(self):
        self.assertRaises(ValueError, ui.liian_pieni_luku, self.pieni_numero)
