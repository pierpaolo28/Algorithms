import pprint
from Blocksworld_tile_puzzle import Space, Space2, Game, MakeNode, expand_node, search, graph_search, bi_search

print("Welcome to my Blocksworld tile puzzle solver")
print("What game matrix size do you prefer? (minimum 4*4)")
m = input("Number of rows: ")
n = input("Number of columns: ")
if int(m) < 4  or int(n) < 4:
    print("Invalid selction")

print("Do you want to use Tree (0), Graph Search (1) or Bilateral Search (2)?")
t_or_g = input("")
if t_or_g == "0":
    obs = input("Do you want to add obstacles in the world? (yes/no)")
    if obs == "no":
        print("Do you want to play the game yourself? (yes/no)")
        p = input("")
        if p == 'yes':
            print("Use a to move left, d to move right, w to move up, z to move down and e to escape the game")
            play = Game(int(m), int(n))
            print(play)
        print("Which algorithm do you want to use to solve the Blocksworld tile puzzle?")
        print(" 0: Breadth First Search \n 1: Depth First Search or Limited Depth Search \n "
              "2: Iterative Deepening \n 3: A Star \n")
        choice = input("")
        if choice == '0':
            problem = Space(int(m), int(n))
            pprint.pprint(problem.w)
            pprint.pprint(problem.solution())

            depth, complexity, moves, history, cost = search(problem, 0)
            if depth == 0:
                print('Initial state is equal to goal state')
            elif depth == 1:
                print('Searched Tree, no possible result')
            elif complexity is None:
                print("Please follow the instructions to run the simulation")
            else:
                print('Scored Computational TIme:', complexity)
                print('Node Depth to reach goal state:', depth)
                print("Estimated Path Cost:", cost)
                print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                print('Graphical representation of moves:')
                pprint.pprint(history)
        elif choice == '1':
            print("Do you want to use Depth First search? (yes/no)")
            d = input("")
            if d == 'yes':
                problem = Space(int(m), int(n))
                pprint.pprint(problem.w)
                pprint.pprint(problem.solution())

                depth, complexity, moves, history, cost = search(problem, 1)
                if depth == 0:
                    print('Initial state is equal to goal state')
                elif depth == 1:
                    print('Searched Tree, no possible result')
                elif complexity is None:
                    print("Please follow the instructions to run the simulation")
                else:
                    print('Scored Computational TIme:', complexity)
                    print('Node Depth to reach goal state:', depth)
                    print("Estimated Path Cost:", cost)
                    print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                    print('Graphical representation of moves:')
                    pprint.pprint(history)
            elif d == 'no':
                lim = input("Please enter the Depth limited search limit: ")
                problem = Space(int(m), int(n))
                pprint.pprint(problem.w)
                pprint.pprint(problem.solution())

                depth, complexity, moves, history, cost = search(problem, 1, int(lim))
                if depth == 0:
                    print('Initial state is equal to goal state')
                elif depth == 1:
                    print('Searched Tree, no possible result')
                elif complexity is None:
                    print("Please follow the instructions to run the simulation")
                else:
                    print('Scored Computational TIme:', complexity)
                    print('Node Depth to reach goal state:', depth)
                    print("Estimated Path Cost:", cost)
                    print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                    print('Graphical representation of moves:')
                    pprint.pprint(history)
        elif choice == '2':
            i = input("Please enter the maximum number of iterations: ")
            problem = Space(int(m), int(n))
            pprint.pprint(problem.w)
            pprint.pprint(problem.solution())

            depth, complexity, moves, history, cost = search(problem, 2, int(i))
            if depth == 0:
                print('Initial state is equal to goal state')
            elif depth == 1:
                print('Searched Tree, no possible result')
            elif complexity is None:
                print("Please follow the instructions to run the simulation")
            else:
                print('Scored Computational TIme:', complexity)
                print('Node Depth to reach goal state:', depth)
                print("Estimated Path Cost:", cost)
                print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                print('Graphical representation of moves:')
                pprint.pprint(history)
        elif choice == '3':
            problem = Space(int(m), int(n))
            pprint.pprint(problem.w)
            pprint.pprint(problem.solution())

            depth, complexity, moves, history, cost = search(problem, 3)
            if depth == 0:
                print('Initial state is equal to goal state')
            elif depth == 1:
                print('Searched Tree, no possible result')
            elif complexity is None:
                print("Please follow the instructions to run the simulation")
            else:
                print('Scored Computational TIme:', complexity)
                print('Node Depth to reach goal state:', depth)
                print("Estimated Path Cost:", cost)
                print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                print('Graphical representation of moves:')
                pprint.pprint(history)
        else:
            print("Please follow the instructions")
    elif obs == 'yes':
        print("Do you want to play the game yourself? (yes/no)")
        p = input("")
        if p == 'yes':
            print("Use a to move left, d to move right, w to move up, z to move down and e to escape the game")
            play = Game(int(m), int(n), obstacles=True)
            print(play)
        print("Which algorithm do you want to use to solve the Blocksworld tile puzzle?")
        print(" 0: Breadth First Search \n 1: Depth First Search or Limited Depth Search \n "
              "2: Iterative Deepening \n 3: A Star \n")
        choice = input("")
        if choice == '0':
            problem = Space(int(m), int(n), obstacles=True)
            pprint.pprint(problem.w)
            pprint.pprint(problem.solution())

            depth, complexity, moves, history, cost = search(problem, 0, obstacles=True)
            if depth == 0:
                print('Initial state is equal to goal state')
            elif depth == 1:
                print('Searched Tree, no possible result')
            elif complexity is None:
                print("Please follow the instructions to run the simulation")
            else:
                print('Scored Computational TIme:', complexity)
                print('Node Depth to reach goal state:', depth)
                print("Estimated Path Cost:", cost)
                print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                print('Graphical representation of moves:')
                pprint.pprint(history)
        elif choice == '1':
            print("Do you want to use Depth First search? (yes/no)")
            d = input("")
            if d == 'yes':
                problem = Space(int(m), int(n), obstacles=True)
                pprint.pprint(problem.w)
                pprint.pprint(problem.solution())

                depth, complexity, moves, history, cost = search(problem, 1, obstacles=True)
                if depth == 0:
                    print('Initial state is equal to goal state')
                elif depth == 1:
                    print('Searched Tree, no possible result')
                elif complexity is None:
                    print("Please follow the instructions to run the simulation")
                else:
                    print('Scored Computational TIme:', complexity)
                    print('Node Depth to reach goal state:', depth)
                    print("Estimated Path Cost:", cost)
                    print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                    print('Graphical representation of moves:')
                    pprint.pprint(history)
            elif d == 'no':
                lim = input("Please enter the Depth limited search limit: ")
                problem = Space(int(m), int(n), obstacles=True)
                pprint.pprint(problem.w)
                pprint.pprint(problem.solution())

                depth, complexity, moves, history, cost = search(problem, 1, int(lim), obstacles=True)
                if depth == 0:
                    print('Initial state is equal to goal state')
                elif depth == 1:
                    print('Searched Tree, no possible result')
                elif complexity is None:
                    print("Please follow the instructions to run the simulation")
                else:
                    print('Scored Computational TIme:', complexity)
                    print('Node Depth to reach goal state:', depth)
                    print("Estimated Path Cost:", cost)
                    print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                    print('Graphical representation of moves:')
                    pprint.pprint(history)
        elif choice == '2':
            i = input("Please enter the maximum number of iterations: ")
            problem = Space(int(m), int(n), obstacles=True)
            pprint.pprint(problem.w)
            pprint.pprint(problem.solution())

            depth, complexity, moves, history, cost = search(problem, 2, int(i), obstacles=True)
            if depth == 0:
                print('Initial state is equal to goal state')
            elif depth == 1:
                print('Searched Tree, no possible result')
            elif complexity is None:
                print("Please follow the instructions to run the simulation")
            else:
                print('Scored Computational TIme:', complexity)
                print('Node Depth to reach goal state:', depth)
                print("Estimated Path Cost:", cost)
                print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                print('Graphical representation of moves:')
                pprint.pprint(history)
        elif choice == '3':
            problem = Space(int(m), int(n), obstacles=True)
            pprint.pprint(problem.w)
            pprint.pprint(problem.solution())

            depth, complexity, moves, history, cost = search(problem, 3, obstacles=True)
            if depth == 0:
                print('Initial state is equal to goal state')
            elif depth == 1:
                print('Searched Tree, no possible result')
            elif complexity is None:
                print("Please follow the instructions to run the simulation")
            else:
                print('Scored Computational TIme:', complexity)
                print('Node Depth to reach goal state:', depth)
                print("Estimated Path Cost:", cost)
                print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                print('Graphical representation of moves:')
                pprint.pprint(history)
        else:
            print("Please follow the instructions")
