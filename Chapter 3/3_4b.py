# The while loop can be complicated to write correctly;
# It is possible to simplify its structure and improve its readability

theSum = 0

while True:
    data = input("Enter a number or just enter to quit: ")
    if data == "":      # termination condition
        break
    number = float(data)
    theSum += number

print("The sum is", theSum)