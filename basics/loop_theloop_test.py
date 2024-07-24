from loop_theloop import loop
import unittest

class TestLoop(unittest.TestCase):
    
    def test_3_args(self):
        self.assertEqual(18, loop(2,13,4))
        self.assertEqual(910, loop(-2,143,12))
        
    def test_2_args(self):
        self.assertEqual(9, loop(2,5))
        self.assertEqual(122843, loop(-220,543))
        
if __name__ == "__main__":
    unittest.main()