#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    try:
        while i != x:
            print("{:d}".format(my_list[i]))
            i += 1
            count += 1
    except (IndexError, TypeError):
        None
    return count

