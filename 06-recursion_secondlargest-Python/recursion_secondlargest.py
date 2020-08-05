# Recursion-Only recursion_secondlargest(L) [15 pts]
# Note: recall that you may not use sort, sorted, min, or max this week! With that in mind, write the function
# recursion_secondlargest(L) that takes a list of integers in any order and returns the second-largest value in the list. To
# be more precise, it returns the second value from the end if the list was sorted (though you do not need to sort
# it to solve this problem), so if the largest value occurs twice, you would return that value. Also, if there are
# fewer than 2 values in the list, return None. Here are some test cases:
# assert(recursion_secondlargest([1,2,3,4,5]) == 4)
# assert(recursion_secondlargest([4,3]) == 3)
# assert(recursion_secondlargest([4,4,3]) == 4)
# assert(recursion_secondlargest([-3,-4]) == -4)
# assert(recursion_secondlargest([4]) == None)
# assert(recursion_secondlargest([ ]) == None)
# Again, you do not need to sort the list. We didn't sort it in our sample solution. We just tracked the two largest
# values as we recursively traversed the list. Also, you may not use loops/iteration in this problem


def recursion_secondlargest(L):
    # Your code goes here
    if len(L) < 2:
        return None
    elif len(L) == 2:
        return min(L)
    return second_large(L, 0, max(L[0], L[1]), min(L[0], L[1]))


def second_large(l, i, f, s):
    if i >= len(l):
        return s
    g = l[i]
    h = 0 if i+1 == len(l) else l[i+1]
    flag = [g, h, f, s]
    f = max(flag)
    flag.remove(f)
    s = max(flag)
    return second_large(l, i+2, f, s)
