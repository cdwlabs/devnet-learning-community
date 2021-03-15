#!/usr/bin/env python
"""
Some quick notes on running scripts and virtual environments:
https://realpython.com/run-python-scripts/
https://realpython.com/python-virtual-environments-a-primer/
"""

# Imports and how they work: https://realpython.com/python-modules-packages/
import random
import csv

# Variables and assignment - https://realpython.com/python-variables/
greeting = "Hello"
name = input("What's your name?  ")

# Also, Real Python summary of lists and tuples - https://realpython.com/python-lists-tuples/
FORTUNES = [
    "There is a good chance your code will work, eventually.",
    "I see Network DevOps in your future.",
]

# Working with files in Python - https://realpython.com/working-with-files-in-python/
with open("fortune_cookies.txt", "r") as file:
    FORTUNE_COOKIES = file.read().splitlines()

# CSV file load into dictionary - This is a broad topic and Real Python has a great overview: https://realpython.com/python-csv/
GROUP_FORTUNES = []
with open("grouped_fortunes.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["group"] == "1":
            GROUP_FORTUNES.append(row["fortune"])


# Real Python - Functions in Python - https://realpython.com/defining-your-own-python-function/
def generate_number():
    return random.choice(range(1, 100))


def generate_fortune(fortune_list=FORTUNES):
    """
    This function selects and returns a random fortune when called.
    """
    return random.choice(fortune_list)


# What is a main function? Why do this? https://realpython.com/python-main-function/
def main():
    # Building text output without string formatting eatures.
    print(greeting + " " + name + "! Thanks for running the fortune machine!")
    print("Your lucky number is: " + str(generate_number()))
    print("Your fortune is:  " + generate_fortune())

    """
    Various string formatting types used.
    The history of the formats and best practices can be found here:
    https://realpython.com/python-string-formatting/
    """
    # Oldest string formatting style. Mostly seen in Python 2 code.
    print(
        """%s %s! Thanks for running the fortune machine!
Your lucky number is:  %s
Your fortune is:  %s"""
        % (greeting, name, generate_number(), generate_fortune())
    )

    # Python 3 introduced the .format syntax. Newer versions on 2.7 had .format added to them
    print(
        """{} {}! Thanks for running the fortune machine!
Your lucky number is:  {}
Your fortune is:  {}""".format(
            greeting, name, generate_number(), generate_fortune()
        )
    )

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

    # Python 3.6+ support f-strings. These are generally cleaner and easier to read.
    print(
        f"""{greeting} {name}! Thanks for running the fortune machine!
Your lucky number is:  {generate_number()}
Your fortune is:  {generate_fortune()}"""
    )

    # Oldest string formatting style. Mostly seen in Python 2 code.
    print("%s Thanks for running the fortune machine!" % greeting)
    # Python 3 introduced the .format syntax. Newer versions on 2.7 had .format added to them
    print("Your lucky number is:  {}".format(generate_number()))
    # Python 3.6+ support f-strings. These are generally cleaner and easier to read.
    print(f"Your fortune is:  {generate_fortune()}")


# Check to see if this file is the "__main__" script being executed
if __name__ == "__main__":
    main()
