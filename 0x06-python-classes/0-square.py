#!/usr/bin/python3
class Square:
    """
    This function takes an argument and returns the squre 
    Args:
        a(int): The first number
    Returns:
        int: The su quare of a number
    """
    def __init__(self, num):
        self.num = num
    def cal_squ(self):
        return self.num ** 2
    