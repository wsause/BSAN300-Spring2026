"""
Python includes many useful functions,
which are organized in libraries of code called modules.
Functions often require arguments,
referred to by names known as parameters.
"""

# The math modules includes functions
# that perform basic mathematical operations
import math

print(math.sqrt(16))
print(math.pi)


# If you are going to use only a couple of the modules resources,
# you can just import the individual resources,
# which saves memory and makes your program run faster
from math import sqrt, pi

print(pi)
print(sqrt(16))