# This example modifies the grade-conversion program
while True:
    number = int(input("Enter the numeric grade: "))

    if number >= 0 and number <= 100:
        break
    else:
        print("Error: grade must be between 0 and 100")

if number > 89:
    letter = "A"
elif number > 79:
    letter = "B"
elif number > 69:
    letter = "C"
else:
    letter = "F"
print("The letter grade is", letter)