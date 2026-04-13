# You can sort the list first the traverse it to print the
# entries of the dictionary in alphabetical order:
info = {"occupation":"manager", "name":"Sandy"}

theKeys = list(info.keys())
theKeys.sort()

for key in theKeys:
    print(key, info[key])