#!/usr/bin/python3
"""Module class MyList"""


class MyList(list):
    """class MyList"""
    def print_sorted(self):
        """print Method"""
        print(sorted(list(self)))
