import numpy as np


def world(n, m):
    grid = np.chararray((n, m))
    grid = [['-' for j in i] for i in grid]
    return grid


def move_up(w, player):
    if player[0] > 0:
        if w[player[0] - 1][player[1]] != '%':
            a = w[player[0] - 1][player[1]]
            w[player[0] - 1][player[1]] = w[player[0]][player[1]]
            w[player[0]][player[1]] = a
            player[0] = player[0] - 1
            return w, player
        else:
            return 0, 1
    else:
        return 0, 1


def move_down(w, player):
    if player[0] < len(w) - 1:
        if w[player[0] + 1][player[1]] != '%':
            a = w[player[0] + 1][player[1]]
            w[player[0] + 1][player[1]] = w[player[0]][player[1]]
            w[player[0]][player[1]] = a
            player[0] = player[0] + 1
            return w, player
        else:
            return 0, 1
    else:
        return 0, 1


def move_left(w, player):
    if player[1] > 0:
        if w[player[0]][player[1] - 1] != '%':
            a = w[player[0]][player[1] - 1]
            w[player[0]][player[1] - 1] = w[player[0]][player[1]]
            w[player[0]][player[1]] = a
            player[1] = player[1] - 1
            return w, player
        else:
            return 0, 1
    else:
        return 0, 1


def move_right(w, player):
    if player[1] < len(w) - 1:
        if w[player[0]][player[1] + 1] != '%':
            a = w[player[0]][player[1] + 1]
            w[player[0]][player[1] + 1] = w[player[0]][player[1]]
            w[player[0]][player[1]] = a
            player[1] = player[1] + 1
            return w, player
        else:
            return 0, 1
    else:
        return 0, 1


def solution_check(w, sol):
    h = [k for i, j in zip(w, sol) for k, z in zip(i, j) if k != z]
    return len(h)
