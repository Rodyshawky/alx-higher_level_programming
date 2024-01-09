#!/usr/bin/python3
"""define json module"""


import json


def save_to_json_file(my_obj, filename):
    """function save json to file """

    json_string = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json_string)