elif t_or_g == "1":
    obs = input("Do you want to add obstacles in the world? (yes/no)")
    if obs == "no":
        print("Do you want to play the game yourself? (yes/no)")
        p = input("")
        if p == 'yes':
            print("Use a to move left, d to move right, w to move up, z to move down and e to escape the game")
            play = Game(int(m), int(n))
            print(play)
        print("Which algorithm do you want to use to solve the Blocksworld tile puzzle?")
        print(" 0: Breadth First Graph Search \n 1: Depth First Graph Search or Limited Depth Graph Search \n "
              "2: Iterative Deepening Graph Search \n 3: A Star Graph Search \n")
        choice = input("")
        if choice == '0':
            problem = Space(int(m), int(n))
            pprint.pprint(problem.w)
            pprint.pprint(problem.solution())

            depth, complexity, moves, history, cost = graph_search(problem, 0)
            if depth == 0:
                print('Initial state is equal to goal state')
            elif depth == 1:
                print('Searched Tree, no possible result')
            elif complexity is None:
                print("Please follow the instructions to run the simulation")
            else:
                print('Scored Computational TIme:', complexity)
                print('Node Depth to reach goal state:', depth)
                print("Estimated Path Cost:", cost)
                print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                print('Graphical representation of moves:')
                pprint.pprint(history)
        elif choice == '1':
            print("Do you want to use Depth First search? (yes/no)")
            d = input("")
            if d == 'yes':
                problem = Space(int(m), int(n))
                pprint.pprint(problem.w)
                pprint.pprint(problem.solution())

                depth, complexity, moves, history, cost = graph_search(problem, 1)
                if depth == 0:
                    print('Initial state is equal to goal state')
                elif depth == 1:
                    print('Searched Tree, no possible result')
                elif complexity is None:
                    print("Please follow the instructions to run the simulation")
                else:
                    print('Scored Computational TIme:', complexity)
                    print('Node Depth to reach goal state:', depth)
                    print("Estimated Path Cost:", cost)
                    print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                    print('Graphical representation of moves:')
                    pprint.pprint(history)
            elif d == 'no':
                lim = input("Please enter the Depth limited search limit: ")
                problem = Space(int(m), int(n))
                pprint.pprint(problem.w)
                pprint.pprint(problem.solution())

                depth, complexity, moves, history, cost = graph_search(problem, 1, int(lim))
                if depth == 0:
                    print('Initial state is equal to goal state')
                elif depth == 1:
                    print('Searched Tree, no possible result')
                elif complexity is None:
                    print("Please follow the instructions to run the simulation")
                else:
                    print('Scored Computational TIme:', complexity)
                    print('Node Depth to reach goal state:', depth)
                    print("Estimated Path Cost:", cost)
                    print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                    print('Graphical representation of moves:')
                    pprint.pprint(history)
        elif choice == '2':
            i = input("Please enter the maximum number of iterations: ")
            problem = Space(int(m), int(n))
            pprint.pprint(problem.w)
            pprint.pprint(problem.solution())

            depth, complexity, moves, history, cost = graph_search(problem, 2, int(i))
            if depth == 0:
                print('Initial state is equal to goal state')
            elif depth == 1:
                print('Searched Tree, no possible result')
            elif complexity is None:
                print("Please follow the instructions to run the simulation")
            else:
                print('Scored Computational TIme:', complexity)
                print('Node Depth to reach goal state:', depth)
                print("Estimated Path Cost:", cost)
                print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                print('Graphical representation of moves:')
                pprint.pprint(history)
        elif choice == '3':
            problem = Space(int(m), int(n))
            pprint.pprint(problem.w)
            pprint.pprint(problem.solution())

            depth, complexity, moves, history, cost = graph_search(problem, 3)
            if depth == 0:
                print('Initial state is equal to goal state')
            elif depth == 1:
                print('Searched Tree, no possible result')
            elif complexity is None:
                print("Please follow the instructions to run the simulation")
            else:
                print('Scored Computational TIme:', complexity)
                print('Node Depth to reach goal state:', depth)
                print("Estimated Path Cost:", cost)
                print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                print('Graphical representation of moves:')
                pprint.pprint(history)
        else:
            print("Please follow the instructions")
    elif obs == 'yes':
        print("Do you want to play the game yourself? (yes/no)")
        p = input("")
        if p == 'yes':
            print("Use a to move left, d to move right, w to move up, z to move down and e to escape the game")
            play = Game(int(m), int(n), obstacles=True)
            print(play)
        print("Which algorithm do you want to use to solve the Blocksworld tile puzzle?")
        print(" 0: Breadth First Search \n 1: Depth First Search or Limited Depth Search \n "
              "2: Iterative Deepening \n 3: A Star \n")
        choice = input("")
        if choice == '0':
            problem = Space(int(m), int(n), obstacles=True)
            pprint.pprint(problem.w)
            pprint.pprint(problem.solution())

            depth, complexity, moves, history, cost = graph_search(problem, 0, obstacles=True)
            if depth == 0:
                print('Initial state is equal to goal state')
            elif depth == 1:
                print('Searched Tree, no possible result')
            elif complexity is None:
                print("Please follow the instructions to run the simulation")
            else:
                print('Scored Computational TIme:', complexity)
                print('Node Depth to reach goal state:', depth)
                print("Estimated Path Cost:", cost)
                print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                print('Graphical representation of moves:')
                pprint.pprint(history)
        elif choice == '1':
            print("Do you want to use Depth First search? (yes/no)")
            d = input("")
            if d == 'yes':
                problem = Space(int(m), int(n), obstacles=True)
                pprint.pprint(problem.w)
                pprint.pprint(problem.solution())

                depth, complexity, moves, history, cost = graph_search(problem, 1, obstacles=True)
                if depth == 0:
                    print('Initial state is equal to goal state')
                elif depth == 1:
                    print('Searched Tree, no possible result')
                elif complexity is None:
                    print("Please follow the instructions to run the simulation")
                else:
                    print('Scored Computational TIme:', complexity)
                    print('Node Depth to reach goal state:', depth)
                    print("Estimated Path Cost:", cost)
                    print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                    print('Graphical representation of moves:')
                    pprint.pprint(history)
            elif d == 'no':
                lim = input("Please enter the Depth limited search limit: ")
                problem = Space(int(m), int(n), obstacles=True)
                pprint.pprint(problem.w)
                pprint.pprint(problem.solution())

                depth, complexity, moves, history, cost = graph_search(problem, 1, int(lim), obstacles=True)
                if depth == 0:
                    print('Initial state is equal to goal state')
                elif depth == 1:
                    print('Searched Tree, no possible result')
                elif complexity is None:
                    print("Please follow the instructions to run the simulation")
                else:
                    print('Scored Computational TIme:', complexity)
                    print('Node Depth to reach goal state:', depth)
                    print("Estimated Path Cost:", cost)
                    print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                    print('Graphical representation of moves:')
                    pprint.pprint(history)
        elif choice == '2':
            i = input("Please enter the maximum number of iterations: ")
            problem = Space(int(m), int(n), obstacles=True)
            pprint.pprint(problem.w)
            pprint.pprint(problem.solution())

            depth, complexity, moves, history, cost = graph_search(problem, 2, int(i), obstacles=True)
            if depth == 0:
                print('Initial state is equal to goal state')
            elif depth == 1:
                print('Searched Tree, no possible result')
            elif complexity is None:
                print("Please follow the instructions to run the simulation")
            else:
                print('Scored Computational TIme:', complexity)
                print('Node Depth to reach goal state:', depth)
                print("Estimated Path Cost:", cost)
                print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                print('Graphical representation of moves:')
                pprint.pprint(history)
        elif choice == '3':
            problem = Space(int(m), int(n), obstacles=True)
            pprint.pprint(problem.w)
            pprint.pprint(problem.solution())

            depth, complexity, moves, history, cost = graph_search(problem, 3, obstacles=True)
            if depth == 0:
                print('Initial state is equal to goal state')
            elif depth == 1:
                print('Searched Tree, no possible result')
            elif complexity is None:
                print("Please follow the instructions to run the simulation")
            else:
                print('Scored Computational TIme:', complexity)
                print('Node Depth to reach goal state:', depth)
                print("Estimated Path Cost:", cost)
                print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
                print('Graphical representation of moves:')
                pprint.pprint(history)
        else:
            print("Please follow the instructions")
