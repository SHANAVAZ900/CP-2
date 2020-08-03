# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that
# number contains two consecutive digits that are the same, and False otherwise.


def hasconsecutivedigits(n):
    # your code goes here
    n = abs(n)

    flag = n

    while flag > 0:
        res = (flag % 10)
        flag //= 10
        if res == (flag % 10):
            return True
    return False
