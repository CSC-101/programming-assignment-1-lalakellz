import math

import data
import hw1
import unittest

from hw1 import add_prices, vowel_count, short_lists, ascending_pairs, rectangle_area, books_by_author, circle_bound, \
    Employee, below_pay_average


# Write your test cases for each part below.
class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel(self):
        input_str = "We Love Donuts"
        result = vowel_count(input_str)
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
from hw1 import Rectangle
class TestRectArea(unittest.TestCase):
    def test_rect_area(self):
        rec = Rectangle(2, 5, 5, 2)
        result = rectangle_area(rec)
        expected = 9
        self.assertEqual(result, expected)

    def test_rect_area_2(self):
        rec = Rectangle(0, 10, 10, 0)
        result = rectangle_area(rec)
        expected = 100
        self.assertEqual(result, expected)

    # Part 6
from hw1 import Book
class TestBooks(unittest.TestCase):

    def test_books(self):
        book1 = Book("Pink Matter", "Frank Ocean")
        book2 = Book("911", "Tyler the Creator")
        book3 = Book("White Ferari", "Frank Ocean")

        books = [book1, book2, book3]
        result = books_by_author("Frank Ocean", books)
        expected = [book1, book3]
        self.assertEqual(result, expected)

    def test_books_2(self):
        book1 = Book("Pink Matter", "Frank Ocean")
        book2 = Book("911", "Tyler the Creator")
        book3 = Book("White Ferari", "Frank Ocean")

        books = [book1, book2, book3]
        result = books_by_author("ASAP Rocky", books)
        expected = []
        self.assertEqual(result, expected)

# Part 7
    def test_circle(self):
        rec = Rectangle(2, 5, 8, 1)
        circle = circle_bound(rec)
        expected_center = (5.0, 3.0)
        expecter_radius = math.sqrt(9 + 4)
        self.assertEqual((circle.center_x, circle.center_y), expected_center)
        self.assertAlmostEqual(circle.radius, expecter_radius)

    def test_circle_2(self):
        rec = Rectangle(0, 4, 4, 0)
        circle = circle_bound(rec)
        expected_center = (2.0, 2.0)
        expected_radius = math.sqrt(2**2 + 2**2)
        self.assertEqual((circle.center_x, circle.center_y), expected_center)
        self.assertAlmostEqual(circle.radius, expected_radius)

    # Part 8
    def test_below_pay(self):
        emp1 = Employee("Liyah", 50000)
        emp2 = Employee("Ella", 40000)
        emp3 = Employee("Josh", 60000)

        employees = [emp1, emp2, emp3]
        result = below_pay_average(employees)
        expected = ['Ella']
        self.assertEqual(result, expected)

    def test_below_pay_2(self):
        employees = []
        result = below_pay_average(employees)
        expected = []
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
