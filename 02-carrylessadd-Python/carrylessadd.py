# carry less addition means a  normal addition with the carry from each column ignored.
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
    s1, s2 = str(x)[::-1], str(y)[::-1]
    low, high = min(s1, s2), max(s1, s2)
    res = ''
    for i in range(len(low)):
        res += str(int(low[i])+int(high[i]))[-1]
    if i < len(high):
        res += high[i+1:]
    return int(res[::-1])
