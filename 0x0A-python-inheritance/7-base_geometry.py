#!/usr/bin/python3
"""Module of BaseGeometry"""


class BaseGeometry:
    """A BaseGeometry class"""
    def area(self):
        """function raise exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Function validate integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
