"""
The code uses a top-down dynamic programming approach with memorization to solve the problem. The function
number_of_ways takes two arguments: n, which is the ladder to reach, and dp, which is an array to store the intermediate
results. The base cases are for when n is 0 or 1, for which there is only 1 way to reach the ladder. For all other
values of n, the function calls itself twice, once with n-1 and once with n-2, and adds the results to get the total
number of ways to reach the ladder. The dp array is used to store the intermediate results so that they can be reused if
the same sub-problem is encountered again, reducing the time complexity.

Here's a code in Python to find the number of ways to reach the Nth ladder using the top-down dynamic programming
approach with memorization:
"""


def number_of_ways(n, dp):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = number_of_ways(n - 1, dp) + number_of_ways(n - 2, dp)
    return dp[n]


n = int(input("Enter the value of N: "))
dp = [-1] * (n + 1)
print("The number of ways to reach the", n, "th ladder is", number_of_ways(n, dp))
