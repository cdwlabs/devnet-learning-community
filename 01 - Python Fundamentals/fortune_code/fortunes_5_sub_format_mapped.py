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
    # You can improve readability of .format syntax with variable substitution.
    # Note that functions can't be set as variables though and the code isn't easy to read.
    print(
        """{greeting} {name}! Thanks for running the fortune machine!
Your lucky number is:  {generate_number}
Your fortune is:  {generate_fortune}""".format(
            greeting=greeting,
            name=name,
            generate_number=generate_number(),
            generate_fortune=generate_fortune(),
        )
    )


# Check to see if this file is the "__main__" script being executed
if __name__ == "__main__":
    main()
