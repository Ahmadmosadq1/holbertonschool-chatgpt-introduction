#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1        # ← FIX: decrement n each time, otherwise the loop never ends
    return result

f = factorial(int(sys.argv[1]))
print(f)

