#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    remainder = (number) % 10
else:
    remainder = (number % (-10)) * (-1)
print(f"Last digit of {number} is {remainder} and is ", end="")
if remainder > 5:
    print("greater than 5")
elif remainder == 0:
    print("0")
else:
    print("less than 6 and not 0")
