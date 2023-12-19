#!/usr/bin/python3
"""define Module"""


class Square:
    """Define Class"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    """position getter"""
    @property
    def position(self):
        return self.__position
    """position setter"""
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            """Type Error Exception"""
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value
        """public function"""
    def area(self):
        """return square Area"""
        return self.__size * self.__size

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print("")
            return
        [print("", end="") for f in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
