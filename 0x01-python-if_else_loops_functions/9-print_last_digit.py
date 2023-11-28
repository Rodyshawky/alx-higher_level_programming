#!/usr/bin/python3
def print_last_digit(number):
    if number > 10:
        digit = number % 10
    else:
        digit = number % -10
    return digit
