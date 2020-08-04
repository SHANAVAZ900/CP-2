# Pool balls are arranged in balls where the first row contains 1 pool ball and each row contains 1
# more pool ball than the previous row.
# numberOfPoolBallRows(balls) that takes a non-negative int number of pool balls, and returns the
# smallest int number of balls required for the given number of pool balls. Thus, numberOfPoolBallRows(6)
# returns 3. Note that if any balls must be in a row, then you count that row, and so
# numberOfPoolBallRows(7) returns 4 (since the 4th row must have a single ball in it).


def fun_numberofpoolballrows(balls):
    if balls == 1:
        return 1
    num, res, add, = 1, 1, 1
    while True:
        num += 1
        if add + res + 1 < balls:
            res += 1
            add += res
        else:
            break
    return num
