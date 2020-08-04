# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both
# guaranteed to not contain any 0's, and
# returns True if x is a rotation of the digits of y and False otherwise. For example,
# 3412 is a rotation of 1234. Any number
# is a rotation of itself.


def isrotation(x, y):
    # Your code goes here
    first, last = str(x), str(y)
    if len(first) != len(last):
        return False
    for i in range(len(first)):
        if first[i:] + first[:i] == last or first[len(first) - i:] + first[:len(first) - i] == last:
            return True
    return False
