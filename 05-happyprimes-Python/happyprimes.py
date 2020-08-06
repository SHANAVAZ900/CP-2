# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After
# some thought, we see that no matter what number we start with, when we keep replacing
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write happy(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n).
# And that's top-down design! Here we go....
# Note: the autograder will grade each of the following functions, so they are required.
# However, they also are here specifically because they are just the right helper
# functions to make nthHappyNumber(n) easier to write!


import math


def square(n):
    return n**2


def ishappyprimenumber(n):
    # Your code goes here
    if prime(n) and happy(n):
        return True
    return False
    pass


def happy(n):
    # your code goes here

    if n < 1:
        return False
    if n == 1:
        return True
    while n != 1:
        if len(str(n)) == 1:
            break
        l = list(str(n))
        l = list(map(int, l))
        l = list(map(square, l))
        n = sum(l)
    if n == 1:
        return True
    else:
        return False
    pass


def prime(g):
    if g < 2:
        return False
    else:
        for i in range(2, (g//2)+1):
            if g % i == 0:
                return False
        return True
