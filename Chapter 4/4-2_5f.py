"""
string representations of integers and flating-point
numbers can be converted to the numbers by using the
functions int and float.
"""

f = open("integers.txt", "r")
theSum = 0
for line in f:
    line = line.strip()
    number = int(line)
    theSum += number
print("The sum is", theSum)
f.close()