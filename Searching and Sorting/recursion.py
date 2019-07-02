def get_fib(position):
    if position <=1:
        return position
    res = get_fib(position -1) + get_fib(position -2)
    return res


# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)