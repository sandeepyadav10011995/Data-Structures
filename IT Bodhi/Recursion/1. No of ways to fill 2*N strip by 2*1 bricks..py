"""
The code uses a recursive approach to solve the problem. The base cases are for when n is 0 and 1, for which there is
only 1 and 2 ways to fill the strip, respectively. For all other values of n, the function calls itself twice, once with
n-1 and once with n-2, and adds the results to get the total number of ways to fill the strip.

Here's a code in Python to find the number of ways to fill a 2 x N strip with 2 x 1 bricks:
"""


def fill_strip(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    else:
        return fill_strip(n - 1) + fill_strip(n - 2)


n = int(input("Enter the value of N: "))
print("The number of ways to fill 2 x", n, "strip is", fill_strip(n))
