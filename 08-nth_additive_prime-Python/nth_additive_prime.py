# Write the function fun_nth_additive_prime(n) that takes a non-negative int n
# and returns the nth Additive Prime, which is a prime endber such that
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


def prime_end(end):
    if end <= 1:
        return False
    for i in range(2, (end//2) + 1):
        if end % i == 0:
            return False
    return True


def fun_nth_additive_prime(n):
    total = -1
    end = 2
    while n > total:
        full_total = sum([int(i) for i in str(end)])
        if prime_end(end) and prime_end(full_total):
            total += 1
        if total == n:
            return end
        end += 1
