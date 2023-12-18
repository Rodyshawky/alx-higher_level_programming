#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = 0
    i = 0
    new_list = []
    while i < list_length:
        try:
            res = my_list_1[i] / my_list_2[i]
            new_list.append(res)
            i += 1
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
            i += 1
            continue
        except TypeError:
            new_list.append(0)
            print("wrong type")
            i += 1
            continue
        except IndexError:
            new_list.append(0)
            print("out of range")
            i += 1
            continue
        finally:
            pass
    return new_list
