# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic
# square.


def fixmostlymagicsquare(L):
    # Your code goes here
    row, diff = which_row(L)

    col, diff = which_col(L)

    L[row][col] += diff
    return L


def which_row(L):
    r = []
    for i in L:
        add = 0
        for j in i:
            add += j
        if add in rows:
            right = add
        rows.append(add)
    for i in range(len(rows)):
        if rows[i] != right:
            return i, right-rows[i]


def which_col(L):
    c = []
    for i in range(len(L)):
        add = 0
        for j in range(len(L)):
            add += L[j][i]
        if add in c:
            right = add
        c.append(add)
    for i in range(len(c)):
        if c[i] != right:
            return i, right-c[i]
