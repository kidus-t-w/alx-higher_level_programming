#!/usr/bin/python3
def no_c(my_string):
    newstr = ""
    if my_string is None:
        return
    for i in my_string:
        if i != 'c' and i != 'C':
            newstr = newstr + i
    return newstr
