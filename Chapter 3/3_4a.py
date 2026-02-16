"""
The for loop executes a set of statements a definite number of times.
In may situations, however, the number of iterations in a loop is upredictable.
The while loop can be used to describe conditional iteration, meaning the
process continues to repeast as long as a condition remains true.
"""

# For example, a program's input loop can accept values until
# the user enters a sentinel that terminates the input.
theSum = 0.0
data = input("Enter a number or just enter to quit: ")

while data != "":       # while the user hasn't pressed the enter key
    number = float(data)
    theSum += number
    data = input("Enter a number or just enter to quit: ")

print("The sum is", theSum)