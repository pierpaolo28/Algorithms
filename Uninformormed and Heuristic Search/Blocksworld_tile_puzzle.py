import pprint
import random
import numpy as np
from Foundations import world, move_up, move_down, move_left, move_right, solution_check
from IPython.display import clear_output
from collections import deque
import time
from operator import attrgetter
import copy

start = time.time()


class Space:
    def __init__(self, m, n, obstacles=False):
        self.m = m
        self.n = n

        grid = world(self.n, self.m)

        if obstacles is False:
            # Final Grid
            grid[self.n - 1][self.m - 2] = 'C'
            grid[self.n - 1][self.m - 3] = 'B'
            grid[self.n - 1][self.m - 4] = 'A'
            grid[self.n - 1][self.m - 1] = 'x'
            self.player = [self.n - 1, self.m - 1]
            # Simple Grid
            # grid[self.n - 1][self.m - 3] = 'C'
            # grid[self.n - 2][self.m - 3] = 'B'
            # grid[self.n - 3][self.m - 2] = 'A'
            # grid[self.n - 1][self.m - 2] = 'x'
            # self.player = [self.n - 1, self.m - 2]
        else:
            # Obstacles Grid Simple
            # grid[self.n - 1][self.m - 3] = 'C'
            # grid[self.n - 2][self.m - 3] = 'B'
            # grid[self.n - 3][self.m - 2] = 'A'
            # Obstacle grid Final
            grid[self.n - 1][self.m - 2] = 'C'
            grid[self.n - 1][self.m - 3] = 'B'
            grid[self.n - 1][self.m - 4] = 'A'

            grid[self.n - 4][self.m - 1] = '%'
            grid[self.n - 2][self.m - 2] = '%'
            grid[self.n - 1][self.m - 1] = 'x'
            self.player = [self.n - 1, self.m - 1]

        self.w = grid

    def solution(self):
        grid = world(self.n, self.m)

        grid[self.n - 1][self.m - 3] = 'C'
        grid[self.n - 2][self.m - 3] = 'B'
        grid[self.n - 3][self.m - 3] = 'A'
        return grid


# Used for Bilateral Search
class Space2:
    def __init__(self, m, n, obstacles=False):
        self.m = m
        self.n = n

        grid = world(self.n, self.m)

        if obstacles is False:
            # Final Grid
            grid[self.n - 1][self.m - 3] = 'C'
            grid[self.n - 2][self.m - 3] = 'B'
            grid[self.n - 3][self.m - 3] = 'A'
            grid[self.n - 2][self.m - 2] = 'x'
            self.player = [self.n - 2, self.m - 2]
        else:
            # Obstacles Grid
            grid[self.n - 1][self.m - 3] = 'C'
            grid[self.n - 2][self.m - 3] = 'B'
            grid[self.n - 3][self.m - 3] = 'A'
            grid[self.n - 4][self.m - 1] = '%'
            grid[self.n - 2][self.m - 2] = '%'
            grid[self.n - 3][self.m - 2] = 'x'
            self.player = [self.n - 3, self.m - 2]

        self.w = grid


class Game(Space):
    def __init__(self, m, n, obstacles=False):
        super().__init__(m, n, obstacles)

    def __repr__(self):
        game = True
        pprint.pprint(self.w)
        clear_output(wait=True)
        while game is True:
            val = input("Choose Direction: ")
            if val == 'a':
                clear_output(wait=True)
                check1, check2 = move_left(self.w, self.player)
                if check1 != 0:
                    self.w, self.player = check1, check2
                    pprint.pprint(self.w)
                else:
                    print("Invalid move, try again")
            elif val == 'd':
                clear_output(wait=True)
                check1, check2 = move_right(self.w, self.player)
                if check1 != 0:
                    self.w, self.player = check1, check2
                    pprint.pprint(self.w)
                else:
                    print("Invalid move, try again")
            elif val == 'w':
                clear_output(wait=True)
                check1, check2 = move_up(self.w, self.player)
                if check1 != 0:
                    self.w, self.player = check1, check2
                    pprint.pprint(self.w)
                else:
                    print("Invalid move, try again")
            elif val == 'z':
                clear_output(wait=True)
                check1, check2 = move_down(self.w, self.player)
                if check1 != 0:
                    self.w, self.player = check1, check2
                    pprint.pprint(self.w)
                else:
                    print("Invalid move, try again")
            elif val == 'e':
                game = False
                return ('End of the game!')
            else:
                print('Wrong Entry')


# play = Game(4, 4)
# print(play)


