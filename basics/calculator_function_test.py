from calculator_function import calc
import unittest, random

# Test the happy cases only, defensive stuff
# comes in the next exercise
class TestCalc(unittest.TestCase):
    a = random.randrange(-9999,9999)
    b = random.randrange(1,9999) # avoid div by 0

    def test_add(self):
        self.assertEqual(self.a + self.b, calc(self.a,'+',self.b))

    def test_sub(self):
        self.assertEqual(self.a - self.b, calc(self.a,'-',self.b))

    def test_mult(self):
        self.assertEqual(self.a * self.b, calc(self.a,'*',self.b))

    def test_div(self):
        self.assertEqual(self.a / self.b, calc(self.a,'/',self.b))

    def test_bad_op_raises_nothing(self):
        calc(1,'BAD',1)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calc(1,'/',0)

if __name__ == '__main__':
    unittest.main()
