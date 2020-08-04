"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    # Your code goes here
    quick_sort(array, 0, len(array)-1)
    return array


def quick_sort(array, low, high):
    if low < high:
        sort_part = seperation(array, low, high)
        quick_sort(array, low, sort_part - 1)
        quick_sort(array, sort_part+1, high)


def seperation(array, low, high):
    pivot = array[low]
    start = low + 1
    end = high
    while True:
        while start <= end and array[start] <= pivot:
            start += 1
        while start <= end and array[end] >= pivot:
            end -= 1
        if start <= end:
            array[start], array[end] = array[end], array[start]
        else:
            break
    array[low], array[end] = array[end], array[low]
    return end
