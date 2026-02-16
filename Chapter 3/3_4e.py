# Alternative: Use a Boolean variable to control the loop
done = False
while not done:     # equivalent to done != False
    number = int(input("Enter the numeric grade: "))

    if number >= 0 and number <= 100:
        done = True
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