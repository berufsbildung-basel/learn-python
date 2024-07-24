from using_sets import dedup
import unittest,string,random

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

class TestDedup(unittest.TestCase):
    
    def test_static(self):
        self.assertEqual(['one','three'],dedup('one',2,'three',True,'three'))

    def test_random_and_check_sorting(self):
        for i in range(1,4321) :
            r = randomword(random.randrange(12,322))
            self.assertEqual(sorted(['one',r]),dedup('one',2,r,r,True,r,-42))

if __name__ == '__main__':
    unittest.main()
