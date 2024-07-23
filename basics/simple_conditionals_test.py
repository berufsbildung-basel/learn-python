from simple_conditionals import classify
import unittest

class TestClassifyNumber(unittest.TestCase):
    def test_all(self):
        self.assertEqual(classify(-10), "Negative")
        self.assertEqual(classify(3), "Small")
        self.assertEqual(classify(4), "Small")
        self.assertEqual(classify(5), "Small")
        self.assertEqual(classify(1), "Small")
        self.assertEqual(classify(0), "Zero")
        self.assertEqual(classify(10000), "Large")
        self.assertEqual(classify(5000), "Medium")
        self.assertEqual(classify(9362), "Medium")
        self.assertEqual(classify(9363), "Large")
        self.assertEqual(classify(9364), "Large")

if __name__ == "__main__":
    unittest.main()