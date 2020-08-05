# Without using iteration and without using strings,
# write the recursive function onlyEvenDigits(L),
# that takes a list L of non-negative integers
# (you may assume that), and returns a new list of
# the same numbers only without their odd digits
# (if that leaves no digits, then replace the number with 0).
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844].
# Also the function returns the empty list if the original list is empty.
# Remember to not use strings. You may not use loops/iteration in this problem.


def fun_recursion_onlyevendigits(l):
    return even(l, 0)


def even(l, i):
    if i == len(l):
        return l
    flag, flag1, flag2 = l[i], 0, 0
    while flag > 0:
        s = flag % 10
        if s % 2 == 0:
            flag2 += s * (10 ** flag1)
            flag1 += 1
        flag = flag // 10
    l[i] = flag2
    return even(l, i+1)
