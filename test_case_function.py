from function import*
import unittest

class Testfunction(unittest.TestCase):
    def test_functions(self):
        actual = function(str='May I share your email')
        expected = {"May I share your email": 'Student wants to know if can share'}
        self.assertEqual(actual, expected)

