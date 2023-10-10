#!/usr/bin/python3
"""Module: 1-my_list"""


class MyList(list):

    def print_sorted(self):
        """
        Prints the list, int a sorted format
        """
        print(sorted(self))
