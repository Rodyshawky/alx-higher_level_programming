#!/usr/bin/python3
def multiple_returns(sentence):
    c = ''
    n = len(sentence)
    if not sentence:
        c = None
    else:
        c = sentence[0]
    return (n, c)
