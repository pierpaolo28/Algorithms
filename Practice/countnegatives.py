# Count the number of negative numbers in a 2D list (both rows and columns are already sorted)

a = [[-4, -3, -1, 0], [-2, -2, 1, 2], [-1, 1, 2, 3], [1, 2, 4, 5]]
a = [[-1, 0], [0, 0]]
a = [[-2, 0], [-1, 0]]


def countnegatives(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] < 0:
                res += 1
            else:
                break
    return res


def countnegatives2(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if (arr[i][len(arr) - j - i] > -1
                    and arr[i][len(arr) - j - 1 - i] <= -1):
                count += len(arr) - j - i
                break
    return count


print(countnegatives2(a))