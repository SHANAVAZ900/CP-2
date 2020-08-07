# sameChars(s1, s2) [20 pts]
# Write the function sameChars(s1, s2) that takes two strings and returns True if the two strings are composed of
# the same characters (though perhaps in different numbers and in different orders) -- that is, if every character
# that is in the first string, is in the second, and vice versa -- and False otherwise. This test is
# case-sensitive, so "ABC" and "abc" do not contain the same characters. The function returns False if either
# parameter is not a string, but returns True if both strings are empty (why?).


def samechars(m):
    m1, m2 = m[0], m[1]
    if m1 == m2:
        return True
    if type(m1) == type(m2):
        k, l = sorted(list(set(m1))), sorted(list(set(m2)))
        if len(k) == len(k) and k == l:
            return True
    return False
