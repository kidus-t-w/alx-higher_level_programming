#!/usr/bin/python3

for i in range(0, 8):
    for x in range(0, 9):
        if (i < x):
            print("{:d}{:d}".format(i, x), end=", ")
print("{:d}{:d}".format(8, 9))
