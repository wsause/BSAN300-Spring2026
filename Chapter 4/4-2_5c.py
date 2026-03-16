# You open a file for input in a manner
# similar to opening a file for output

f = open("myfile.txt", "r")
text = f.read()
print(text)
f.close()