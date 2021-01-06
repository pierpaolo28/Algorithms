# 1. Write a recursive function that given an input n,
# sums all nonnegative integers up to n
def sol1(n):
    result = 0
    for i in range(n + 1):
        result += i
    return result


print(sol1(5))


def sol2(n):
    return int(n * (n + 1) / 2)


print(sol2(5))


def sol3(n):
    if n == 0:
        return 0
    else:
        return n + sol3(n - 1)


print(sol3(5))

# 2. Write a function that takes two inputs n and m and outputs the number of unique paths
# from the top left corner to the bottom right cornerof a n*m grid.
# Constraints: you can only move down or right 1 unit at the time.


def sol4(n, m):
    if n == 1 or m == 1:
        return 1
    else:
        return sol4(n - 1, m) + sol4(n, m - 1)


print(sol4(3, 3))

# 3. Write a function that counts the number of ways you can partition n objects
# using parts up to m (assuming m => 0)


def sol5(n, m):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    else:
        return sol5(n - m, m) + sol5(n, m - 1)


print(sol5(9, 5))