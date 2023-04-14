"""
Problem : Max profit from stealing. No consecutive houses. ==> Constraint
Ex-: arr = [20, 15, 2, 3, 40]
F(i) = X : This means from 0-i maxSteal = X
F(i) = max( F(i-1) --> Not taking the last element
            F(i-2) + arr[i] --> Taking the last element

    TC: O(2^N)
    SC: O(N)

Follow Up -: No more than two consecutive are allowed !!
F(i) = max(F(i-1), # Skipping the last element: X arr[i]
           arr[i] + F(i-2),   # Taking the last element and skipping i-1: X, arr[i]
           arr[i] + arr[i-1] + F(i-3), # Taking the last two elements: arr[i], arr[i-1]
           )

"""

class Solution:
    def maxStealing(self, arr, index):
        # Base Case
        if index == 0:
            return arr[0]
        if index < 0:
            return 0

        return max(self.maxStealing(arr, index-1),
                   arr[index] + self.maxStealing(arr, index-2))
    """
    TC: O(2^N)
    SC: O(N) --> Call Stack
    """

    def maxStealingMemo(self, arr, index, memo):
        # Base Case
        if index == 0:
            return arr[0]
        if index < 0:
            return 0
        if memo[index] < 0:
            memo[index] = max(self.maxStealingMemo(arr, index - 1, memo),
                              arr[index] + self.maxStealingMemo(arr, index - 2, memo))
        return memo[index]
    """
    TC: O(2*N)
    SC: O(N)
    """

    @staticmethod
    def maxStealingBottomUp(arr):
        N = len(arr)
        memo = [-1 for _ in range(N+1)]
        memo[0] = 0
        memo[1] = arr[0]

        for i in range(2, N+1, 2):
            memo[i] = max(memo[i-1], memo[i-2]+arr[i-1])
        for i in range(3, N+1, 2):
            memo[i] = max(memo[i-1], memo[i-2]+arr[i-1])

        return memo[-1]
    """
    TC: O(N)
    SC: O(N)
    """


sol = Solution()
print(sol.maxStealing(arr=[20, 15, 2, 3, 40], index=4))
print(sol.maxStealingMemo(arr=[20, 15, 2, 3, 40], index=4, memo=[-1 for _ in range(5)]))
print(sol.maxStealingBottomUp(arr=[20, 15, 2, 3, 40]))


"""
Follow Up Solution-:
F(i) = max(F(i-1), # Skipping the last element: X arr[i]
           arr[i] + F(i-2),   # Taking the last element and skipping i-1: X, arr[i]
           arr[i] + arr[i-1] + F(i-3), # Taking the last two elements: arr[i], arr[i-1]
           )
"""

class FollowUpSolution:
    def maxStealing(self, arr, index):
        # Base Case
        if index < 0:
            return 0
        if index == 0:
            return arr[0]

        return max(self.maxStealing(arr, index-1),
                   arr[index] + self.maxStealing(arr, index-2),
                   arr[index] + arr[index-1] + self.maxStealing(arr, index-3)
                   )
    """
    TC: O(3^N)
    SC: O(N) --> Call Stack
    """

    def maxStealingMemo(self, arr, index, memo):
        # Base Case
        if index < 0:
            return 0
        if index == 0:
            return arr[0]
        if memo[index] < 0:
             memo[index] = max(self.maxStealing(arr, index - 1),
                               arr[index] + self.maxStealing(arr, index - 2),
                               arr[index] + arr[index - 1] + self.maxStealing(arr, index - 3)
                               )

        return memo[index]
    """
    TC: O(3*N)
    SC: O(N)
    """

    @staticmethod
    def maxStealingBottomUp(arr):
        N = len(arr)
        memo = [-1 for _ in range(N + 1)]
        memo[0] = 0
        memo[1] = arr[0]
        memo[2] = arr[0] + arr[1]

        for i in range(4, N + 1, 2):
            memo[i] = max(memo[i-1], memo[i-2]+arr[i-1], memo[i-3]+arr[i-1]+arr[i-2])
        for i in range(3, N + 1, 2):
            memo[i] = max(memo[i-1], memo[i-2]+arr[i-1], memo[i-3]+arr[i-1]+arr[i-2])

        return memo[-1]


print("*"*100)
followUpSolution = FollowUpSolution()
print(followUpSolution.maxStealing(arr=[20, 15, 2, 3, 40], index=4))
print(followUpSolution.maxStealingMemo(arr=[20, 15, 2, 3, 40], index=4, memo=[-1 for _ in range(5)]))
print(followUpSolution.maxStealingBottomUp(arr=[20, 15, 2, 3, 40]))
