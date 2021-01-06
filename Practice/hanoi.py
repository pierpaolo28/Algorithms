# Write a function hanoi(n, start, end) that
# outputs a sequence of steps to move n disks
# from the start rod to the end rod (Hanoi problem)
# Assumptions:
# 1 <= start <= 3
# 1 <= end <= 3
# start != end
# n => 1


def hanoi(n, start, end):
    # Print the list of steps required to move
    # n disks from the start rod to the end rod
    # hanoi(2, 1, 3)
    # 1 -> 2
    # 1 -> 3
    # 2 -> 3
    if n == 1:
        print(start, '->', end)
    else:
        other = 6 - (start + end)
        hanoi(n - 1, start, other)
        print(start, '->', end)
        hanoi(n - 1, other, end)


hanoi(2, 1, 3)