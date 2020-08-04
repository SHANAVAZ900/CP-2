# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every
# digit (from 0 to 9) at least once. 309 is the smallest number with this property.
# Write the function nthWithProperty309 that takes a non-negative int n and returns
# the nth number with Property309.


def nthwithproperty309(n):
    # Your code goes here
    calc, num = 0, 309
    note = list("0123456789")
    while calc < n:
        num += 1
        star5 = (num) ** (5)
        note1 = list(str(star5))
        if set(note).issubset(set(note1)):
            calc += 1
    return num
