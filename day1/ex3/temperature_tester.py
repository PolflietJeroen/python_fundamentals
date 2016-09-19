import temperature
import unittest

class Test_temperature(unittest.TestCase):
    def test_K2C(self):
        a = 50
        b = temperature.convCtoK(a)
        self.assertEqual(4,temperature.convKtoC(b))
    def test_F2C(self):
        a = 50
        b = temperature.convCtoF(a)
        self.assertEqual(4,temperature.convFtoC(b))
    def test_K2F(self):
        a = 50
        b = temperature.convKtoC(a)
        c = temperature.convCtoF(b)
        self.assertEqual(4,temperature.convCtoK(b))
        self.assertEqual(4,temperature.convFtoC(c))



unittest.main()
        
