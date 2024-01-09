#!/usr/bin/python3
"""Module write file"""

def write_file(filename="", text=""):
    with open(filename, "w", encoding="UTF-8") as my_file:
        my_file.write(text)
        return len(list(filename))
