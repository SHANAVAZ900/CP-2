# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"


def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    if s1 == "" or s2 == "":
        return ""
    c, m = "", 0
    low, high = min(s1, s2), max(s1, s2)
    for i in range(len(low)):
        k = len(low)-1
        while k >= 1:
            val = low[i:k + 1]
            if val in high and len(val) > m:
                c = ""+val
                m = len(val)
            elif val in high and len(val) == m:
                c = min(c, val)
            k -= 1
    return "" if len(c) == 0 else c
