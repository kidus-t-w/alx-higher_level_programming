#!/usr/bin/python3
def print_sorted_dictionary(a_dictonary):
    for i in sorted(a_dictonary):
        print("{}: {}".format(i, a_dictonary[i]))
    return