class MakeNode:
    def __init__(self, state, parent, action, path_depth, estimated_cost):
        self.state = state
        self.parent = parent
        self.path_depth = path_depth
        self.action = action
        self.estimated_cost = estimated_cost


def heuristic(world, sol, depth):
    w = [item for sublist in world for item in sublist]
    s = [item for sublist in sol for item in sublist]
    manhattan = 0
    manhattan += abs(w.index('A') - s.index('A')) + abs(w.index('B') - s.index('B')) + abs(w.index('C') - s.index('C'))
    return manhattan + depth


def expand_node(problem, node, mode, sol, visited=0):
    if mode == 3:
        up = MakeNode(move_up([x[:] for x in problem.w], [x for x in problem.player]), node.parent + problem.w,
                         node.action + ', Up', node.path_depth + 1,
                         heuristic(problem.w, sol, node.path_depth))
        down = MakeNode(move_down([x[:] for x in problem.w], [x for x in problem.player]), node.parent + problem.w,
                         node.action + ', Down', node.path_depth + 1,
                         heuristic(problem.w, sol, node.path_depth))
        left = MakeNode(move_left([x[:] for x in problem.w], [x for x in problem.player]), node.parent + problem.w,
                         node.action + ', Left', node.path_depth + 1,
                         heuristic(problem.w, sol, node.path_depth))
        right = MakeNode(move_right([x[:] for x in problem.w], [x for x in problem.player]), node.parent + problem.w,
                         node.action + ', Right', node.path_depth + 1,
                         heuristic(problem.w, sol, node.path_depth))
        res = [node for node in [up, left, down, right] if node.state[0] != 0]
        if visited != 0:
            res = [i for i in res if i.state[0] not in visited]
        return res
    else:
        up = MakeNode(move_up([x[:] for x in problem.w], [x for x in problem.player]), node.parent + problem.w,
                        node.action + ', Up', node.path_depth + 1, node.estimated_cost + 1)
        down = MakeNode(move_down([x[:] for x in problem.w], [x for x in problem.player]), node.parent + problem.w,
                          node.action + ', Down', node.path_depth + 1, node.estimated_cost + 1)
        left = MakeNode(move_left([x[:] for x in problem.w], [x for x in problem.player]), node.parent + problem.w,
                          node.action + ', Left', node.path_depth + 1, node.estimated_cost + 1)
        right = MakeNode(move_right([x[:] for x in problem.w], [x for x in problem.player]), node.parent + problem.w,
                           node.action + ', Right', node.path_depth + 1, node.estimated_cost + 1)
        res = [node for node in [up, left, down, right] if node.state[0] != 0]
        if mode == 0:
            return res
        elif mode == 1:
            res = random.sample(res, len(res))
            return res
        elif mode == 4:
            res = [i for i in res if i.state[0] not in visited]
            return res


