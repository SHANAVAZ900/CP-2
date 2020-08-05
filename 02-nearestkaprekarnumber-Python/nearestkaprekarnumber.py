# Note: please do not start this problem prior to completing previous problem.
# Bearing in mind the definition of Kaprekar Number from above problem, write the function
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45,
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number,
# nearestKaprekarNumber(50) returns 45.
# Note: as you probably guessed, this also cannot be solved by counting up from 0,
# as that will not be efficient enough to get past the autograder.
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.


#import math

def fun_nearestkaprekarnumber(n):
    low, high = n, n
    while True:
        low -= 1
        high += 1
        if Kaprekar(low) and Kaprekar(high):
            return min(low, high)
        elif Kaprekar(low):
            return low
        elif Kaprekar(high):
            return high


def Kaprekar(m):
    root = m ** 2
    val1, val2 = len(str(root)), 0
    while val2 < val1:
        val2 += 1
        val3 = 10 ** val2
        if val3 == m:
            continue
        res = int(root / val3) + (root % val3)
        if res == m:
            return True
    return False
