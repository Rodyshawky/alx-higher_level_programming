#!/usr/bin/python3
"""define Module"""


class Square:
    """Define class"""
    def __init__(self, size=0):
        """initial private size value"""
        self.__size = size
        """size getter"""
    @property
    def size(self):
        return self.__size
    """size setter"""
    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            """Type Error Exception"""
            raise TypeError("size must be an integer")
        if value < 0:
            """Value Error Exception"""
            raise ValueError("size must be >= 0")
        """public function"""
    def area(self):
        """return square Area"""
        return self.__size ** 2
    def my_print(self):
        i = 0
        j = 0
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()
