# Print the maximum and minimum of two input numbers
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first > second:
    maximum = first
    minimum = second
else:
    maximum = second
    minimum = first
print("Maximum: ", maximum)
print("Minimum: ", minimum)

# Note: Python inclues two built-in functions, max and min,
# that make the if-then statement above unnecessary.
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

print("Maximum: ", max(first, second))
print("Minimum: ", min(first, second))


# Multi-way selection statement
# can check if they're equal
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first > second:
    maximum = first
    minimum = second
    print("Maximum: ", maximum)
    print("Minimum: ", minimum)
elif second > first:
    maximum = second
    minimum = first
    print("Maximum: ", maximum)
    print("Minimum: ", minimum)
else:
    print("These numbers are equal.")
