"""
Note that the code uses a for loop over an index rather than
a for loop over the list of elements, because the index is needed
to access the positions for the replacements
"""

sentence = "The example has five words."
words = sentence.split()

for index in range(len(words)):
    words[index] = words[index].upper()

print(words)