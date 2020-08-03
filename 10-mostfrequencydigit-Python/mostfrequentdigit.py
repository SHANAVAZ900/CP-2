# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9
# that occurs most frequently in it, with ties going to the smaller digit.


def mostfrequentdigit(n):
    # your code goes here
    n = str(n)
    high_count = 0
    high = 0
    for i in n:
        if n.count(i) > high_count:
            high = int(i)
            high_count += 1
        if n.count(i) == high_count:
            high = min(high_count, int(i))
    return high
