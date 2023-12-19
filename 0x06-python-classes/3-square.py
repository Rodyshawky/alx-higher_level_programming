#!/usr/bin/python3
"""define Module"""


class Square:
    """Define class"""
    def __init__(self, size=0):
        """initial private size value"""
        self.__size = size
        if not isinstance(size, int):
            """Type Error Exception"""
            raise TypeError("size must be an integer")
        if size < 0:
            """Value Error Exception"""
            raise ValueError("size must be >= 0")
        """public function"""
    def area(self):
        """return square Area"""
        return self.__size ** 2
