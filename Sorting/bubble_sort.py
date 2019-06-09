def bubble_sort(inp):
    for i in range(len(inp)):
        for j in range(len(inp)-i-1):
            if inp[j] > inp[j+1]:
                inp[j], inp[j+1] = inp[j+1], inp[j]
    return inp


arr = [33, 55, 2, 7, 1, 1, 6778]
print(arr)
print(bubble_sort(arr))
