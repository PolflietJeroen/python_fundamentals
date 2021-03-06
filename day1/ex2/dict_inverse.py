import unittest

def dict_inverse(d):
#    print"lets do this"
    inv_d = {}
    for value in d.values():
            if value not in inv_d.keys(): #checking to be sure it hasn't been done.
                 inv_d[value] = []
                 for key in d.keys():
                     if d[key] == value:
                        if key not in inv_d[value]:    
                            inv_d[value].append(key)
   
#    print"got here"
    return inv_d

class Test_dict_inverse(unittest.TestCase):
    def test_dict_inverse(self):
        d = { "Oostende" : 8400,
              "Zandvoorde":8400,
              "Stene":8400,
              "Brugge":8000,
              "Gent":9000,
              }

        d2 = dict_inverse(d)
        self.assertEqual(len(d2), 3)
    
        self.assertEqual(len(d2[8400]),3)
        for city in ("Oostende","Zandvoorde","Stene"):
            self.assertTrue(city in d2[8400])

        self.assertEqual(d2[8000],["Brugge"])
        self.assertEqual(d2[9000],["Gent"])

unittest.main()

