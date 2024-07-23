from whats_your_name import wyn
import unittest, random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

class TestWyn(unittest.TestCase):

    def test_static(self):
        self.assertEqual('Hello, Bob!', wyn('Bob'))

    def test_random(self):
        rw = randomword(10)
        self.assertEqual('Hello, ' + rw + '!', wyn(rw))

if __name__ == '__main__':
    unittest.main()