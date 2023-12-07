#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    else:
        res = 0
        n = 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for r in reversed(roman_string):
            n = dic[r]
            res += n if res < n * 5 else -n
        return res
