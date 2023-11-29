#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a &lt; b:
        return c
    elif c &gt; b:
        return a + b
    return a * b - c
