#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# flag is used to check whether we have found a negative number
flag = 1
if number < 0:
    number *= -1
    flag = 0
last_d = number % 10
if flag == 0:
    number *= -1
    last_d *= -1
print("Last digit of {:d} is {:d}".format(number, last_d), end="")
if last_d > 5:
    print(" and is greater than 5")
elif last_d == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
