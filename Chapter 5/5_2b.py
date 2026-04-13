# A Boolean function usually tests its argument for the
# presence of absence of some property

def odd(x):
    if x % 2 == 1:  # x has a remainder of 1 (odd)
        return True
    else:
        return False

print(odd(5))
print(odd(6))