import unittest
from main import *

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

        from unittest import TestCase
    
    def test_sum(self):

        result_add = sum(3, 4)
        self.assertEquals(7, result_add)

    def test_subtract(self):

        result_subtract = subtract(4, 3)
        self.assertEquals(1, result_subtract)

    def test_divide(self):

        result_divide = divide(10, 2)
        self.assertEquals(5, result_divide)

    def test_multiply(self):

        result_multiply = multiply(10, 2)
        self.assertEquals(20, result_multiply)

if __name__ == '__main__':
    unittest.main()