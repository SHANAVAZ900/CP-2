# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9
# that occurs most frequently in it, with ties going to the smaller digit.

import collections


def mostfrequentdigit(n):
    # your code goes here
    num = str(n)
    num_list = list(num)

    changes = [(item, count)
               for item, count in collections.Counter(num_list).most_common() if count == max(collections.Counter(num_list).values())]
    exord = min(changes)
    print(min(changes))
    if not changes:
        return int(num_list[0])
    else:
        return int(exord[0])
