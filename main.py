"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Divide by zero")
    else:
        return b / a
def log(a, b):
    if b <= 0 or a <= 1:
        raise ValueError("Cannot use a negative number")
    else:
        return math.log(a, b)
def exp(a, b):
    return a**b