import unittest

from common import genHtmlReport
from src.module.exercise.mathFunc import *


class TestMathFunc003(unittest.TestCase):
    """Test mathfunc.py"""
    @classmethod
    def setUpClass(cls):
        print("this setUpClass method only called once")

    @classmethod
    def tearDownClass(cls):
        print("this tearDownClass method only called once")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

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
        self.assertEqual(2,divide(4,2))

if __name__ == "__main__":
    # 设置testCase有顺序，按设定顺序执行
    # suit=unittest.TestSuite()
    # tests=[TestMathFunc003("test_add"),TestMathFunc003("test_minus"),
    #        TestMathFunc003("test_multi"),TestMathFunc003("test_divide")]
    # suit.addTests(tests)
    # unittest.TextTestRunner(verbosity=2).run(suit)

    suit1=unittest.TestSuite()
    suit1.addTest(TestMathFunc003("test_add"))
    suit1.addTest(TestMathFunc003("test_minus"))
    suit1.addTest(TestMathFunc003("test_multi"))
    suit1.addTest(TestMathFunc003("test_divide"))
    genHtmlReport.generateHtmlReport(suit=suit1,
                                     title="TestMathFunc003接口测试报告",
                                     description="接口执行结果详情",
                                     verbosity=2,
                                     casefile="testMathFunc003_")

