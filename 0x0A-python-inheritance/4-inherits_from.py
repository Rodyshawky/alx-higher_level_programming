#!/usr/bin/python3
""""Module of class"""


def inherits_from(obj, a_class):
    """Method of kind class"""
    return isinstance(obj, a_class) and type(obj) != a_class
