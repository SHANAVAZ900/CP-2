# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number.
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46


def fun_nth_tidynumber(n):
    c, v = 0, 1
    while c < n:
        v += 1
        if tidy_num(v):
            c += 1
    return v


def tidy_num(m):
    val = str(m)
    for i in range(len(val) - 1):
        if int(val[i]) > int(val[i+1]):
            return False
    return True
