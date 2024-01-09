#!/usr/bin/python3
"""define json module"""


import json


def to_json_string(my_obj):
    """function json"""
    json_string = json.dumps(my_obj)
    return json_string
