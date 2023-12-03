#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    n = len(my_list)
    if idx < 0:
        return my_list
    for i in range(n):
        if idx == i:
            my_list[i] = element
            return my_list
        elif idx > n:
            return my_list
