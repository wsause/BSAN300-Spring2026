"""
When it is used with strings, the left operand of in is a target
subsctring and the right operand is the string to be searched.
Returns True if target string is somewhere in search string, or
False otherwise.
"""
fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]

for fileName in fileList:
    if ".txt" in fileName:
        print(fileName)