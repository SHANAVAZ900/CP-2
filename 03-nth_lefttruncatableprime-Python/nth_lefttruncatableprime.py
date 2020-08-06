# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0
# and which remains prime when the leading (left) digit is successively removed.
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime.
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarmber(n)rns 2, and
# nthLeftTruncatablePrime(10) returns 53.


#import math

def fun_nth_lefttruncatableprime(n):
    c, v = 0, 2
    while c < n:
        v += 1
        if prime_trunc(v):
            c += 1
    return v


def prime_trunc(m):
    val = str(m)[::-1]
    if '0' in val:
        return False
    for i in range(len(val)):
        x = int(val[: i + 1][::-1])
        # if not prime, then False
        if not prime_num(x):
            return False
    return True


def prime_num(m):
    if m <= 1:
        return False
    for i in range(2, ((m // 2) + 1)):
        if m % i == 0:
            return False
    return True
