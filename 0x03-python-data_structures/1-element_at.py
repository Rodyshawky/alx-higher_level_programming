#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    n = len(my_list)
    for i in range(n):
        if idx == i:
            return my_list[i]
        elif idx > n:
            return None
