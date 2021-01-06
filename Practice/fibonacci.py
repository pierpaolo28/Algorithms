# As n increases by 1, the number of times f() is called doubles roughly by 2.
# The running time is exponential: O(2^N)
def f(n):
    if n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 1)


print(f(3))