#!/usr/bin/env python
"""
Some quick notes on running scripts and virtual environments:
https://realpython.com/run-python-scripts/
https://realpython.com/python-virtual-environments-a-primer/
"""

# Imports and how they work: https://realpython.com/python-modules-packages/
import random

# Variables and assignment: https://realpython.com/python-variables/
greeting = "Hello"

# Insight on input and output on the console: https://realpython.com/python-input-output/
name = input("What's your name?  ")

# Also, Real Python summary of lists and tuples - https://realpython.com/python-lists-tuples/
FORTUNES = [
    "There is a good chance your code will work, eventually.",
    "I see Network DevOps in your future.",
]


# Function basics - https://realpython.com/defining-your-own-python-function/
def generate_number():
    return random.choice(range(1, 100))


def generate_fortune(fortune_list=FORTUNES):
    """
    This function selects and returns a random fortune when called.
    """
    return random.choice(fortune_list)


# Building text output without string formatting features. Related to the input resoruces above.
print(greeting + " " + name + "! Thanks for running the fortune machine!")
print("Your lucky number is: " + (generate_number()))
print("Your fortune is:  " + generate_fortune())
