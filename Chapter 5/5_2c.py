# Our next example function computes the average
# value in a list of numbers.

def average(lyst):
    theSum = 0
    for number in lyst:
        theSum += number
    return theSum / len(lyst)

print(average([1, 3, 5, 7]))