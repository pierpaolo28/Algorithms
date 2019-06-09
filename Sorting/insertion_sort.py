# Sorting array in Ascending order
def insertion_sort(arr):
    # Starting by considering the second element in the array
    for j in range(2, len(arr), 1):
        # Storing the input value
        key = arr[j]
        i = j - 1
        # Compare the input value with the previous one
        while i >= 0 and arr[i] > key:
            # If the previous value is bigger than the input one swap their position
            arr[i+1] = arr[i]
            i = i - 1
        # otherwise do not swap their order
        arr[i + 1] = key
    return arr


# Sorting array in Descending order
def insertion_sort2(arr):
    for j in range(2, len(arr), 1):
        key = arr[j]
        i = j - 1
        # To order the array in descending order just change the check condition
        while i >= 0 and arr[i] < key:
            # If the previous value is less than the input one swap their position
            arr[i+1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr


list_sort = [9, 4, 23, 67, 133, 1, 8, 3]
print(insertion_sort(list_sort))

list_sort2 = [9, 4, 23, 67, 133, 1, 8, 3]
print(insertion_sort2(list_sort2))
