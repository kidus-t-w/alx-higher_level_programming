#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            tup_a = tuple_a[0], 0
        elif len(tuple_a) == 0:
            tup_a = (0, 0)
    else:
        tup_a = (tuple_a[0], tuple_a[1])

    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            tup_b = tuple_b[0], 0
        elif len(tuple_b) == 0:
            tup_b = (0, 0)
    else:
        tup_b = (tuple_b[0], tuple_b[1])

    x = tup_a[0] + tup_b[0]
    y = tup_a[1] + tup_b[1]
    addtup = (x, y)

    return addtup
