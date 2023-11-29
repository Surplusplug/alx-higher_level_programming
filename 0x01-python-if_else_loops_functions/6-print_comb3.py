#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        if i * 10 + j &lt; 89:
            print("{:d}{:d}".format(i, j), end=", ")
            print("{:d}".format(89))
