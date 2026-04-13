"""
It is interesting that when the Python interpreter
evaluates a list literal,
each of the elements is evaluated as well.
"""
import math

x = 2
print([x, math.sqrt(x)])
print([x + 1])


# Lists of integers can be built using the range and 
# list functions
first = [1, 2, 3, 4]
second = list(range(1, 5))
print(first)
print(second)


# The list function can build a list from any iterable
# sequence of elements.
third = list("Hi there!")
print(third)
