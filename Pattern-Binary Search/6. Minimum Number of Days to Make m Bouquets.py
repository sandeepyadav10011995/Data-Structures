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

Problem : Minimum Number of Days to Make m Bouquets [Medium]
          Given an integer array bloomDay, an integer m and an integer k. We need to make m bouquets. To make a bouquet,
          you need to use k adjacent flowers from the garden. The garden consists of n flowers, the ith flower will
          bloom in the bloomDay[i] and then can be used in exactly one bouquet. Return the minimum number of days you
          need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

Examples:

    Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
    Output: 3
    Explanation: Let's see what happened in the first three days. x means flower bloomed and _ means flower didn't bloom
                 in the garden.

                We need 3 bouquets each should contain 1 flower.
                After day 1: [x, _, _, _, _]   // we can only make one bouquet.
                After day 2: [x, _, _, _, x]   // we can only make two bouquets.
                After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

    Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
    Output: -1
    Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is
                 impossible to get the needed bouquets and we return -1.

    Now that we've solved three advanced problems, this one should be pretty easy to do. The monotonicity of this
    problem is very clear: if we can make m bouquets after waiting for d days, then we can definitely finish that as
    well if we wait for more than d days.

"""


class Solution:
    @staticmethod
    def feasible(bloom_days: list[int], m: int, k: int, days: int) -> bool:
        bouquets = 0
        flowers = 0
        for bloom in bloom_days:
            if bloom > days:
                flowers = 0
            else:
                bouquets += (flowers + 1) // k
                flowers = (flowers + 1) % k
        return bouquets >= m

    @staticmethod
    def min_days(bloom_days: list[int], m: int, k: int) -> int:
        # Edge Case : Do we have enough kind/variety of flowers to make m bouquets with k flowers.
        if len(bloom_days) < m * k:
            return -1
        left = 1
        right = max(bloom_days)

        while left < right:
            mid = left + (right - left) // 2
            if Solution.feasible(bloom_days, m, k, mid):
                right = mid
            else:
                left = mid + 1
        return left


sol = Solution()

# Example 1
bloom_day1 = [1, 10, 3, 10, 2]
m1 = 3
k1 = 1
print(sol.min_days(bloom_days=bloom_day1, m=m1, k=k1))

# Example 2
bloom_day2 = [1, 10, 3, 10, 2]
m2 = 3
k2 = 2
print(sol.min_days(bloom_days=bloom_day2, m=m2, k=k2))
