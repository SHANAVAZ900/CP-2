# Write the function hasnoprimes(L) that takes a 2d list L of integers,
# and returns True if L does not contain any primes, and False otherwise.


def prime_num(num):
    if num <= 1:
        return False
    for i in range(2, ((num // 2) + 1)):
        if num % i == 0:
            return False
    return True


def fun_hasnoprimes(l):
    for i in l:
        for j in i:
            if prime_num(j):
                return False
    return True
