# Chase Staples
# This is some tips and tricks I've learned in Python
# Some ranging from very east to very hard algorithms

# Imports
from functools import reduce


# Simple Math Functions
def square(x):
    return x ** 2


def even(x):
    return x % 2 == 0


def odd(x):
    return x % 2 == 1


def multiply(x, y):
    return x * y


# List Manipulations with Map, filter and reduce
def ListManipulations(arr):
    squares = list(map(square, arr))
    evens = list(filter(even, arr))
    odds = list(filter(odd, arr))
    products = reduce(multiply, arr)
    print("List Manipulation with Map, Filter, and Reduce")
    print("----------------------------------------------")
    print("Map")
    print(squares)
    print("Filter")
    print(evens)
    print(odds)
    print("Reduce")
    print(products)
    print("----------------------------------------------\n")


# Swapping 2 numbers
def Swap(x, y):
    print("Swapping 2 numbers/variables")
    print("--------------------------------")
    print("Before Swap x = ", x, " Y = ", y)
    x, y = y, x
    print("After Swap x = ", x, " Y = ", y)
    print("--------------------------------\n")


# Finding the largest and smallest numbers
def MinMax(lists):
    largest = max(lists)
    smallest = min(lists)
    print("Finding largest and smallest numbers in a list")
    print("--------------------------------")
    print("The largest number is: ", largest)
    print("The smallest number is: ", smallest)
    print("--------------------------------\n")


# List Manipulation for evens and odds up till range(numbers)
def ListEvensOdds(numbers):
    evens = [x for x in range(numbers) if x % 2 == 0]
    odds = [x for x in range(numbers) if x % 2 == 1]
    print("List of numbers even and odd")
    print("---------------------------------------------")
    print(evens)
    print(odds)
    print("---------------------------------------------\n")

# 1 line for Ternary Conditionals
def TernaryConditionals(condition):
    x = "Condition is True" if condition else "Condition is false"
    print("Ternary Conditionals")
    print("---------------------------------------------")
    print(x)
    print("---------------------------------------------\n")

# Underscore placeholders
def UnderScore():
    num1 = 10_000_000_000
    num2 = 100_000_000
    print("Underscore place holders")
    print("---------------------------------------------")
    print(f"{num1:,}")
    print(f"{num2:,}")
    print("---------------------------------------------\n")


# Notice a need for a context manager
def ContextManager(fileName):
    with open(fileName, 'r') as file:
        fileContents = file.read()
    words = fileContents.split(' ')
    wordCount = len(words)
    print("Context Manager for reading a file")
    print("---------------------------------------------")
    for word in fileContents:
        print(word, end="")
    print("\nThe word count of this file is: ", wordCount)
    print("---------------------------------------------\n")

# Enumerate for a list of names
def enumerates():
    names = ["Chase Staples", "Kyle Allen", "Smith Jr", "Carl Flint", "Steve Powers"]
    print("Adding enumerate to list")
    print("---------------------------------------------")
    for index, name in enumerate(names):
        print(index, name)
    print("---------------------------------------------\n")






myList = [9, 4, 10, 26, 18, 43, 14]
list2 = [x for x in range(1, 20)]

# Main
print()
ListManipulations(list2)
Swap(10, 20)
MinMax(myList)
ListEvensOdds(20)
TernaryConditionals(True)
UnderScore()
ContextManager('text.txt')
enumerates()