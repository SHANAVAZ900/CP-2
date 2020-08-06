# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth
# Circular prime, which is a prime number that does not contain any 0's and such that all the
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3,
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime,
# note that 197 is prime, as is 971 (circular_primed left), as is 719 (circular_primed left again).


def nthcircularprime(n):
    # Your code goes here
    l = 1
    total = 1
    while (total <= n):
        if prime(l):
            c = 1
            k = l
            for j in range(len(str(l))-1):
                k = circular_prime(k)
                if prime(k) and k != l:
                    c += 1
            if c == len(str(l)):
                total += 1
        l += 1
    return l-1


def prime(m):

    if (m <= 1):
        return False
    if (m <= 3):
        return True

    if (m % 2 == 0 or m % 3 == 0):
        return False

    j = 5
    while(j * j <= m):
        if (m % j == 0 or m % (j + 2) == 0):
            return False
        j = j + 6

    return True


def circular_prime(m):
    m = str(m)
    m = m[-1]+m[:len(m)-1]
    return int(m)
