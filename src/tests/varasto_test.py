import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_alkusaldo_alle_nolla(self):
         varasto = Varasto(10, -1)
         self.assertAlmostEqual(varasto.saldo, 0)

    def test_lisaa_negatiivinen(self):
         saldo = self.varasto.saldo
         self.varasto.lisaa_varastoon(-1)
         self.assertAlmostEqual(self.varasto.saldo, saldo)

    testit rikki

    def test_ota_negatiivinen_maara(self):
         self.varasto.lisaa_varastoon(5)
         saldo = self.varasto.saldo
         self.varasto.ota_varastosta(-5)
         self.assertAlmostEqual(self.varasto.saldo, saldo)

    def test_tostr_oikein(self):
         oikea = "saldo = 0, vielä tilaa 10"
         self.assertEqual(str(self.varasto), oikea)
         

    def test_alkutilavus_liian_pieni(self):
            varasto = Varasto(-1)
            self.assertAlmostEqual(varasto.tilavuus, 0)
    
    def test_lisaa_liikaa(self):
            self.varasto.lisaa_varastoon(100)
            self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)
    
    def test_ota_liikaa(self):
            self.varasto.ota_varastosta(1000)
            self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
