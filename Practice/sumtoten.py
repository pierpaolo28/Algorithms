a = [3, 4, 1, 2, 9]


def sumtoten(arr):
    dic = {}
    for i in arr:
        if 10 - i in dic:
            return (10 - i, i)
        else:
            dic[i] = 1
    return "No two numbers in the array add up to 10"


print(sumtoten(a))