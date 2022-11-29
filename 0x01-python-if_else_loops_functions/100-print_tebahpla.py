#!/usr/bin/python3
for letters in range(122, 96, -1):
    c = letters
    if letters % 2 != 0:
        c = letters - 32
    print("{}".format(chr(c)), end="")
