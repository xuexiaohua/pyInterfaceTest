import unittest
from sourceCode.mathFunc import *

class TestMathFunc001(unittest.TestCase):
    """Test mathfunc.py"""
    def test_add(self):
        """Test method add(a,b)"""
        self.assertEqual(3,add(1,2))
    def test_minus(self):
        """Test Method minus(a,b)"""
        self.assertEqual(1,minus(3,2))
    def test_multi(self):
        """Test Method multi(a,b)"""
        self.assertEqual(2,multi(1,2))
    def test_divide(self):
        """Test Method divide(a,b)"""
        self.assertEqual(2,divide(5,2))

if __name__ == "__main__":
    unittest.main()