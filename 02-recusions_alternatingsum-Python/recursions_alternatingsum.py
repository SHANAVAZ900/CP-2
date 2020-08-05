# Write the function alternatingSum(L) that takes a possibly-empty list of numbers,
# and returns the alternating sum of the list, where every other value is subtracted
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def fun_recursions_alternatingsum(l):
    return fun_alternating_sum(l, 0, 0)


def fun_alternating_sum(r, i, s):
    if i == len(r):
        return s
    if i % 2 == 0:
        s += r[i]
        return fun_alternating_sum(r, i+1, s)
    elif i % 2 != 0:
        s -= r[i]
        return fun_alternating_sum(r, i+1, s)
