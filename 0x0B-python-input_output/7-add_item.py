#!/usr/bin/python3
"""Module that loads, adds and saves arguments to a Python list"""
import sys


load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

arg_list = list(sys.argv[1:])
try:
    json_list = load_file('add_item.json')
Exception:
    json_list = []

json_list.extend(arg_list)
save_file(json_list, 'add_item.json')
