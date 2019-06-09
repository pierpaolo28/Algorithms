# Explanation: https://www.youtube.com/watch?v=CB_NCoxzQnk

import math


# The objective is to find a pivot able to split a list in half
# In this example a chose to use the median of the first, last and center items
# in the list as pivot
def find_pivot(inp, low, high):
    med = math.floor((high + low)/2)
    new_pivot = high
    if inp[low] < inp[med]:
        if inp[med] < inp[high]:
            new_pivot = med
    elif inp[low] < inp[high]:
        new_pivot = low
    return new_pivot


# Dividing the list in two partitions (there are determined by the border position)
# The elements smaller than the pivot should be at its left and the elements bigger
# to its right.
def partition(inp, low, high):
    pivot_index = find_pivot(inp, low, high)
    pivot_value = inp[pivot_index]
    inp[pivot_index], inp[low] = inp[low], inp[pivot_index]
    border = low

    for i in range(low, high+1):
        if inp[i] < pivot_value:
            border += 1
            inp[i], inp[border] = inp[border], inp[i]
        inp[low], inp[border] = inp[border], inp[low]
    return border


# Identify first the partition and then sort them iteratively to sort the list (dived and conquer
# approach)
def quick_sort(inp, low, high):
    if low < high:
        pivot = partition(inp, low, high)
        quick_sort(inp, low, pivot-1)
        quick_sort(inp, pivot+1, high)
    return inp


arr = [3, 6, 2, 23, 11, 453, 1]
print(arr)
print(quick_sort(arr, 0, len(arr)-1))
