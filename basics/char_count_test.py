from char_count import ccount
import unittest, random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


class TestCcount(unittest.TestCase):

    def test_static(self):
        self.assertEqual('Yo, cats:8', ccount('Yo, cats'))

    def test_random(self):
        testlen = random.randrange(12,99999)
        rw = randomword(testlen)
        self.assertEqual(rw + ':' + str(testlen), ccount(rw))

if __name__ == '__main__':
    unittest.main()
