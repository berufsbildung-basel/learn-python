import simple_module as smod
import unittest,random

class TestSimpleModule(unittest.TestCase):
    
    def test_set_get(self):
        r = random.randrange(-9999,9999)
        smod.clear()
        self.assertEqual(-1, smod.get())
        smod.set(r)        
        self.assertEqual(r, smod.get())
        
    def test_clear(self):
        r = random.randrange(-9999,9999)
        smod.set(r)        
        self.assertEqual(r, smod.get())
        smod.clear()
        self.assertEqual(-1, smod.get())
        
    def test_count(self):
        smod.clear()
        expected = random.randrange(1,100)
        for i in range(0,expected+1):
            smod.set(i)
        self.assertEqual(expected, smod.count())
        
if __name__ == "__main__":
    unittest.main()