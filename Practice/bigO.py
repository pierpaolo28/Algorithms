# a + b + c = n
# Find all sets of nonnegative integers (a, b, c) that sum to an integer n (n>=0)


# Time complexity: O(n^3)
def simple_sol(n):
    solutions = 0
    for a in range(n + 1):
        for b in range(n + 1):
            for c in range(n + 1):
                if a + b + c == n:
                    solutions += 1
                    #print(a, b, c)
    return solutions


# Time complexity: O(n^2)
def better_sol(n):
    solutions = 0
    for a in range(n + 1):
        for b in range(n + 1):
            c = n - (a + b)
            if c >= 0:
                solutions += 1
    return solutions


print(simple_sol(22))
print(simple_sol(2))
print(better_sol(22))
print(better_sol(2))