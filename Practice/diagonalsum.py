# Calculate the sum of the diagonal elements in a 2d array

ex = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ex = [[1, 0], [0, 1]]


def diagonal_sum(arr):
    res = 0
    for i in range(len(arr)):
        res += arr[i][i]
    return res


print(diagonal_sum(ex))
