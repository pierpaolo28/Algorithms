# Class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, N):
        # List of Lists to represent an adjacency list
        self.neighbors = [[] for _ in range(N)]
        # Adding edges to the undirected graph
        for (src, dest) in edges:
            self.neighbors[src].append(dest)
            self.neighbors[dest].append(src)


# List of graph edges as per above diagram
edges = [(0, 1), (0, 2), (0, 3), (1, 3), (3, 4), (2, 3)]

# Set number of vertices in the graph (0-12)
# create a graph from edges
N = 5
graph = Graph(edges, N)
print(graph.neighbors)
marked = [False] * N


# DFS Recursive (Preorder)
def dfs_test_1(graph, v):
    print(v)
    marked[v] = True
    for node in graph.neighbors[v]:
        if not marked[node]:
            dfs_test_1(graph, node)


#dfs_test_1(graph, 0)


# DFS Iterative (Preorder)
def dfs_test_2(graph, v):
    stack = [v]
    while len(stack) > 0:
        v = stack.pop()
        if not marked[v]:
            print(v)
            marked[v] = True
        for node in graph.neighbors[v]:
            if not marked[node]:
                stack.append(node)


#dfs_test_2(graph, 0)


# DFS Recursive (Postorder)
def dfs_test_3(graph, v):
    marked[v] = True
    for node in graph.neighbors[v]:
        if not marked[node]:
            dfs_test_1(graph, node)
    print(v)


# dfs_test_3(graph, 0)