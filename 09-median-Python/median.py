# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value,
# which is the value of the middle element, or the average of the two middle elements if there is no single middle
# element. If the list is empty, return None.


def median(a):
    # your code goes here
    if not a:
        return None
    l = len(a)
    if l % 2 == 0:
        module = (a[l//2] + a[(l//2)-1])/2
    else:
        module = a[l//2]
    return module
