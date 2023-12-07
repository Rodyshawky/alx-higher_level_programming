#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq = list(map(lambda x: list(map(lambda i: i ** 2, x)), matrix))
    return sq
