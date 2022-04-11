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


Problem : Capacity To Ship Packages Within D Days [Medium]
          A conveyor belt has packages that must be shipped from one port to another within D days. The i-th package on
          the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt
          (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

        Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being
        shipped within D days.

Algo : Binary search probably would not come to our mind when we first meet this problem. We might automatically treat
       weights as search space and then realize we've entered a dead end after wasting lots of time. In fact, we are
       looking for the minimal one among all feasible capacities.

       We dig out the monotonicity of this problem: if we can successfully ship all packages within D days with capacity
       m, then we can definitely ship them all with any capacity larger than m.

       Initialize;
             left = max(weights) ==>  Otherwise the conveyor belt couldn't ship the heaviest package
             right = sum(weights) ==> Otherwise, we can ship all packages in one day
             condition ~ feasible : This can run in a greedy way:
                                    a.  If there's still room for the current package, we put this package onto the
                                        conveyor belt;
                                    b.  otherwise we wait for the next day to place this package.
                                    c.  If the total days needed exceeds D, we return False, otherwise we return True.

       Next, we need to initialize our boundary correctly. Obviously capacity should be at least max(weights), otherwise
       the conveyor belt couldn't ship the heaviest package. On the other hand, capacity need not be more than
       sum(weights), because then we can ship all packages in just one day.

Example :
    Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
    Output: 15
    Explanation:
        A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
            1st day: 1, 2, 3, 4, 5
            2nd day: 6, 7
            3rd day: 8
            4th day: 9
            5th day: 10

    Note: The cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into
          parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

"""


class Solution:
    def __init__(self) -> None:
        self.weights = []
        self.D = 0

    def feasible(self, capacity: int) -> bool:
        days = 1
        total = 0
        for weight in self.weights:
            total += weight
            if total > capacity:  # Too heavy; wait for next day
                total = weight
                days += 1
                if days > self.D:  # Cannot ship within D-Days
                    return False
        return True

    def ship_within_d_days(self, weights: list[int], D: int) -> int:
        self.weights = weights
        self.D = D
        left = max(self.weights)
        right = sum(self.weights)

        while left < right:
            mid = left + (right - left) // 2
            if self.feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left


sol = Solution()
w1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d1 = 5
print(sol.ship_within_d_days(weights=w1, D=d1))

