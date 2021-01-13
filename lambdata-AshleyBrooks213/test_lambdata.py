"""Basic Unit test for Lambdata"""

import unittest
from example_module import FAVORITE_ANIMALS, FAVORITE_COLORS, add, increment


class ExampleTests(unittest.TestCase):
    """Making sure examples work as expected"""
    
    def test_add(self):
        """Testing that the add function works as expected"""
        num0 = 0
        num1 = 1
        self.assertEqual(add(num0, num1), 1)
        self.assertEqual(add(num1, num1), 2)



    def test_increment(self):
        """testing that the increment function works as expected"""
        x0 =0
        y0 = increment(x0)
        self.assertEqual(y0, 1)

        x1 = 100
        y1 = increment(x1)
        self.assertEqual(y1, 101)

        x2 = -1
        y2 = increment(x2)
        self.assertEqual(y2, 0)

        x3 = -1.5
        y3 = increment(x3)
        self.assertEqual(y3, -0.5)


if __name__ == "__main__":
    unittest.main()