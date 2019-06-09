import math


def merge_sort(inp):
    # If the length of the input array is less than two, no need to
    # sort array
    if len(inp) > 1:
        # Finding the center of the array
        mid = math.floor(len(inp)/2)
        # The array elements are divided in two halves
        left = inp[:mid]
        right = inp[mid:]

        # Sorting the first half
        merge_sort(left)
        # Sorting the second half
        merge_sort(right)

        i, j, k = 0, 0, 0

        # Store the sorted mini arrays in the final array
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                inp[k] = right[j]
                j += 1
            else:
                inp[k] = left[i]
                i += 1
            k += 1

        # Checking to see if there is any array value left
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
