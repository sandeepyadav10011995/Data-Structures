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


Problem : First Bad Version [Easy]
          You are a product manager and currently leading a team to develop a new product. Since each version is
          developed based on the previous version, all the versions after a bad version are also bad. Suppose you have
          n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to
          be bad. You are given an API bool isBadVersion(version) which will return whether version is bad.

Example: Given n = 5, and version = 4 is the first bad version.
         call isBadVersion(3) -> false
         call isBadVersion(5) -> true
         call isBadVersion(4) -> true

         Then 4 is the first bad version.

"""


class Solution:
    def isBadVersion(self, m: int) -> bool:
        pass

    def firstBadVersion(self, n: int) -> int:
        # Search Space --> [1, 2, 3, ..., n]
        left = 1
        right = n

        while left < right:
            mid = left + (right-left)//2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
