#!/usr/bin/python3
def remove_char_at(str, n):
    copy_str = ""
    for i, c in enumerate(str):
        if i != n:
            copy_str += c
    return copy_str