def search(problem, mode, depth=np.inf, obstacles=False):
    computational_time = 0
    gen = []
    sol = [x[:] for x in problem.solution()]
    if mode == 3:
        fringe = [MakeNode([problem.w, problem.player], [0], 'Root', 0, heuristic(problem.w, sol, 0))]
    else:
        fringe = deque([MakeNode([problem.w, problem.player], [0], 'Root', 0, 0)])
    diff = solution_check(problem.w, sol)
    if ((diff == 1) and (obstacles is False)) or ((diff == 3) and (obstacles is True)):
        return 0, computational_time, None, None, None
    elif mode == 0:
        while True:
            if len(fringe) == 0:
                return np.inf, computational_time, None, None, None
            else:
                node = fringe.popleft()
                problem.w, problem.player = node.state[0], node.state[1]
                computational_time += 1
            diff = solution_check(node.state[0], sol)
            if ((diff == 1) and (obstacles is False)) or ((diff == 3) and (obstacles is True)):
                print("Nodes Generated (Space Complexity:", sum(gen), ")")
                return node.path_depth, computational_time, node.action, node.parent + node.state[0], node.estimated_cost
            else:
                new = expand_node(problem, node, 0, sol)
                fringe.extend(new)
                gen.append(len(new))
                if (computational_time % 50000) == 0:
                    print('Time:', computational_time)
    elif mode == 1:
        while True:
            if len(fringe) == 0:
                return np.inf, computational_time, None, None, None
            else:
                node = fringe.pop()
                problem.w, problem.player = node.state[0], node.state[1]
                computational_time += 1
            diff = solution_check(node.state[0], sol)
            if ((diff == 1) and (obstacles is False)) or ((diff == 3) and (obstacles is True)):
                print("Nodes Generated (Space Complexity:", sum(gen), ")")
                return node.path_depth, computational_time, node.action, node.parent + node.state[0], node.estimated_cost
            else:
                if node.path_depth < depth:
                    if depth == np.inf:
                        new = expand_node(problem, node, 1, sol)
                        fringe.extend(new)
                        gen.append(len(new))
                    else:
                        new = expand_node(problem, node, 0, sol)
                        fringe.extend(new)
                        gen.append(len(new))
                    if (computational_time % 50000) == 0:
                        print('Time:', computational_time)
    elif mode == 2:
        iteration = 0
        r = copy.deepcopy(problem)
        for i in range(depth):
            print("Depth: ", i)
            depth, complexity, moves, history, cost = search(copy.deepcopy(r), 1, i)
            iteration += complexity
            if moves is not None:
                return depth, iteration, moves, history, cost
        return 1, computational_time, None, None, None
    elif mode == 3:
        while True:
            if len(fringe) == 0:
                return np.inf, computational_time, None, None, None
            else:
                fringe.sort(key=attrgetter('estimated_cost'))
                node = fringe.pop(0)
                problem.w, problem.player = node.state[0], node.state[1]
                computational_time += 1
            diff = solution_check(node.state[0], sol)
            if ((diff == 1) and (obstacles is False)) or ((diff == 3) and (obstacles is True)):
                print("Nodes Generated (Space Complexity:", sum(gen), ")")
                return node.path_depth, computational_time, node.action, node.parent + node.state[0], node.estimated_cost
            else:
                new = expand_node(problem, node, mode, sol)
                fringe.extend(new)
                gen.append(len(new))
                if (computational_time % 50000) == 0:
                    print('Time:', computational_time)
    else:
        print("Select an adequate mode: \n")
        print(" 0: Breadth First Search \n 1: Depth First Search or Limited Depth Search \n "
              "2: Iterative Deepening \n 3: A Star \n")
        return None, None, None, None, None


def graph_search(problem, mode, depth=np.inf, obstacles=False):
    computational_time = 0
    gen = []
    sol = [x[:] for x in problem.solution()]
    if mode == 3:
        fringe = [MakeNode([problem.w, problem.player], [0], 'Root', 0, heuristic(problem.w, sol, 0))]
        visited = [problem.w]
    else:
        fringe = deque([MakeNode([problem.w, problem.player], [0], 'Root', 0, 0)])
        visited = [problem.w]
    diff = solution_check(problem.w, sol)
    if ((diff == 1) and (obstacles is False)) or ((diff == 3) and (obstacles is True)):
        return 0, computational_time, None, None, None
    elif mode == 0:
        while True:
            if len(fringe) == 0:
                return np.inf, computational_time, None, None, None
            else:
                node = fringe.popleft()
                problem.w, problem.player = node.state[0], node.state[1]
                computational_time += 1
            diff = solution_check(node.state[0], sol)
            if ((diff == 1) and (obstacles is False)) or ((diff == 3) and (obstacles is True)):
                print("Nodes Generated (Space Complexity:", sum(gen), ")")
                return node.path_depth, computational_time, node.action, node.parent + node.state[0], node.estimated_cost
            else:
                new = expand_node(problem, node, 4, sol, visited)
                fringe.extend(new)
                gen.append(len(new))
                visited.extend([i.state[0] for i in new])
                if (computational_time % 50000) == 0:
                    print('Time:', computational_time)
            # new = expand_node(problem, node, 4, sol, visited)
            # fringe.extend(new)
            # gen.append(len(new))
            # visited.extend([i.state[0] for i in new])
            # for i in new:
            #     diff = solution_check(i.state[0], sol)
            #     if ((diff == 1) and (obstacles is False)) or ((diff == 3) and (obstacles is True)):
            #         print("Nodes Generated (Space Complexity:", sum(gen), ")")
            #         return node.path_depth, computational_time, node.action, node.parent + node.state[0], node.estimated_cost
            # if (computational_time % 50000) == 0:
            #     print('Time:', computational_time)
    elif mode == 1:
        while True:
            if len(fringe) == 0:
                return np.inf, computational_time, None, None, None
            else:
                node = fringe.pop()
                problem.w, problem.player = node.state[0], node.state[1]
                computational_time += 1
            diff = solution_check(node.state[0], sol)
            if ((diff == 1) and (obstacles is False)) or ((diff == 3) and (obstacles is True)):
                print("Nodes Generated (Space Complexity:", sum(gen), ")")
                return node.path_depth, computational_time, node.action, node.parent + node.state[0], node.estimated_cost
            else:
                if node.path_depth < depth:
                    new = expand_node(problem, node, 4, sol, visited)
                    fringe.extend(new)
                    gen.append(len(new))
                    visited.extend([i.state[0] for i in new])
                    if (computational_time % 50000) == 0:
                        print('Time:', computational_time)
    elif mode == 2:
        iteration = 0
        r = copy.deepcopy(problem)
        for i in range(depth):
            print("Depth: ", i)    # When using obstacles remember to add uncommented code!
            depth, complexity, moves, history, cost = graph_search(copy.deepcopy(r), 1, i) # , obstacles=True
            iteration += complexity
            if moves is not None:
                return i, iteration, moves, history, cost
        return 1, computational_time, None, None, None
    elif mode == 3:
        while True:
            if len(fringe) == 0:
                return np.inf, computational_time, None, None, None
            else:
                fringe.sort(key=attrgetter('estimated_cost'))
                node = fringe.pop(0)
                problem.w, problem.player = node.state[0], node.state[1]
                computational_time += 1
            diff = solution_check(node.state[0], sol)
            if ((diff == 1) and (obstacles is False)) or ((diff == 3) and (obstacles is True)):
                print("Nodes Generated (Space Complexity:", sum(gen), ")")
                return node.path_depth, computational_time, node.action, node.parent + node.state[0], node.estimated_cost
            else:
                new = expand_node(problem, node, 3, sol, visited)
                fringe.extend(new)
                gen.append(len(new))
                visited.extend([i.state[0] for i in new])
                if (computational_time % 50000) == 0:
                    print('Time:', computational_time)
    else:
        print("Select an adequate mode: \n")
        print(" 0: Breadth First Graph Search \n 1: Depth First Graph Search or Limited Depth Graph Search \n "
              "2: Iterative Deepening Graph Search \n 3: A Star Graph Search \n")
        return None, None, None, None, None


