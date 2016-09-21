'''
comment
'''
import unittest
import piglatin

class TestPiglatin(unittest.TestCase):
    '''
    comment
    '''
    def test_gfdsdg2piglatin(self):
        '''
        comment
        '''
        aaa = 'gfdsdg'
        bbb = piglatin.to_piglatin(aaa)
        ccc = aaa + '-ay'
        self.assertEqual(bbb, ccc)
    def test_egg2piglatin(self):
        '''
        comment
        '''
        aaa = 'egg'
        bbb = piglatin.to_piglatin(aaa)
        ccc = aaa + '-ay'
        self.assertEqual(bbb, ccc)
    def test_word2piglatin(self):
        '''
        comment
        '''
        aaa = 'Word'
        bbb = piglatin.to_piglatin(aaa)
        ccc = 'ord-W'+ 'ay'
        self.assertEqual(bbb, ccc)
    def test_frompiglatin(self):
        '''
        comment
        '''
        aaa = 'Word'
        bbb = piglatin.to_piglatin(aaa)
        ccc = piglatin.from_piglatin(bbb)
        self.assertEqual(aaa, ccc)



unittest.main()
