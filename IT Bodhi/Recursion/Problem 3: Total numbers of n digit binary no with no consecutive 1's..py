"""
The code uses a top-down dynamic programming approach with memorization to solve the problem. The function
binary_numbers takes two arguments: n, which is the number of digits, and dp, which is an array to store the
intermediate results. The base cases are for when n is 1 or 2, for which there are 2 and 3 n digit binary numbers
with no consecutive 1's, respectively. For all other values of n, the function calls itself twice, once with n-1
and once with n-2, and adds the results to get the total number of n digit binary numbers with no consecutive 1's.
The dp array is used to store the intermediate results so that they can be reused if the same sub-problem is
encountered again, reducing the time complexity.

Here's a code in Python to find the total number of n digit binary numbers with no consecutive 1's:
"""


def binary_numbers(n, dp):
    if n == 1:
        return 2
    if n == 2:
        return 3
    if dp[n] != -1:
        return dp[n]
    dp[n] = binary_numbers(n-1, dp) + binary_numbers(n-2, dp)
    return dp[n]


n = int(input("Enter the value of N: "))
dp = [-1] * (n + 1)
print("The total number of", n, "digit binary numbers with no consecutive 1's is", binary_numbers(n, dp))
