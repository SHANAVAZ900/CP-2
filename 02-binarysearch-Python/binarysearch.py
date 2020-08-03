"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    # Your code goes here
    last = 0
    top = len(input_array)
    while last <= top:
        bottom = (last + top) // 2
        if value > input_array[bottom]:
            last = bottom + 1
        elif value < input_array[bottom]:
            top = bottom - 1
        else:
            return bottom
    return -1
