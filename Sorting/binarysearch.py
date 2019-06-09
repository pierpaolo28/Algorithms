import math


# This binary search can only be efficient assuming the input array is sorted (otherwise not ordered values index
# is wrong)
def binary_search(inp, low, high, num):
    # If high < low, the element you are looking for can't be found
    if high >= low:
        # Calculating the median value of the list
        med = low + math.floor((high-low)/2)
        # If the number we are looking for is in the median, return the result
        if inp[med] == num:
            return med, inp[med]
        # If the number we are looking for is greater than the median, look in the right hand half of the
        # list
        elif inp[med] < num:
            return binary_search(inp, med + 1, high, num)
        # If the number we are looking for is lower tha the median, look at the left hand side of the list
        elif inp[med] > num:
            return binary_search(inp, low, med - 1, num)
    # If the requested number can' be found return -1
    else:
        return -1


arr = [1, 2, 5, 7, 11, 18, 56, 83]
print(arr)
print("18 is the number we are looking for")
print("Index location in array of the number and it's value =", binary_search(arr, 0, len(arr)-1, 18))
