import os

currentDirectoryPath = os.getcwd()
listOfFileNames = os.listdir(currentDirectoryPath)
print(listOfFileNames)
for name in listOfFileNames:
    if ".py" in name:
        print(name)