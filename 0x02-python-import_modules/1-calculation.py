#!/usr/bin/python3
import calculator_1
a = 10
b = 5
addition = calculator_1.add(a, b)
subs = calculator_1.sub(a, b)
multi = calculator_1.mul(a, b)
divi = calculator_1.div(a, b)
print("{} + {} = {}".format(a, b, addition))
print("{} - {} = {}".format(a, b, subs))
print("{} * {} = {}".format(a, b, multi))
print("{} / {} = {}".format(a, b, divi))
