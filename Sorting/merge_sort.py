import math


def merge_sort(inp):
    if len(inp) > 1:
        mid = math.floor(len(inp)/2)
        left = inp[:mid]
        right = inp[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                inp[k] = right[j]
                j += 1
            else:
                inp[k] = left[i]
                i += 1
            k += 1

        while j < len(right):
            inp[k] = right[j]
            j += 1
            k += 1

        while i < len(left):
            inp[k] = left[i]
            i += 1
            k += 1
    return inp


arr = [1, 5, 2, 87, 33, 21, 78]
print(arr)
print(merge_sort(arr))
