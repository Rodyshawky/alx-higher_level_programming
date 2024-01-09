#!/usr/bin/python3
"""Module append write file"""


def append_write(filename="", text=""):
    """function append write text"""
    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
