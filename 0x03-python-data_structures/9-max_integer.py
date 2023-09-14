#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return (None)
    length = len(my_list) - 1
    while l > 1:
        j = 0
        while j < l:
            for i in my_list:
                if my_list[j] > my_list[j + 1]:
                    temp = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j + 1] = temp
            j += 1
        length -= 1
    max_num = my_list[len(my_list) - 1]
    return (max_num)
