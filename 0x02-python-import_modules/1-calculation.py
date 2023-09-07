#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    addition = add(a, b)
    subs = sub(a, b)
    multi = mul(a, b)
    divi = div(a, b)
    print("{} + {} = {}".format(a, b, addition))
    print("{} - {} = {}".format(a, b, subs))
    print("{} * {} = {}".format(a, b, multi))
    print("{} / {} = {}".format(a, b, divi))
