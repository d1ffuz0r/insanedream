__author__ = 'd1ffuz0r'
import unittest
from modules import speak

class MyTestCase(unittest.TestCase):

    def test_something(self):
        _speak = speak.Speak()
        self.assertIsNotNone(_speak.get())

if __name__ == '__main__':
    unittest.main()
