#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastDigit = number % 10
elif number < 0:
    lastDigit = number % -10
if lastDigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastDigit))
elif lastDigit < 5 and lastDigit != 0:
    print("Last digit of {:d} is {:d} and is less than 5 and not 0"
          .format(number, lastDigit))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
