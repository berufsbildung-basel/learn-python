from list_processing import listproc
import unittest,string,random

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

class TestListProcessing(unittest.TestCase):
    r = randomword(random.randrange(1,1432))
    
    def test_flag_false(self):
        self.assertEqual(f"onetwothree{self.r}", listproc(['one','two','three',self.r], False))
        
    def test_flag_true(self):
        self.assertEqual(f"ONEtwoTHREE{self.r}", listproc(['one','two','three',self.r], True))

if __name__ == "__main__":
    unittest.main()