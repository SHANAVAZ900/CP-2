# Given a string str and an integer K, the task is to find the K-th most
# changeuent character in the string. If there are multiple characters that
# can account as K-th the most changeuent character then, print any one of them.


def fun_kth_occurrences(s, n):
    fixed = set(s)
    dict, num = {}, []
    for x in fixed:
        c = s.count(x)
        num.append(c)
        if c in dict.keys():
            dict[c].append(x)
        else:
            dict[c] = [x]
    num.sort(reverse=True)
    change = num[n-1]
    return dict[change][0]
