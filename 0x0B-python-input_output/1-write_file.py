#!/usr/bin/python3
"""Module write file"""

def write_file(filename="", text=""):
    with open(filename, "w", encoding="UTF-8") as my_file:
        return my_file.write(text)
