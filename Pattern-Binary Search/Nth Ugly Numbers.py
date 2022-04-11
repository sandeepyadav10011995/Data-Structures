"""
------------------------------------------------------ Binary Search ---------------------------------------------------
1. It is quite easy to understand conceptually.
2. It splits the search space into half the size at every step, until we find the target. Therefore reduces Search Time
   O(N) --> O(logN)

But when it comes to implementation, it's rather difficult to write a bug-free code in just a few minutes. Some of the
most common problems include:
    a. When to exit the loop? Should we use left < right or left <= right as the while loop condition?
    b. How to initialize the boundary variable left and right?
    c. How to update the boundary? How to choose the appropriate combination from left = mid, left = mid + 1 and
       right = mid, right = mid - 1?

A rather common misunderstanding of binary search is that people often think this technique could only be used in simple
scenario like "Given a sorted array, find a specific value in it". As a matter of fact, it can be applied to much more
complicated situations.

3. Most Generalized Binary Search Template -:
   Suppose we have a search space --> It could be an array or range etc.
   ==> Minimize k; s.t. condition(k) is True

def condition(value) -> bool:
    pass


def binary_search(array: list[int]) -> int:
    left = min(search_space)  # could be [0, n], [1, n] etc. Depends on problem
    right = max(search_space)  # could be [0, n], [1, n] etc. Depends on problem

    while left < right:
        mid = left + (right-left)//2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

What's really nice of this template is that, for most of the binary search problems, we only need to modify three parts
after copy-pasting this template, and never need to worry about corner cases and bugs in code any more:

a.  Correctly initialize the boundary variables left and right to specify search space. Only one rule: set up the
    boundary to include all possible elements;
b.  Decide return value. Is it return left or return left - 1? Remember this: after exiting the while loop, left is the
    minimal k satisfying the condition function;
c.  Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.

Advance Application: However, more often are the situations where the search space and search target are not so readily
                     available. Sometimes we won't even realize that the problem should be solved with binary search -->
                     we might just turn to dynamic programming or DFS and get stuck for a very long time.

Then "When can we use binary search?"
*   If we can discover some kind of monotonicity, for example,
    a. if condition(k) is True then;
    b. condition(k + 1) is True ==> then we can consider binary search.

Problem : Ugly Number III [Medium]
          Write a program to find the n-th ugly number. Ugly numbers are positive integers which are divisible by a or
          b or c.

          Nothing special. Still finding the Kth-Smallest. We need to design an enough function, given an input num,
          determine whether there are at least n ugly numbers less than or equal to num. Since a might be a multiple of
          b or c, or the other way round, we need the help of greatest common divisor to avoid counting duplicate
          numbers.

Example :

    Input: n = 3, a = 2, b = 3, c = 5
    Output: 4
    Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.

    Input: n = 4, a = 2, b = 3, c = 4
    Output: 6
    Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.

"""

import math


class Solution:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.ab = (a*b) // math.gcd(a, b)
        self.ac = (a*c) // math.gcd(a, c)
        self.bc = (b*c) // math.gcd(b, c)
        self.abc = (a*b*c) // math.gcd(a, b, c)

    def enough(self, num: int, n: int) -> bool:
        total = (num//self.a) + (num//self.b) + (num//self.c) - (num//self.ab) - (num//self.ac) - (num//self.bc) + \
                (num//self.abc)
        return total >= n

    def nth_ugly(self, n: int) -> int:
        left = 1
        right = 10 ** 10
        while left < right:
            mid = left + (right - left) // 2
            if self.enough(mid, n):
                right = mid
            else:
                left = mid + 1
        return left


# Example 1
a1, b1, c1 = 2, 3, 5
sol = Solution(a=a1, b=b1, c=c1)
print(sol.nth_ugly(3))

# Example 2
a1, b1, c1 = 2, 3, 4
sol = Solution(a=a1, b=b1, c=c1)
print(sol.nth_ugly(4))
