import unittest
import piglatin

class Test_piglatin(unittest.TestCase):
    def test_gfdsdg2piglatin(self):
        AA = 'gfdsdg'
        BB = piglatin.to_piglatin(AA)
        CC = AA + '-ay'
        self.assertEqual(BB, CC)
    def test_egg2piglatin(self):
        aa = 'egg'
        bb = piglatin.to_piglatin(aa)
        cc = aa + '-ay'
        self.assertEqual(bb, cc)
    def test_Word2piglatin(self):
        a = 'Word'
        b = piglatin.to_piglatin(a)
        c = 'ord-W'+ 'ay'
        self.assertEqual(b, c)
    def test_frompiglatin(self):
        a = 'Word'
        b = piglatin.to_piglatin(a)
        c = piglatin.from_piglatin(b)
        self.assertEqual(a, c)



unittest.main()
