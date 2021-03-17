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


GROUP_FORTUNES = []
with open("grouped_fortunes.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["group"] == "1":
            GROUP_FORTUNES.append(row["fortune"])


def generate_number():
    return random.choice(range(1, 100))


def generate_fortune(fortune_list=FORTUNES):
    """
    This function selects and returns a random fortune when called.
    """
    return random.choice(fortune_list)


def main():
    print(
        f"""{greeting} {name}! Thanks for running the fortune machine!
Your lucky number is:  {generate_number()}
Your fortune is:  {generate_fortune(GROUP_FORTUNES)}"""
    )


if __name__ == "__main__":
    main()
