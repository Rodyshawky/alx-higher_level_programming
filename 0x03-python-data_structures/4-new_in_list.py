#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)
    if idx < 0:
        return my_list
    elif idx < n:
        for i in range(n):
            new_list = [element if i == idx else i for i in my_list]
            return new_list
    else:
        return my_list
