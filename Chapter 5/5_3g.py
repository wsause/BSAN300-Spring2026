# Example: Finding the mode of a list of values.
# The mode of a list of values is the value that occurs most frequently.
# The following script inputs a list of words from a text file and
# prints their mode.

fileName = input("Enter the filename: ")
f = open(fileName, "r")

# Input the text, convert its words to uppercase,
# add the words to a list
upperWords = []
for line in f:      # assuming this file has multiple lines (ending with \n)
    words = line.split()
    for word in words:
        word = word.upper()
        upperWords.append(word)

# Obtain unique words and frequencies, saving these to a dictionary
theDictionary = {}
for word in upperWords:
    number = theDictionary.get(word, None)
    if number == None:  # word entered for the first time
        theDictionary[word] = 1
    else:   # word already seen, increment its number
        theDictionary[word] = number + 1

# Find the mode by obtaining max value in dictionary
# and determining its key
theMaximum = max(theDictionary.values())
for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print("The mode is", key)
        break