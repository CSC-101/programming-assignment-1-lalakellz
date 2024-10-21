import data
import hw1
import unittest

from hw1 import add_prices, vowel_count, short_lists, ascending_pairs


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
    def test_list(self):
        lists = [[1, 2], [3, 4, 5], [6], [7, 8]]
        result = short_lists(lists)
        expected = [[1, 2], [7, 8]]
        self.assertEqual(result, expected)

    def test_list_2(self):
        lists = [[1, 2], [3, 4], [5, 6]]
        result = short_lists(lists)
        expected = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(result, expected)

    # Part 3
    def test_ascending(self):
        lists2 = [[4, 2], [3, 5, 1], [8], [9, 7]]
        result = ascending_pairs(lists2)
        expected = [[2, 4], [3, 5, 1], [8], [7, 9]]
        self.assertEqual(result, expected)

    def test_ascending_2(self):
        lists2 = [[5, 3], [2, 4], [6, 1]]
        result = ascending_pairs(lists2)
        expected = [[3, 5], [2, 4], [1, 6]]
        self.assertEqual(result, expected)

    # Part 4
from hw1 import Price
#I had to make a new class for these test to work, why?
class TestAdd(unittest.TestCase):
    def test_adding(self):
        price1 = Price(5,50)
        price2 = Price(3, 40)
        result = add_prices(price1, price2)
        expected = Price(8, 90)
        self.assertEqual((result.dollars, result.cents), (expected.dollars, expected.cents))

    def test_adding_2(self):
        price1 = Price(2, 80)
        price2 = Price(3, 50)
        result = add_prices(price1, price2)
        expected = Price(6, 30)
        self.assertEqual((result.dollars, result.cents), (expected.dollars, expected.cents))

    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
