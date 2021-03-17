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
    print("%s Thanks for running the fortune machine!" % greeting)
    # Python 3 introduced the .format syntax. Newer versions on 2.7 had .format added to them
    print("Your lucky number is:  {}".format(generate_number()))
    # Python 3.6+ support f-strings. These are generally cleaner and easier to read.
    print(f"Your fortune is:  {generate_fortune()}")


# Check to see if this file is the "__main__" script being executed
if __name__ == "__main__":
    main()
