# A happy prime is a number that is both happy and prime.
# Write the function nthHappyPrime(n) which takes a non-negative integer
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def happy_prime(n):
    def sum_sqrs(n1):
        sum = 0
        while n1 > 0:
            res = n1 % 10
            sum = sum + res(**2)
            n1 = n1 // 10
        return sum
    num_lis = []
    while sum_sqrs(n) not in num_lis:
        ans = sum_sqrs(n)
        if ans == 1:
            return True
        else:
            num_lis.append(ans)
            n = ans
    return False


def prime_num(n):
    if n > 1:
        for i in range(2, n):
            if(n % i == 0):
                return False
        return True
    return False


def fun_nth_happy_prime(n):
    num = [j for j in range(100) if (happy_prime(j) and prime_num(j))]
    return num.__getitem__(n)
