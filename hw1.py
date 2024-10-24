import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(input_string: str) -> int:
    #gives all possible vowel values
    vowels = "aeiouAEIOU"
    # adds 1 each time a vowel is found in the input string
    count = sum(1 for char in input_string if char in vowels)
   #returns the sum of the vowels in input_string
    return count

# Part 2
def short_lists(input_lists: list[list[int]]) -> list[list[int]]:
    #checks if length of list is equal to 2 then returns
    return [lst for lst in input_lists if len(lst) == 2]

# Part 3
def ascending_pairs(input_lists: list[list[int]]) -> list[list[int]]:
    # Initialize a result list
    result = []

    # Process each nested list in the input
    for lst in input_lists:
        # Check the length of the nested list
        if len(lst) == 2:
            # Sort the nested list if its length is 2
            result.append(sorted(lst))
        else:
            # Append the nested list unchanged if its length is not 2
            result.append(lst)

    # Return the final result
    return result

# Part 4
"""
    This function takes two Price objects and returns the sum 
    Parameters:
    price1 (Price): The first Price object.
    price2 (Price): The second Price object. 
    ###is this how im supposed to do the logistics part?
"""
class Price:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents

def add_prices(price1: Price, price2: Price) -> Price:

    # Calculate total dollars and total cents
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents

    # adjust for too many cents
    total_dollars += total_cents // 100 #add to dollars
    total_cents = total_cents % 100 #keep with 0-99

    return Price(total_dollars, total_cents)

# Part 5
class Rectangle:
    # Initialize a rectangle with the coordinates of the top-left (x1, y1) and bottom-right (x2, y2) corners.
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def rectangle_area(rec: Rectangle) -> int:
    """
    This function computes the area of a rectangle given its coordinates.
    It assumes the rectangle is axis-aligned, with sides parallel to the x- and y-axes.

    Parameters:
    rec (Rectangle): The rectangle for which to compute the area
    """
    width = rec.x2 - rec.x1
    height = rec.y1 - rec.y2
    return width * height

# Part 6
class Book:

    def __init__(self, title: str, author: str):
        """
        Parameters:
        title (str): The title of the book.
        author (str): The name of the author.
        """
        self.title = title
        self.author = author


#takes an authors name and a list of Book objects, returning a list of books written by the specified author
def books_by_author(author_name: str, books: list[Book]) -> list[Book]:
#  returns list of Book objects written by the specified author
    return [book for book in books if book.author == author_name]

# Part 7
import math
class Circle:
    def __init__(self, center_x:float, center_y:float, radius: float):
        """
        Parameters:
        center_x (float): x-coordinate of the circle's center.
        center_y (float): y-coordinate of the circle's center.
        radius (float): Radius of the circle.
        """
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

def circle_bound(rec: Rectangle) -> Circle:
    # Calculate the center of the rectangle
    center_x = (rec.x1 + rec.x2) / 2
    center_y = (rec.y1 + rec.y2) / 2

    # Calculate the distance from the center to one of the corners
    radius = math.sqrt((rec.x1 - center_x) ** 2 + (rec.y1 - center_y) ** 2)
    return Circle(center_x, center_y, radius)

# Part 8
class Employee:
    def __init__(self, name:str, pay_rate: float):
        """
        This function takes a list of Employee objects and returns a list of names of employees
        whose pay rate is below the average pay rate of all employees in the list.

        Parameters:
        employees (list[Employee]): A list of Employee objects.
        """
        self.name = name
        self.pay_rate = pay_rate

def below_pay_average(employees: list[Employee]) -> list[str]:
    if not employees:
        return [] # Return an empty list if there are no employees

    # Calculate the total pay and the average pay rate
    total_pay = sum(employee.pay_rate for employee in employees)
    average_pay = total_pay / len(employees)

    # Get the names of employees whose pay is less than the average
    below_average = [employee.name for employee in employees if employee.pay_rate < average_pay]
    return below_average