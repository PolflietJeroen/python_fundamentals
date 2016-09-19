import unittest

def isPrime(num):
    a = 2
    while num > a :
        if num%a==0 & a!=num:
            return False
        a += 1
    return True

def isArmstrong(num):
    
    digit = len(str(num))
    f = num
    s = 0
    while(f!=0):
        a = f % 10
        f = f / 10
        s = s + ( a ** digit)                                      
                             
    if(s == num):
        return True  
    else:
        return False

def isPerfectNumber(num):
    s = 0
    for i in range(1, num):
        if(num%i == 0):
            s = s + i
    if (s == num):
        return True
    else:
        return False

def isPalindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True


class Test_Number_tester(unittest.TestCase):
    def test_prime_number_tester(self):
        self.assertTrue(isPrime(5))
        self.assertFalse(isPrime(6))
        
    def test_armstrong_number_tester(self):
        self.assertTrue(isArmstrong(1634))
        self.assertFalse(isArmstrong(121))

    def test_perfect_number_tester(self):
        self.assertTrue(isPerfectNumber(6))
        self.assertFalse(isPerfectNumber(5))

    def test_palindrome_tester(self):
        self.assertTrue(isPalindrome('HellolleH'))
        self.assertFalse(isPalindrome('Hello'))
        self.assertTrue(isPalindrome('ABBA'))
        self.assertTrue(isPalindrome('SOS'))
        self.assertFalse(isPalindrome('SOs'))
        self.assertFalse(isPalindrome('Kayak'))
        self.assertFalse(isPalindrome('Satanoscillatemymetallicsonatas'))
'''

    def test_perfect_number_tester(self):
        self.assertTrue(isPerfectNumber(6))
        self.assertFalse(isPerfectNumber(5))
'''


unittest.main()

