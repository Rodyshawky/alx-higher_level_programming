#!/usr/bin/python3
"""define Module"""


class Square:
    """Define Class"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

        """public function"""
    def area(self):
        """return square Area"""
        return self.__size * self.__size
    """ print # square"""
    def my_print(self):
        """ print empty line"""
        if self.__size == 0:
            print("")
            return
        """print square"""
        [print("") for i in range(1, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
