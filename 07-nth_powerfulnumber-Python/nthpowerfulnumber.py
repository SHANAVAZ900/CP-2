# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it.
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math


def nthpowerfulnumber(n):
    # Your code goes here
    c, v = 0, 1
    while c < n:
        v += 1
        if prime(v):
            c += 1
    return v


def prime(m):
    val = 0
    while m % 2 == 0:
        val += 1
        m //= 2
    if val == 1:
        return False
    for i in range(3, int(math.sqrt(m)) + 1, 2):
        val = 0
        while m % i == 0:
            val += 1
            m = m // i
        if val == 1:
            return False
    return m == 1
