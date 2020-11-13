
# Simple Math Functions to test

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if(y == 0):
        raise ValueError('Can divide by zero!')
    return x / y