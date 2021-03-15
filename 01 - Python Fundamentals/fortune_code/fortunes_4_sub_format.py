#!/usr/bin/env python
# Imports
import random
import csv

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
    # Python 3 introduced the .format syntax. Newer versions on 2.7 had .format added to them
    print(
        """{} {}! Thanks for running the fortune machine!
Your lucky number is:  {}
Your fortune is:  {}""".format(
            greeting, name, generate_number(), generate_fortune()
        )
    )


# Check to see if this file is the "__main__" script being executed
if __name__ == "__main__":
    main()
