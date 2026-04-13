# in determines an element's presence or absence,
# but does not return the position of the element (if found)
aList = [34, 45, 67]
target = 45

if target in aList:
    print(aList.index(target))
else:
    print(-1)


# The mothod sort mutates a list by arranging its elements in
# ascending order
example = [4, 2, 10, 8]
example.sort()
print(example)  # [2, 4, 8, 10]

# To sort in descending order (not in book)
example.sort(reverse=True)
print(example)