def bi_search(problem, mode, problem2):
    computational_time = 0
    fringe = deque([MakeNode([problem.w, problem.player], [0], 'Root', 0, 0)])
    goal_fringe = deque([MakeNode([problem2.w, problem2.player], [0], '', 0, 0)])
    visited = [problem.w]
    visited2 = [problem2.w]
    if mode == 0:
        while True:
                node = fringe.popleft()
                node2 = goal_fringe.popleft()
                if node.state[0] == node2.state[0]:
                           a = node2.action.split(',')
                           a.reverse()
                           node2.parent.pop(0)
                           b = [node2.parent[i:i+len(node2.state[0])] for i in range(0, len(node2.parent), len(node2.state[0]))][::-1]
                           return node.path_depth + node2.path_depth, computational_time, node.action+','.join(a), node.parent + \
                                   node.state[0] + sum(b, []), node.estimated_cost + node2.estimated_cost
                problem.w, problem.player = node.state[0], node.state[1]
                computational_time += 1
                new = expand_node(problem, node, 4, 0, visited)
                fringe.extend(new)
                visited.extend([i.state[0] for i in new])
                problem2.w, problem2.player = node2.state[0], node2.state[1]
                new2 = expand_node(problem2, node2, 4, 0, visited2)
                goal_fringe.extend(new2)
                visited2.extend([i.state[0] for i in new2])

                if (computational_time % 50000) == 0:
                    print('Time:', computational_time)


# problem = Space(4, 4, obstacles=True)
# pprint.pprint(problem.w)
#
# problem2 = Space2(4, 4, obstacles=True)
# pprint.pprint(problem2.w)
#
# depth, complexity, moves, history, cost = bi_search(problem, 0, problem2)

problem = Space(4, 4, obstacles=True)
pprint.pprint(problem.w)
pprint.pprint(problem.solution())
#
# # depth, complexity, moves, history, cost = search(problem, 2, 30, obstacles=False)
#
depth, complexity, moves, history, cost = graph_search(problem, 3, obstacles=True)

if depth == 0:
    print('Initial state is equal to goal state')
elif depth == np.inf:
    print('Searched Tree, no possible result')
elif complexity is None:
    print("Please follow the instructions to run the simulation")
else:
    print('Scored Computational TIme:', complexity)
    print('node Depth to reach goal state:', depth)
    print("Estimated Path Cost:", cost)
    print('Moves used to reach goal state (', str(moves).count(','), ') :\n', moves)
    print('Graphical representation of moves:')
    pprint.pprint(list(history))
end = time.time()
print("Elapsed Time = %s" % (end - start))
