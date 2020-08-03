# Write the function nthHappyNumber(n) which takes a non-negative integer
# and returns the nth happy number (where the 0th happy number is 1).
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)


def happynum(k):
    def sum_square(k1):
        sum = 0
        while k1 > 0:
            res = k1 % 10
            sum = sum + (res**2)
            k1 = k1 // 10
        return sum
    num_list = []
    while sum_square(k) not in num_list:
        add = sum_square(k)
        if add == 1:
            return True
        else:
            num_list.append(add)
            k = add
    return False


def fun_nth_happy_number(n):
    num = [i for i in range(100) if happynum(i)]
    return num[n]
