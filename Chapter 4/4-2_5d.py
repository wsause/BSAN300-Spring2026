# A for loop can be used to read
# one line of a file at time

f = open("myfile.txt", "r")
for line in f:
    print(line.strip())
f.close()
