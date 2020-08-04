# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every
# digit (from 0 to 9) at least once. 309 is the smallest number with this property.
# Write the function nthWithProperty309 that takes a non-negative int n and returns
# the nth number with Property309.


def nthwithproperty309(n):

    pow = 1
    answer = 0

    # Go through every bit of n
    while (n):

        pow = pow*5

        # If last bit of n is set
        if (n & 1):
            answer += pow

        # proceed to next bit
        n >>= 1  # or n = n/2

    return answer
