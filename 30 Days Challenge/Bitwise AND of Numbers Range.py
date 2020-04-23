"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0

"""

# Brute-Force Solution
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        output = m
        for i in range(m+1, n+1):
            output = output & i
        return output


# Optimized Solution --> Using LSB (Left Significant Bit)
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n -= (n & -n)
        return n

