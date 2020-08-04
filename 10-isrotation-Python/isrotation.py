# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both
# guaranteed to not contain any 0's, and
# returns True if x is a rotation of the digits of y and False otherwise. For example,
# 3412 is a rotation of 1234. Any number
# is a rotation of itself.


def isrotation(x, y):
    s1, s2 = str(x), str(y)
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):

        if s1[i:] + s1[:i] == s2 or s1[len(s1) - i:] + s1[:len(s1) - i] == s2:
            return True
    return False
