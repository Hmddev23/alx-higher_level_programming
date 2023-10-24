#!/usr/bin/python3

def magic_calculation(a, b):
    res = 0
    for i in range(1, 3):
        try:
            if a > b:
                raise Exception('Too far')
            res += a ** b / i
        except Exception:
            res = a + b
            break
    return res
