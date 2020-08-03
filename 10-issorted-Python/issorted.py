# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list
# is sorted (either smallest-first or largest-first) and False otherwise. Your function
# must only consider each value in the list once (so, in terms of big-oh, which we will
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort
# the list.


def issorted(a):
    # your code goes here
    if len(a) in [0, 1]:
        return True
    temp = True if a[0] >= a[1] else False
    res = a[0]
    for i in a[1:]:
        if (temp and res >= i) or (not temp and res <= i):
            res = i
        else:
            return False
    return True
