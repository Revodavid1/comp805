"""
Jon Shallow
UNHM COMP705/805 Lab 1
An Introduction to Python
Jan 19, 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def give_me_a_string():
    """
    This function returns a string value
    """
    return "My name is Oreva"

def give_me_an_integer():
    """
    This function returns an integer value
    """
    return 27

def give_me_a_boolean():
    """
    This function returns a boolean value
    """
    return True

def give_me_a_float():
    """
    This function returns a float value
    """
    return 4.0

def give_me_a_list():
    """
    This function returns a list
    """
    return ["Kendrick","Jay","ColdPlay"]

def give_me_a_dictionary():
    """
    This function returns a dictionary
    """
    return {1:"Kendrick",2:"Jay",3:"ColdPlay"}

def give_me_a_tuple():
    """
    This function returns a tuple
    """
    return ("Oreva",27)

def sum_numbers_one_to_ten():
    """
    This function returns the sum of all numbers one to ten
    Use the range function:
    https://docs.python.org/3/library/functions.html
    Use the accumulator pattern:
    http://interactivepython.org/runestone/static/thinkcspy/Functions/TheAccumulatorPattern.html
    """
    fnum = range(0,11,1)
    fsum = 0
    for i in fnum:
        fsum = fsum + i
    return fsum

def check_is_even(number):
    """
    This function returns True if num is even
    else False
    hint: use modulo operator
    https://docs.python.org/3/reference/expressions.html
    """
    if number % 2 == 0:
   	    return True
    else:
   		return False

def check_is_less_than(number1, number2):
    """
    This functions returns True if number1 < number2
    else False
    """
    if number1 < number2:
        return True
    else:
        return False

def check_if_first_letter_of_string_is_uppercase():
    """
    This function checks if the first value of the returned string is true
    """
    return "Web"

def string_count_is_5():
    """
    Checks if the character count is 5, fails if it is less or more
    """
    return "sweet"
