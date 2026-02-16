# range expents a third argument
# that allows you to specify a step value
print(list(range(1, 6, 1)))     # Same as using two argument
print(list(range(1, 6, 2)))     # Use every other number
print(list(range(1, 6, 3)))     # Use every third number

# Example: sum of even numbers from 2 to 10
# using a step value of 2
theSum = 0
for count in range(2, 11, 2):
    theSum += count
print(theSum)