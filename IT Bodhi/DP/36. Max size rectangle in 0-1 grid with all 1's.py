"""
Problem : Max size rectangle in 0/1 grid with all 1's
Ex-:


Approach 1: BF
        TC: O(N^6)

Approach 2: Sum Approach
        TC: O(N^4)

Approach 3: Using Max Rectangle Area Stack Logic
        TC: O(N^3)
        Do for N level:
            At each level we are taking O(N) area logic and to Calculate Height is O(N^2)

Approach 3: Using Max Rectangle Area Stack Logic Optimized
        TC: O(N^2)
        Do for N level:
            At each level we are taking O(N) area logic and to Calculate Height is O(N) if we remember previous previous
            Extra space -: O(N) to store previous level

"""

