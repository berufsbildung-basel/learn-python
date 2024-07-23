from hello_python import hello
import unittest

class TestHello(unittest.TestCase):

    def test_hello(self):
        self.assertEqual('Hello, Python!', hello())

if __name__ == '__main__':
    unittest.main()
