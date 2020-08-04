# Write the function nthSmithNumber that takes a non-negative int n
# and returns the nth Smith number, where a Smith number is a composite (non-prime)
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1).
# Note that if a prime number divides the Smith number multiple times, its digit sum
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22


import math


def fun_nth_smithnumber(n):
    c, v = 0, 4
    #  c v is repeated
    while c < n:
        v += 1
        total_num = total_digits(v)
        pfactors = prime_factors(v)
        total_factors = sum([total_digits(x) for x in pfactors])
        if composite_num(v) and total_num == total_factors:
            c += 1
    return v


def prime_factors(num):
    #   prime_factors to be found
    factors = []
    # checks 2 as prime factor
    while num % 2 == 0:
        factors.append(2)
        num = num / 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num = num / i
    if num > 2:
        factors.append(int(num))
    return factors


def composite_num(num):
    # To check composite no or not
    if num <= 3:
        return False
    for i in range(4, ((num // 2) + 1)):
        if num % i == 0:
            return True
    return False


def total_digits(num):
    # returns total digits number
    poty = [int(n) for n in str(num)]
    return sum(poty)
