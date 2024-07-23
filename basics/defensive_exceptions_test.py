from defensive_exceptions import divide
import unittest,random

class TestDefensiveExceptions(unittest.TestCase):
    n = random.randrange(1,9999)
    neg = random.randrange(-9999,-1)
    
    def test_happy(self):
        self.assertEqual(12, divide(24,2))
        self.assertEqual(self.n/2, divide(self.n,2))
        self.assertEqual(self.n/3, divide(self.n,3))

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1,0)

    def test_invalid_second(self):
        with self.assertRaises(ValueError,msg='Expecting ValueError with a negative second argument'):
            divide(self.n, self.neg)
        
    def test_both_equal(self):
        with self.assertRaises(ValueError,msg='Expecting ValueError with two equal arguments') as context:
            divide(self.n, self.n)
            
        expected = 'Arguments cannot be equal'
        actual = str(context.exception)
        self.assertTrue(expected in actual,msg='Invalid or empty ValueError message: [' + actual + ']')
        
if __name__ == "__main__":
    unittest.main()