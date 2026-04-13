# A list is mutable - Elements can be insterted, removed, or replaced
example = [1, 2, 3, 4]

example[3] = 0
print(example)  # Output: [1, 2, 3, 0]


# List processing example that shows how to replace
# each number in a list with its square
numbers = [2, 3, 4, 5]

for index in range(len(numbers)):
    numbers[index] = numbers[index] ** 2

print(numbers)  # Output: [4, 9, 16, 25]