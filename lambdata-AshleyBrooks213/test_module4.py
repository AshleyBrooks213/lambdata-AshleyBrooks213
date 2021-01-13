import unittest
import pandas as pd
import numpy as np 
from example_module import FAVORITE_ANIMALS, FAVORITE_COLORS, add, increment


class ExampleTests(unittest.TestCase):
    """Making sure examples work as expected"""


    def test_add(self):
        """Testing that add function works as expected"""
        num1 = 100
        num2 = 200
        self.assertEqual(add(num1, num2), 300)
        self.assertEqual(add(num2, num2), 400)


    def test_increment(self):
        """testing that increment function works as expected"""
        x0 = 100
        y0 = increment(x0)
        self.assertEqual(y0, 101)

        x1 = 110
        y1 = increment(x1)
        self.assertEqual(y1, 111)


if __name__ == "__main__":
    unittest.main()