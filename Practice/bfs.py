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
edges = [(0, 1), (0, 3), (0, 2), (1, 3), (3, 4), (2, 3)]

# Set number of vertices in the graph (0-12)
# create a graph from edges
N = 5
graph = Graph(edges, N)
print(graph.neighbors)
marked = [False] * N


def bfs_test(graph, v):
    stack = [v]
    while len(stack) > 0:
        v = stack.pop(0)
        if not marked[v]:
            print(v)
            marked[v] = True
        for node in graph.neighbors[v]:
            if not marked[node]:
                stack.append(node)


bfs_test(graph, 0)