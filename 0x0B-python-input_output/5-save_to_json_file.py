#!/usr/bin/python3
"""define json module"""


import json


def save_to_json_file(my_obj, filename):
    """function save json to file """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
