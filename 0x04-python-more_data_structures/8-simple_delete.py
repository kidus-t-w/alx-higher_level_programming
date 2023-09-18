#!/usr/bin/python3
def simple_del(a_dictionary, key=""):
    if key not in a_dictionary:
        return a_dictionary
    elif key in a_dictionary:
        del a_dictionary[key]
        return a_dictionary
