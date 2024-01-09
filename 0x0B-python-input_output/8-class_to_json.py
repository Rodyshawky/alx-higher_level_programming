#!/usr/bin/python3
"""Module containing the function class_to_json"""


def class_to_json(obj):
    """Returns the dictionary description

    Args:
        obj (MyClass): object.

    Returns:
        dict: dictionary.
    """
    # print("type of obj --> {}".format(type(obj)))
    return obj.__dict__
