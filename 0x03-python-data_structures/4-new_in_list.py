#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)
    if idx < 0:
        return my_list
    elif idx < n:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
    elif idx >= n:
        return my_list
