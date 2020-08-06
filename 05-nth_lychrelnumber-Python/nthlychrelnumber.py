# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def nthlychrelnumbers(n):
    # your code goes here
    c, v = 1, 196
    while c < n:
        v += 1
        if lychre_num(v):
            c += 1
    return v


def lychre_num(m):
    for i in range(255):
        m = m + int(str(m)[::-1])
        if m == int(str(m)[::-1]):
            return False
    return True
