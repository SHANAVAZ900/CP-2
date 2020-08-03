# A happy prime is a number that is both happy and prime.
# Write the function nthHappyPrime(n) which takes a non-negative integer
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def ishappynumber(n):
    def sumofsquares(n1):
        sum = 0
        while n1 > 0:
            rem = n1 % 10
            sum = sum + (rem**2)
            n1 = n1 // 10
        return sum
    list = []
    while sumofsquares(n) not in list:
        result = sumofsquares(n)
        if result == 1:
            return True
        else:
            list.append(result)
            n = result
    return False


def isprime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i == 0):
                return False
        return True
    return False


def fun_nth_happy_prime(n):
    li = [i for i in range(100) if (ishappynumber(i) and isprime(i))]
    return li.__getitem__(n)
