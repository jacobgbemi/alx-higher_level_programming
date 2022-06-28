#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    remainder = (number) % 10
else:
    remainder = (number % (-10))

if remainder > 5:
    print(f"Last digit of {number:d} is {remainder:d} and is greater than 5")
elif remainder == 0:
    print(f"Last digit of {number:d} is {remainder:d} and is 0")
else:
    print(f"Last digit of {number:d} is "
          f"{remainder:d} and is less than 6 and not 0")
