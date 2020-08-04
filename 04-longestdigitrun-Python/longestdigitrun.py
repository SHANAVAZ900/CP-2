# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns
# the digit that has the longest consecutive
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's),
# as does longestDigitRun(-677886).


def longestdigitrun(n):
    # Your code goes here
    s1 = str(abs(n))
    first, last, high, j, calc = 0, 0, 0, 0, 0
    while last < len(s1):
        while last < len(s1) and s1[first] == s1[last]:
            last += 1
        if last - first > calc:
            high = s1[first]
            calc = last - first
        elif last - first == calc:
            high = min(high, s1[first])
        if last == len(s1):
            break
        first = last
    return int(high)
