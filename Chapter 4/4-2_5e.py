"""
In cases where you might want to read a specified number
of lines from a file (say, the first line only),
# you can use the file method readline
"""

f = open("myfile.txt", "r")
while True:
    line = f.readline()
    if line == "":  # reached the end of the file
        break
    print(line)
f.close()