# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.


import math


def distane(x1, y1, x2, y2):
    dist = math.sqrt(((x2-x1)**2+(y2-y1)**2))
    return dist


def isrighttriangle(x1, y1, x2, y2, x3, y3):
    # your code goes here
    x = distane(x1, y1, x2, y2)
    y = distane(x1, y1, x3, y3)
    z = distane(x2, y2, x3, y3)
    high = max(x, y, z)
    if high == x and math.isclose(x**2, (y**2+z**2)):
        return True
    elif high == y and math.isclose(y**2, (z**2+x**2)):
        return True
    elif high == z and math.isclose(z**2, (y**2+x**2)):
        return True
    return False
