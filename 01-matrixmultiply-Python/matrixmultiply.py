# Write the function matrixMultiply(m1, m2) that takes two 2d lists
# (that we will consider to be matrices) and returns a new 2d list that
# is the result of multiplying the two matrices. Return None if the
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    l1, l2 = len(m1), len(m1[0])
    s1, s2 = len(m2), len(m2[0])
    if l2 != s1:
        return None
    ans = [[0] * s2 for l in range(l1)]
    for i in range(l1):
        for j in range(s2):
            for k in range(s1):
                ans[i][j] += m1[i][k] * m2[k][j]
    return ans
