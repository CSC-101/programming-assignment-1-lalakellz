import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(input_string: str) -> int:
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    return count

# Part 2
def short_lists(input_lists: list[list[int]]) -> list[list[int]]:
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


# Part 6


# Part 7


# Part 8


