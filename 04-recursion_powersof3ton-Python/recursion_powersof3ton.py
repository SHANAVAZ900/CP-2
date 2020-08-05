# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem.
import math


def recursion_powersof3ton(n):
    # Your code goes here
    if n < 1:
        return None
    elif n == 1:
        return [1]
    return pow3(n, [])


def pow3(n, l):
    if n < 1:
        l.sort()
        return l
    n = int(n // 1)

    if math.isclose(3**int(math.log(n, 3)), n):
        l.append(n)
    return pow3(n - 1, l)
