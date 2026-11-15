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

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def log(a, b):
    if b <= 0 or a <= 1:
        raise ValueError("Cannot use a negative number")
    else:
        return math.log(a, b)
def exp(a, b):
    return a**b

def logarithm(a, b):
    if b <= 0 or a <= 0:
        raise ValueError("Cannot use a negative number")
    
    if a == 1:
        raise ValueError("Argument cannot be exactly 1.")
    
    return math.log(a, b)

def exponent(a, b):
    return a**b
