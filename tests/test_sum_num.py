import unittest
from main import *

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

        from unittest import TestCase
    
    def test_sum(self):

        # first store the expected result in a variable
        result_add = sum(3, 4)

        # check if the result is equal to expected result
        # here the result should be equal to 7.
        self.assertEquals(7, result_add)

    def test_subtract(self):

        # first store the expected result in a variable
        result_subtract = subtract(4, 3)

        # check if the result is equal to expected result
        # here the result should be equal to 7.
        self.assertEquals(1, result_subtract)

    def test_divide(self):

        # first store the expected result in a variable
        result_divide = divide(10, 2)

        # check if the result is equal to expected result
        # here the result should be equal to 7.
        self.assertEquals(5, result_divide)

    def test_multiply(self):

        # first store the expected result in a variable
        result_multiply = multiply(10, 2)

        # check if the result is equal to expected result
        # here the result should be equal to 7.
        self.assertEquals(20, result_multiply)

        

if __name__ == '__main__':
    unittest.main()