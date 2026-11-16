import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(-5, 5), 0)
        self.assertEqual(add(-2, -4), -6)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(5, -5), 10)
        self.assertEqual(subtract(3, 3), 0)
    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(400, 2), 800)
        self.assertEqual(mul(5, 2566), 12830)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(3, 4), 1.3333, places=4)
        self.assertAlmostEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(6, 900000), 150000)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(8, 2), 3.0)
        self.assertAlmostEqual(logarithm(100, 10), 2.0)
        self.assertAlmostEqual(logarithm(27, 3), 3.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 0)
    ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(-4, 5)
        
    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(16, 10), 18.86796, places=5)

    def test_sqrt(self): # 3 assertions
    # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-6)
    # Test basic function
        self.assertAlmostEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(102), 10.0995, places=4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
