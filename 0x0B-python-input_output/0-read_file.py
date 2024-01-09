#!/usr/bin/python3
"""Module read file"""


def read_file(filename=""):
    """function read file"""
    with open(filename, "r",  encoding="UTF-8") as my_file:
        print(my_file.read(), end="")
