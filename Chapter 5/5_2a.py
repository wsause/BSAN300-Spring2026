"""
Defining our own functions allows us to organize our code
in existing scripts more effectively.
Definition of a function consists of a header and a body.
"""
def square(x):
    print(x * x)

square(4)

"""
Place a return statement at each exit point of a function
when the function should explicity return a value.
"""
def square(x):
    return x * x

print(square(5))
