"""
---------------------------- FENWICK TREE --------------------------
Imagine you have a really long list of numbers, and you want to quickly find the sum of any part of that list.
A Fenwick tree is a data structure that can help you do that efficiently.

It works by storing the cumulative sum of the numbers in the list at each position in the tree.
To find the sum of a specific range of numbers in the list, you only need to look at a few specific nodes in the tree.

Approach 1: Simple Calculate Prefix Sum --> O(N)
Fetch (2, 4) = (0, 4) - (0, 2)

Problem -: Update -: As all the prefixSum on the right side of the index would need to be updated.
TC -: Query No * Update(O(N))
So this will not be efficient approach in case if there are frequent updates operations


Solution -: Fenwick Tree :: A Fenwick tree is a data structure that can help you do that efficiently.

Dummy Node -: Index 0
    Dummy-Node
               (1,1)          (3,3)           (5,5)           (7,7)           (9,9)           (11,11)         (13,13)         (15,15)
index   0       1       2       3       4       5       6       7       8       9       10      11      12      13      14      15      16
range                 (1,2)            (1,4)          (5,6)           (1,8)            (9,10)         (9,12)          (13,14)         (1,16)


How to fill the array -: Initially all the index would be assigned as 0
Rules ::
Fill the value for index 1 from the input array
Then update all the values where 1 is left of the range
1. 2's complement
2. & with original number
3. add to the original number

==> i = i + (i&(-i)) or += (i&(-i))

How to find the value for the given range -: F(0, 12) = 8-->F(1, 8) + 4-->F(9, 12)
Easier way -: 2's complement logic
Example F(1, 13) = F(13) + F(9, 12) + F(1, 8)
Steps-:
1101(13) --> Offset the right most bit --> 1100 (12)
1100(12) --> Offset the right most bit --> 1000(8)
1000(8)  --> Offset the right most bit --> 0000(0)



For index=1-:
Binary repr for 1 = 1
Offset the right most bit --> 0 ==> val = 0
Left = val + 1 ==> 0+1 = 1
Right = index = 1
Range(left, right) = (1, 1)

For index=2-:
Binary repr for 2 = 10
Offset the right most bit --> 00 ==> val = 0
Left = val + 1 ==> 0+1 = 1
Right = index = 2
Range(left, right) = (1, 2)

For index=3-:
Binary repr for 3 = 11
Offset the right most bit --> 10 ==> val = 2
Left = val + 1 ==> 0+2 = 2
Right = index = 3
Range(left, right) => (3, 3)

For index=4-:
Binary repr for 4 = 100
Offset the right most bit --> 000 ==> val = 0
Left = val + 1 ==> 0+1 = 1
Right = index = 4
Range(left, right) = (1, 4)

For index=4-:
Binary repr for 4 = 100
Offset the right most bit --> 000 ==> val = 0
Left = val + 1 ==> 0+1 = 1
Right = index = 4
Range(left, right) = (1, 4)


For index=4-:
Binary repr for 4 = 100
Offset the right most bit --> 000 ==> val = 0
Left = val + 1 ==> 0+1 = 1
Right = index = 4
Range(left, right) = (1, 4)
===================================================================
Note that the FenwickTree class uses 1-based indexing instead
of 0-based indexing for its array and query operations.
===================================================================
"""


class FenwickTree:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr
        self.N = len(arr)
        """
        Note that the FenwickTree class uses 1-based indexing instead
        of 0-based indexing for its array and query operations.
        """
        self.fen = [0 for _ in range(self.N+1)]

    def _update(self, idx: int, addVal: int) -> None:
        idx += 1
        while idx < self.N:
            self.fen[idx] += addVal
            idx += (idx&(-idx))

    def _sum(self, idx):
        s = 0
        while idx > 0:
            s += self.fen[idx]
            idx -= (idx & (-idx))
        return s

    def createFenwickTree(self) -> None:
        for i in range(self.N):
            self._update(idx=i, addVal=self.arr[i])
        return self.fen

    def rangeSum(self, l: int, r: int):
        return self._sum(r) - self._sum(l-1)


f = FenwickTree(arr=[1, 3, 2, 4, 5, 7, 6])
print(f.fen)
print(f.createFenwickTree())
