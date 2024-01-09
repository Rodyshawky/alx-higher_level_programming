#!/usr/bin/python3
"""Module write file"""


def write_file(filename="", text=""):
    """function write text"""
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
