def selection_sort(inp):
    min_val = 0
    # loop through array
    for i in range(len(inp)):
        for j in range(i+1, len(inp)):
            # find the minimum number in the array
            if inp[min_val] > inp[j]:
                min_val = j
        # Put the current minimum value in the right position of sorted array
        inp[min_val], inp[i] = inp[i], inp[min_val]
    return inp


arr = [34, 22, 11, 1, 34, 35, 12]
print(selection_sort(arr))
