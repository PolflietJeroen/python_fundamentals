'''
poweroutlet class
'''

POWERON = 1
POWEROFF = 0
"""
    #basic outlet
class PowerOutlet(object):
    '''
    define class
    '''
    def __init__(self, ident, comm):
        '''
        init object
        '''
        self.comm = comm
        self.ident = ident
    def set_state(self, outlet_state):
        '''
        define state
        '''
        self.comm.write("%{}={};".format(self.ident, outlet_state))
"""

class PowerOutletBank(object):
    '''
    Powerbanks
    '''
    def get_outlets(self):
        '''
            comment
        '''
        raise NotImplementedError

    def set_outlet_state(self, outlet_id, outlet_state):
        '''
            comment
        '''
        raise NotImplementedError


class PowerOutlet(object):
    '''
    define class
    '''
    def __init__(self, bank, identifier):
        '''
        init object
        '''
        self.bank = bank
        self.identifier = identifier
    def set_state(self, outlet_state):
        '''
        define state
        '''
        self.bank.set_outlet_state(self.identifier, outlet_state)
