# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n
# and returns the nth palindromic Prime, which is a palidrome endber such that
# it is also a prime. For example, 313 is a palindrome and it is prime
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2


def prime_num(end):

    if end <= 1:
        return False
    for i in range(2, (end // 2) + 1):
        if end % i == 0:
            return False
    return True


def fun_nth_palindromic_prime(n):
    total = -1
    end = 2
    while n > total:

        if str(end) == str(end)[::-1] and prime_num(end):
            total += 1
        if total == n:
            return end
        end += 1
