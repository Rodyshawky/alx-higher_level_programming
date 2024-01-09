#!/usr/bin/python3
"""define json module"""


import json


def load_from_json_file(filename):
    """function  json from  file """

    with open(filename, "r", encoding="utf-8") as f:
        json.load(f)
~                              
