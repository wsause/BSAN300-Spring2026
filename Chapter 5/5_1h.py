# extend performs a similar operation, but adds the
# elements of its list argument to the end of the list
example = [1, 2, 3]
example.extend([11, 12, 13])
print(example)      # Output: [1, 2, 3, 11, 12, 13]

# The method pop is used to remove an element at a given position
example.pop()   # Remove the last element
print(example)  # Output: [1, 2, 3, 11, 12]
example.pop(0)  # Remove the first element
print(example)  # Output: [2, 3, 11, 12]

# The method remove is used to remove an element using its value (not in book)
example.remove(11)
print(example)  # Output: [2, 3, 11]