"""
Problem : Find the celebrity using party data as 2D Boolean matrix.
Relation(i, j) --> If i knows j ?
0 -> No
1 -> Yes
E --> IS THE CELEBRITY


        A   B   C   D   E   F
        0   1   2   3   4   5
A   0   0   0   1   1   1   0
B   1   1   0   0   0   1   1
C   2   1   1   0   1   1   0
D   3   1   1   0   0   1   1
E   4   0   0   0   0   0   0
F   5   1   0   1   0   1   0

Approach 1: CONDITION OF CELEBRITY ->
        1. All row value will be 0 except itself
        2. All the col values will be 1
        TC: O(N*(N+N)) ~ O(2N^2) ~ O(N^2)
        SC: O(1)

Approach 2: Starting Point -: 1st row, Last col
    If the search value is 1, then MOVE down and DISCARD the ROW
    If the search value is 0, then MOVE left and DISCARD the COL
    TC: O(M+N)
    SC: O(1)
"""


def find_celebrity(matrix: list[list[int]]):
    n = len(matrix)
    potential_celebrity = 0

    # Step 1: Iterate through each row of the matrix.
    for i in range(n):
        # Step 2: Check if there is a 1 at every column except for the person's own column.
        if all(matrix[i][j] == 1 for j in range(n) if j != i):
            potential_celebrity = i
            break

    # Step 3: Iterate through every other person in the matrix to check if they know the potential celebrity.
    for i in range(n):
        if i != potential_celebrity:
            if matrix[potential_celebrity][i] == 1 or matrix[i][potential_celebrity] == 0:
                # The potential celebrity cannot be the true celebrity.
                return -1

    # Step 4: If no person is disqualified in step 3, then the potential celebrity is the true celebrity.
    return potential_celebrity
