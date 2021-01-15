ex = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]]
ex = [[1, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0]]
ex = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0]]


def rooks_are_safe(arr):
    for i in range(len(arr)):
        if sum(arr[i]) > 1:
            return False
        else:
            for j in range(len(arr[i])):
                if sum([row[j] for row in arr]) > 1:
                    return False
    return True


print(rooks_are_safe(ex))
