import unittest

from common import genHtmlReport
from src.module.exercise.mathFunc import *


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
    s=unittest.TestSuite()
    s.addTest(TestMathFunc001("test_add"))
    s.addTest(TestMathFunc001("test_minus"))
    s.addTest(TestMathFunc001("test_multi"))
    s.addTest(TestMathFunc001("test_divide"))
    genHtmlReport.generateHtmlReport(suit=s,
                                     title="TestMathFunc001接口测试报告",
                                     description="接口测试结果详情",
                                     verbosity=2,
                                     casefile="testMathFunc001_")


