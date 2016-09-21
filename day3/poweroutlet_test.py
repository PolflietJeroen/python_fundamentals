'''
poweroutlet tester
'''
import unittest
import poweroutlet

class MockComm:
    '''
        create communication
    '''
    def __init__(self):
        '''
            comment
        '''
        self.data = []
    def write(self, writedata):
        '''
            comment
        '''
        self.data.append(writedata)

class TestPowerOutlet(unittest.TestCase):
    '''
        comment
    '''
    def setUp(self):
        '''
            comment
        '''
        self.comm = MockComm()
        self.outlet = poweroutlet.PowerOutlet(4, self.comm)
    def test_set_state_on(self):
        '''
            comment
        '''
        self.outlet.set_state(poweroutlet.PowerOn)
        self.assertEqual(len(self.comm.data), 1)
        self.assertEqual(self.comm.data[0], "%4=1;")
    def test_set_state_off(self):
        '''
            comment
        '''
        self.outlet.set_state(poweroutlet.PowerOff)
        self.assertEqual(len(self.comm.data), 1)
        self.assertEqual(self.comm.data[0], "%4=0;")

unittest.main()
