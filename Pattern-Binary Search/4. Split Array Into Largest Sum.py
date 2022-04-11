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


Problem : Split Array Largest Sum [Hard]
          Given an array which consists of non-negative integers and an integer m, you can split the array into m
          non-empty continuous sub-arrays. Write an algorithm to minimize the largest sum among these m sub-arrays.

Algo : Initialize;
            left = max(nums)
            right = sum(nums)
            condition ~ feasible: Given an input threshold, then decide if we can split the array into several
                                  sub-arrays such that every sub-array-sum is less than or equal to threshold.
        Monotonicity Of The Problem :
            a.  If feasible(m) is True;
            b.  All the inputs larger than m can satisfy feasible function



Example:
    Input:
        nums = [7,2,5,10,8]
        m = 2
    Output:
        18

    Explanation:
        There are four ways to split nums into two sub-arrays. The best way is to split it into [7,2,5] and [10,8],
        where the largest sum among the two sub-arrays is only 18.

"""


class Solution:
    def __init__(self) -> None:
        self.nums = []
        self.m = 0

    def feasible(self, threshold: int) -> bool:
        count = 1
        total = 0
        for num in self.nums:
            total += num
            if total > threshold:  # Too large; put it in next sub-array
                total = num
                count += 1
                if count > self.m:  # Cannot split within m sub-arrays
                    return False
        return True

    def split_array(self, nums: list[int], m: int) -> int:
        self.nums = nums
        self.m = m
        left = max(self.nums)
        right = sum(self.nums)

        while left < right:
            mid = left + (right - left) // 2
            if self.feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left


sol = Solution()
n1 = [7, 2, 5, 10, 8]
m1 = 2
print(sol.split_array(nums=n1, m=m1))
