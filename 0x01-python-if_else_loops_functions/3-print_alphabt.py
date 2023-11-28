#!/usr/bin/python3
for ch in range(ord('a'), ord('z') + 1):
    if ch == ord('q') or ch == ord('e'):
        continue
    print("{:c}".format(ch), end="")
