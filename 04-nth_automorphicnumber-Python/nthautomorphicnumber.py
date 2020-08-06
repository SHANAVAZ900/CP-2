# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6,
# 76 and 890625 are all automorphic numbers.


def nthautomorphicnumbers(n):
    # Your code goes here
    c, v = 1, 0
    while c < n:
        v += 1
        if auto_morphic(v):
            c += 1
    return v


def auto_morphic(m):
    square = str(m ** 2)
    return m == int(square[len(square)-len(str(m)):])
