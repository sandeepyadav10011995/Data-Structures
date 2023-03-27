"""
Types Of Graphs
    1. Undirected Graphs
        (u, v) = (v, u)
        Example -: Road B/w cities

    2. Directed Graphs
        (u, v) != (v, u)
        Example -: People gifting persons

Weighted Graphs -: It can be undirected or directed graph.
                   Notation -: (u, v, w)
                               w -: weight {cost, dist, quantity etc}

Common Problems -: We should look at while solving Graph Theory Problems
    1. Is the graph directed or undirected?
    2. Are the edges of the graph weighted?
    3. Is the graph we will encounter likely to be Sparse or Dense with edges?
    4. Should I use Adjacency Matrix, Adjacency List or Edge List or other structure to represent the graph efficiency?

----------------------  MOST COMMON GRAPHS PROBLEMS  ----------------------

SHORTEST PATH PROBLEM -: Given a weighted graph, find the shortest path of edges from Node A to Node B.
                        Algorithms -:   BFS --> unweighted graph
                                        Dijkstra's Algorithms
                                        Bellman Ford
                                        Floyd Warshall

CONNECTIVITY -: Does there an exists a path b/w Node A to Node B
                Typical Solution -: Union Find Data Structure
                                    Any Search Algorithm (e.g. DFS)


MINIMUM SPANNING TREE -: In short MST :: It's a tree with no cycles, and it spans the graph at a minimal cost.
                         Algorithms -: Kruskal's Algorithm
                                       Prim's Algorithm

-----------------------------  IMPORTANT NOTES ------------------------

TO FIND A CYCLE IN A GRAPH --> Do a DFS on that.
DP will not work whenever there is CYCLE in Recursive Relation. Therefore, use BFS.


"""
