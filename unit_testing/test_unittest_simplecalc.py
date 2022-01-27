from unit_testing.simplecalc import SimpleCalc
import unittest

# Class that inherits from TestCase

class CalcTests(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalc()
        print("Setting Up")

    def tearDown(self):
        pass

    def test_add(self):
        actual = self.calc.add(2, 4)
        expected = 6
        self.assertEqual(actual, expected)

    def test_subtract(self):
        pass

    def test_multiply(self):
        actual = self.calc.multiply(0.4, -80.9)
        expected = -32.36
        self.assertAlmostEqual(actual, expected)

    def test_divide(self):
        pass