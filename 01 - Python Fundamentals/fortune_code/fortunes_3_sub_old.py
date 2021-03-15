#!/usr/bin/env python
# Imports
import random

greeting = "Hello"
name = input("What's your name?  ")

FORTUNES = [
    "There is a good chance your code will work, eventually.",
    "I see Network DevOps in your future.",
]


def generate_number():
    return random.choice(range(1, 100))


def generate_fortune(fortune_list=FORTUNES):
    """
    This function selects and returns a random fortune when called.
    """
    return random.choice(fortune_list)


def main():
    # Oldest string formatting style. Mostly seen in Python 2 code.
    print(
        """%s %s! Thanks for running the fortune machine!
Your lucky number is:  %s
Your fortune is:  %s"""
        % (greeting, name, generate_number(), generate_fortune())
    )


if __name__ == "__main__":
    main()
