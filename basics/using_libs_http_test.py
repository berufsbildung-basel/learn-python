from using_libs_http import get_content
import unittest, random, string

class TestGetContent(unittest.TestCase):

    def test_asf(self):
        self.assertTrue(get_content('apache.org','ASF'))
        self.assertFalse(get_content('apache.org','something_that_is_not_there, really'))
        
if __name__ == '__main__':
    unittest.main()
