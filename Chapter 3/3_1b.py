# Loop to compute exponentiation for a 
# non-negative exponent
number = 2
exponent = 3
product = 1
for eachPass in range(exponent):
    product = product * number
    print(product, end = " ");