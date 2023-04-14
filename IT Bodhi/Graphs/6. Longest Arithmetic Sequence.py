"""
Problem : Longest Arithmetic Sequence

    6   2   5   7   4   11  6   12  8   10
1   1   1   1   2   1
2   1   1   1   2   2
3   1   1   2   1   1       3       4   5
4   1   1   1   1
5   1   1   1   2
6   1   1   1   1
7   1   1   1   1
8   1   1   1   1
9   1   1   1   1
10  1   1   1   1
11  1   1   1   1
12  1   1   1   1

Main Data Structure -: Map of Maps
                  Key -: Index(int)
                  Value -: Map
                            Key -: Constant Sum(int)
                            Value -: Length(int)

Note if the constantSum is not present in the map the for that the default value is 1.

TC: N^2 + N^2 ~ O(N^2)
SC: O(N^2) --> This will used to find in O(1)
"""
