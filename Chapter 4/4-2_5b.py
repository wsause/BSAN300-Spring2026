"""
The file method write expects a string as an argument.
Other types of data must first be converted to strings
before being written to an output file (e.g., using str)
"""

import random

f = open("integers.txt", "w")
for count in range(500):
    number = random.randint(1, 500)
    f.write(str(number) + "\n")
f.close()