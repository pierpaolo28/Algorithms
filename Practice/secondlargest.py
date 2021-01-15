a = [2, 4, 5, 3, 1, 8]
b = [2]
c = []
d = [1, 3]


def second_largest1(arr):
    arr.sort()
    if (len(arr) == 0 or len(arr) == 1):
        return None
    else:
        return arr[len(arr) - 2]


def second_largest2(arr):
    largest, second_largest = None, None
    for i in arr:
        if largest == None:
            largest = i
        elif i > largest:
            second_largest = largest
            largest = i
        elif second_largest == None:
            second_largest = i
        elif i > second_largest:
            second_largest = i
    return second_largest


print(second_largest1(a))
print(second_largest2(a))