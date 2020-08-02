# Write the function getKthDigit(n, k) that takes
# a possibly-negative int n and a non-negative int k,
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0


def fun_get_kth_digit(digit, k):

    if digit > 0:
        p = str(digit)
        if k < p.__len__():
            return int(p[p.__len__() - k - 1])
        else:
            return 0
    else:
        k1 = -1 * digit
        k1 = str(k1)
        if(k < k1.__len__()):
            return int(k1[len(k1) - k-1])
        return 0
