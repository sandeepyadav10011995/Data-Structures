"""
To demonstrate that computer scientists can turn just about anything into a graph problem, let’s consider the difficult problem of 
stirring up a batch of pancakes. The recipe is really quite simple: 1 egg, 1 cup of pancake mix, 1 tablespoon oil, and 34 cup of milk. 
To make pancakes you must heat the griddle, mix all the ingredients together and spoon the mix onto a hot griddle. 
When the pancakes start to bubble you turn them over and let them cook until they are golden brown on the bottom. 
Before you eat your pancakes you are going to want to heat up some syrup. Figure 27 illustrates this process as a graph.


"""
import random
class Node:
    def __init__(self, key):
        self.key = key
        self.connections = []
class Graph:
    def __init__(self):
        self.nodes = {}
    def addEdge(self, _from, _to):
        # check if node exists already
        from_node = self.addNode(_from)
        to_node = self.addNode(_to)
        # add edge
        from_node.connections.append(to_node)
    def addNode(self, key):
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]
def dfs(graph, node, visited, i, ordering):
    visited.add(node)
    for next_node in node.connections:
        if next_node not in visited:
            i = dfs(graph, next_node, visited, i, ordering)
    ordering[i] = node
    return i-1
def topological_sort(graph_object: Graph):
    nodes = graph_object.nodes
    N = len(nodes)
    visited = set()
    ordering = [0] * N
    i = N-1
    keys = list(nodes.keys())
    random.shuffle(keys)
    for each_node in keys:
        if nodes[each_node] not in visited:
            i = dfs(graph_object, nodes[each_node], visited, i, ordering)
    return [i.key for i in ordering]
g1 = Graph()
for node in ('A','B','C','D','E','F','G','H','I','J','K','L','M'):
    g1.addNode(node)
g1.addEdge('A', 'D')
g1.addEdge('C', 'A')
g1.addEdge('C', 'B')
g1.addEdge('B', 'D')
g1.addEdge('D', 'G')
g1.addEdge('D', 'H')
g1.addEdge('H', 'J')
g1.addEdge('H', 'I')
g1.addEdge('G', 'I')
g1.addEdge('I', 'L')
g1.addEdge('J', 'L')
g1.addEdge('J', 'M')
g1.addEdge('K', 'J')
g1.addEdge('F', 'K')
g1.addEdge('F', 'J')
g1.addEdge('E', 'A')
g1.addEdge('E', 'D')
g1.addEdge('E', 'F')
for i in range(10):
    print(topological_sort(g1))


