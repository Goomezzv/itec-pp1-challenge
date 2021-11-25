import unittest
from numtolet import numtolet

class TestNumberToLetter(unittest.TestCase):

    def test_exceed(self):
        numero = 10000000000
        self.assertRaises(OverflowError, numtolet, numero)

    def test_unidades(self):
        numero = 5
        self.assertEqual(numtolet(numero), 'cinco')
        numero = 9
        self.assertEqual(numtolet(numero), 'nueve')
        numero = 0
        self.assertEqual(numtolet(numero), 'cero')

    def test_decena_diez(self):
        numero = 13
        self.assertEqual(numtolet(numero), 'trece')
        numero = 10
        self.assertEqual(numtolet(numero), 'diez')
        numero = 17
        self.assertEqual(numtolet(numero), 'diecisiete')

    def test_decena_veinte(self):
        numero = 24
        self.assertEqual(numtolet(numero), 'veinticuatro')
        numero = 29
        self.assertEqual(numtolet(numero), 'veintinueve')
        numero = 22
        self.assertEqual(numtolet(numero), 'veintidos')

    def test_centenas(self):
        numero = 151
        self.assertEqual(numtolet(numero), 'ciento cincuenta y uno')
        numero = 650
        self.assertEqual(numtolet(numero), 'seiscientos cincuenta')
        numero = 217
        self.assertEqual(numtolet(numero), 'doscientos diecisiete')

    def test_miles(self):
        numero = 1840
        self.assertEqual(numtolet(numero), 'mil ochocientos cuarenta')
        numero = 4221
        self.assertEqual(numtolet(numero), 'cuatro mil doscientos veintiuno')

    def test_millones(self):
        numero = 10504000
        self.assertEqual(numtolet(numero), 'diez millones quinientos cuatro mil')
        numero = 4000000
        self.assertEqual(numtolet(numero), 'cuatro millones')

    def test_decimales(self):
        numero = 1.61
        self.assertEqual(numtolet(numero), 'uno punto sesenta y uno')
        numero = 5.50
        self.assertEqual(numtolet(numero), 'cinco punto cincuenta')

    def test_negativo(self):
        numero = -1
        self.assertEqual(numtolet(numero), 'menos uno')


if __name__ == '__main__':
    unittest.main()