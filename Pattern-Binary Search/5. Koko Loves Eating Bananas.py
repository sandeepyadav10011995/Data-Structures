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

Problem : Koko Eating Bananas [Medium]
    Koko loves to eat bananas. There are N piles of bananas, the i-th pile has piles[i] bananas. The guards have gone
    and will come back in H hours. Koko can decide her bananas-per-hour eating speed of K. Each hour, she chooses some
    pile of bananas, and eats K bananas from that pile. If the pile has less than K bananas, she eats all of them
    instead, and won't eat any more bananas during this hour.

    Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back. Return the
    minimum integer K such that she can eat all the bananas within H hours.

Algo : Initialize;
            left = 1
            right = max(piles)
            condition ~ feasible: speed

Example :
    Input: piles = [3,6,7,11], H = 8
    Output: 4

    Input: piles = [30,11,23,4,20], H = 5
    Output: 30

    Input: piles = [30,11,23,4,20], H = 6
    Output: 23

"""


class Solution:
    def __init__(self) -> None:
        self.piles = []
        self.H = 0

    def feasible(self, speed: int) -> bool:
        return sum(((pile - 1) // speed) + 1 for pile in self.piles) <= self.H  # faster

    def min_eating(self, piles: list[int], H: int) -> int:
        self.piles = piles
        self.H = H

        left = 1  # Bcz Koko can only choose 1 pile of bananas only
        right = max(self.piles)

        while left < right:
            mid = left + (right - left) // 2
            if self.feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left


sol = Solution()
# Example 1
piles1 = [3, 6, 7, 11]
H1 = 8
print(sol.min_eating(piles=piles1, H=H1))

# Example 2
piles2 = [30, 11, 23, 4, 20]
H2 = 5
print(sol.min_eating(piles=piles2, H=H2))

# Example 3
piles3 = [30, 11, 23, 4, 20]
H3 = 6
print(sol.min_eating(piles=piles3, H=H3))
