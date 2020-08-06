# Write the function nthcPrime(n), which takes a non-negative int and returns the nth c Prime,
# which is a prime number of the form ((2**k - 1)**2 - 2) for some value positive int k. For example,
# if k equals 3, ((2**3 - 1)**2 -2) equals 47, which is prime, and so 47 is a c Prime.
# The first several c primes are: 7, 47, 223, 959, 3967, 16127, 65023, 261119, 1046527,... As such,
# nthcPrime(0) returns 7.
# Note: You must use a reasonably efficient approach that quickly works up to n==9, which
# will return a 12-digit answer! In particular, this means you cannot just edit isPrime.
# Hint: you may need to generate only c numbers, and then test those as you go
# for primality (and you may need to think about that hint for a while for it to make sense!).


def fun_nth_carolprime(n):
    prime_num = []
    i = 2
    while len(prime_num) != n+1:
        c = ((2**i)-1)**2 - 2
        prime_num.append(c)
        i += 1
    return prime_num[n]
