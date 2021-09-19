import unittest

from main import compare

class MyTestCase(unittest.TestCase):
    def test_something0(self):
        self.assertEqual(compare(),False)
    def test_something1(self):
        self.assertEqual(compare(),False)
    def test_something2(self):
        self.assertEqual(compare(),False)
    def test_something3(self):
        self.assertEqual(compare(),False)
    def test_something4(self):
        self.assertEqual(compare(),False)

if __name__ == '__main__':
    unittest.main()
