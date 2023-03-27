"""
Topological Sort
Steps:
    Input ==> Vertices: Integer
              Edges : List[(from(int), to(int)] # EDGE LIST
      1. Initialize the Graph
         - inDegree = {i: 0 for i in range(vertices)} # Count of incoming edges
         - graph = {i: [] for i in range(vertices)}

      2. Build the Graph
         - Iterate over all the edges
         - Put the Child into it's Parent's List
         - Increment Child's inDegree

      3. Find all the sources i.e., all the vertices with 0 in-degrees
         - Put all the sources in the bfsQueue

      4. BFS Traversal
         - Pop the node
         - store the node value in sortedOrder
         - Get the node's children to decrement their inDegree
            - if the inDegree == 0 # It is a source now
                Add it the bfsQueue

      5. Return the topological sort if there is no cycle
        if len(sortedOrder) != vertices
"""
from collections import deque


def topological_sort(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder

    # a. Initialize the graph
    inDegree = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjacency list graph

    # b. Build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)  # put the child into it's parent's list
        inDegree[child] += 1  # increment child's inDegree

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:  # get the node's children to decrement their in-degrees
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    return [] if len(sortedOrder) != vertices else sortedOrder


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
