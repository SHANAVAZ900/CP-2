# Write the function interleave(s1, s2) that takes two strings, s1 and s2,
# and interleaves their characters starting with the first character in s1.
# For example, interleave('pto', 'yhn') would return the string "python".
# If one string is longer than the other, concatenate the rest of the remaining
# string onto the end of the new string. For example ('a#', 'cD!f2') would return
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.


def fun_interleave(s1, s2):
    low_sting, hig_sting = s1, s2

    if len(s2) < len(s1):
        low_sting, hig_sting = s2, s1
    ans = []
    j = 0

    for j in range(len(low_sting)):
        ans.append(s1[j] + s2[j])
    ans.append(hig_sting[j+1:])
    return "".join(ans)
