# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g.
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
    # Your code goes here
    ans = 0
    while ans < len(str1):
        if str1[ans:] + str1[:ans] == (str2) or (str1[len(str1)-ans:]+str1[:len(str1)-ans]) == str2:
            return True
        ans += 1
    return False
