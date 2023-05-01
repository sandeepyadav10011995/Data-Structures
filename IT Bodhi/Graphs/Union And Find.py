"""
Union-find is a popular algorithm used for grouping objects into sets. It can be used to group friends
into one group based on their relationships with each other.

The algorithm works by creating a disjoint set for each object, with a representative element representing each set.
Initially, each element is in its own set. As we process the input relationships between friends, we merge sets by
unioning them.

For example, suppose we have four friends A, B, C, and D, and we know that A and B are friends, and B and C are friends.
To group them into one set, we would start by creating four singleton sets {A}, {B}, {C}, and {D}. Then, we would union
the sets containing A and B, resulting in {A,B}, {C}, and {D}. Finally, we would union the set containing B with the set
containing C, resulting in {A,B,C}, and {D}.

At the end of the algorithm, each set contains all the friends who are connected to each other through their
relationships. The representative element for each set can be used to identify the group of friends to which each
person belongs.
"""


from typing import List


class UnionFindBasic:  # Overall TC: O(NlogN)
    def __init__(self, n):  # O(N)
        """
        This code defines a class called UnionFind. The constructor of the class takes an argument n which specifies
        the number of elements that need to be grouped. The constructor initializes two lists parent and rank.
        The parent list holds the parent of each element, which is initially set to the element's own index.
        The rank list holds the rank of each element, which is initially set to 0.
        """
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):  # Amortized Cost -> O(logN) Worst Case O(N)
        """
        The find method takes an element x as input and returns the representative element for the group containing x.
        This method uses path compression to optimize the search for the representative element.

        It first checks if the parent of x is equal to x. If it is not, it recursively calls find on the parent of x
        until it finds the representative element, and then sets the parent of x to be the representative element.

        Important -:
            This path compression technique ensures that subsequent find operations on x (and other elements in the
            same group) are faster.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y): #  O(logN)
        """
        The union method takes two elements x and y as input and merges the groups containing x and y.
        It first finds the representative elements root_x and root_y for the groups containing x and y using the
        find method.

        If root_x and root_y are the same, then x and y are already in the same group, so there is
        nothing to do and the method returns.

        Otherwise, the method merges the two groups by making one of the roots the parent of the other,
        based on the rank of each root.
            If root_x has a lower rank than root_y, then root_x becomes the child of root_y.
            If root_x has a higher rank than root_y, then root_y becomes the child of root_x.

        If root_x and root_y have the same rank, then either one can become the parent, and the rank of the new parent
        is incremented by 1.
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


class UnionFind:
    def __init__(self, n: int):
        self.count = n
        self.id = list(range(n))
        self.rank = [0] * n

    def unionByRank(self, u: int, v: int) -> None:
        i = self._find(u)
        j = self._find(v)
        if i == j:
            return
        if self.rank[i] < self.rank[j]:
            self.id[i] = self.id[j]
        elif self.rank[i] > self.rank[j]:
            self.id[j] = self.id[i]
        else:
            self.id[i] = self.id[j]
            self.rank[j] += 1
        self.count -= 1

    def getCount(self) -> int:
        return self.count

    def _find(self, u: int) -> int:
        if self.id[u] != u:
            self.id[u] = self._find(self.id[u])
        return self.id[u]


class Solution1:
    @staticmethod
    def earliestAcq(logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)

        logs.sort(key=lambda x: x[0])

        # Sort `logs` by timestamp.
        for timestamp, x, y in logs:
          uf.unionByRank(x, y)
          if uf.getCount() == 1:
            return timestamp

        return -1


class Solution2:
    @staticmethod
    def earliestAcq(logs: List[List[int]], n: int) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        p = list(range(n))
        logs.sort()
        for t, a, b in logs:
            if find(a) == find(b):
                continue
            p[find(a)] = find(b)
            n -= 1
            if n == 1:
                return t
        return -1


sol1 = Solution1()
sol2 = Solution2()
logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],
         [20190322,4,5]]
N = 6
print(sol1.earliestAcq(logs, N))
print("*"*100)
print(sol2.earliestAcq(logs, N))
