# len and [] work on lists as they do for strings
first = [1, 2, 3, 4]
print(first[0])     # Output: 1
print(len(first))   # Output: 4
print(first[2:4])   # Output: [3, 4]

# Concatenation (+) and equality (==) also work as expected
# for lists
first = [1, 2, 3, 4]
second = list(range(1, 5))
print(first + [5, 6])   # Output: [1, 2, 3, 4, 5, 6]
print(first == second)  # Output: True

# We can detect the presence of an element using the in operator
print(3 in [1, 2, 3])   # True
print(0 in [1, 2, 3])   # False