elif t_or_g == "2":
    obs = input("Do you want to add obstacles in the world? (yes/no)")
    if obs == "no":
        print("Do you want to play the game yourself? (yes/no)")
        p = input("")
        if p == 'yes':
            print("Use a to move left, d to move right, w to move up, z to move down and e to escape the game")
            play = Game(int(m), int(n))
            print(play)
        print("Bilateral Search using Breath First Search")
        problem = Space(int(m), int(n))
        pprint.pprint(problem.w)

        problem2 = Space2(int(m), int(n))
        pprint.pprint(problem2.w)

        depth, complexity, moves, history, cost = bi_search(problem, 0, problem2)
        if depth == 0:
            print('Initial state is equal to goal state')
        elif depth == 1:
            print('Searched Tree, no possible result')
        elif complexity is None:
            print("Please follow the instructions to run the simulation")
        else:
            print('Scored Computational TIme:', complexity)
            print('Node Depth to reach goal state:', depth)
            print("Estimated Path Cost:", cost)
            print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
            print('Graphical representation of moves:')
            pprint.pprint(history)
    elif obs == 'yes':
        print("Do you want to play the game yourself? (yes/no)")
        p = input("")
        if p == 'yes':
            print("Use a to move left, d to move right, w to move up, z to move down and e to escape the game")
            play = Game(int(m), int(n), obstacles=True)
            print(play)
        print("Bilateral Search using Breath First Search")
        problem = Space(int(m), int(n), obstacles=True)
        pprint.pprint(problem.w)

        problem2 = Space2(int(m), int(n), obstacles=True)
        pprint.pprint(problem2.w)

        depth, complexity, moves, history, cost = bi_search(problem, 0, problem2)
        if depth == 0:
            print('Initial state is equal to goal state')
        elif depth == 1:
            print('Searched Tree, no possible result')
        elif complexity is None:
            print("Please follow the instructions to run the simulation")
        else:
            print('Scored Computational TIme:', complexity)
            print('Node Depth to reach goal state:', depth)
            print("Estimated Path Cost:", cost)
            print('Moves used to reach goal state (', moves.count(','), ') :\n', moves)
            print('Graphical representation of moves:')
            pprint.pprint(history)
else:
    print("Please follow the instructions")
