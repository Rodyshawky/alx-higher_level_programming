#!/usr/bin/python3
"""define json module"""


import json


def from_json_string(my_str):
    """function json to string """
    json_string = json.loads(my_str)
    return json_string
~                            
