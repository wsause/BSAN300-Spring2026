"""
Ceaser cipher replaces each character in plain text with a
character a given distance away.
The ord function returns the ordinal position in the ASCII sequence.
chr is the inverse function.
"""
plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter a distance value: "))
code = ""

for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > ord('z'):  # if value is after z, move back to a
        cipherValue = ord('a') + distance - (ord('z') - ordValue + 1)
    code = code + chr(cipherValue)

print(code)