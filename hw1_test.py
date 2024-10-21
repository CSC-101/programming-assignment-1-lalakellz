import data
import hw1
import unittest

from hw1 import add_prices, vowel_count


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel(self):
        input_str = "We Love Donuts"
        result = vowel_count((input_str))
        expected = 5
        self.assertEqual(result, expected)

    def test_vowel_2(self):
        input_str = "YOOOO"
        result = vowel_count(input_str)
        expected = 4
        self.assertEqual(result, expected)

    # Part 2


    # Part 3


    # Part 4
from hw1 import Price
class TestAddPrice(unittest.TestCase):

    def test_adding(self):
        price1 = Price(5,75)
        price2 = Price(3, 20)
        result = add_prices(price1, price2)
        expected = Price(8, 95)
        self.assertEqual(result, expected)


    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
