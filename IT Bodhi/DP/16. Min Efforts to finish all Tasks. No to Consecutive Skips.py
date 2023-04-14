"""
Problem : Minimum efforts to finish all tasks. No to consecutive skips
Questions: Let say there are doctors and patient and doctors are not allowed to skip consecutive patients.
What would be the minimum tie time to finish all the patients.

Ex-: arr = [10, 5, 2, 3, 20, 40, 3]
Constraints: No consecutive skips

F(i) = min( arr[i] + F(i-1) # No Skip + Do last task
            arr[i-1] + F(i-2) # Skip the last task + Then second last task is must)

Follow-Up : No more than two consecutive skipping !!

F(i) = min(F(i-1) + arr[i], # No skipping of Last
           F(i-2) + arr[i-1] # Skipping last but not second last
           F(i-3) + arr[i-2] # Skipping both the last and second last)

"""


class Solution:
    def minTasksEfforts(self, arr, index):
        # Base Case
        if index < 0:
            return 0
        if index == 0:
            return arr[index]
        if index == 1:
            return min(arr[index-1], arr[index])

        return min(self.minTasksEfforts(arr, index-1) + arr[index],
                   self.minTasksEfforts(arr, index-2) + arr[index-1])
    """
    TC: O(2^N)
    SC: O(N) --> Call Stack
    """


    def minTasksEffortsMemo(self, arr, index, memo):
        # Base Case
        if index < 0:
            return 0
        if index == 0:
            return arr[index]
        if index == 1:
            return min(arr[index-1], arr[index])
        if memo[index] < 0:
            memo[index] = min(self.minTasksEffortsMemo(arr, index-1, memo) + arr[index],
                              self.minTasksEffortsMemo(arr, index-2, memo) + arr[index-1])
        return memo[index]
    """
    TC: O(2*N)
    SC: O(N)
    """

    @staticmethod
    def minTasksEffortsBottomUp(arr):
        N = len(arr)
        memo = [-1 for _ in range(N+1)]
        memo[0] = 0
        memo[1] = arr[0]
        memo[2] = min(arr[0], arr[1])

        for i in range(3, N+1):
            memo[i] = min(memo[i-1]+arr[i-1],
                          memo[i-2]+arr[i-2])

        return memo[-1]
    """
    TC: O(N)
    SC: O(N)
    """

sol = Solution()
print(sol.minTasksEfforts(arr=[10, 5], index=1))
print(sol.minTasksEfforts(arr=[10, 5, 2], index=2))
print(sol.minTasksEfforts(arr=[10, 5, 2, 3], index=3))
print(sol.minTasksEfforts(arr=[10, 5, 2, 3, 20], index=4))
print(sol.minTasksEfforts(arr=[10, 5, 2, 3, 20], index=4))
print(sol.minTasksEfforts(arr=[10, 5, 2, 3, 20, 40, 3], index=6))
print(sol.minTasksEfforts(arr=[10, 5, 2, 3, 20, 40, 2], index=6))
print("*"*100)
print(sol.minTasksEffortsMemo(arr=[10, 5], index=1, memo=[-1 for _ in range(2)]))
print(sol.minTasksEffortsMemo(arr=[10, 5, 2], index=2, memo=[-1 for _ in range(3)]))
print(sol.minTasksEffortsMemo(arr=[10, 5, 2, 3], index=3, memo=[-1 for _ in range(4)]))
print(sol.minTasksEffortsMemo(arr=[10, 5, 2, 3, 20], index=4, memo=[-1 for _ in range(5)]))
print(sol.minTasksEffortsMemo(arr=[10, 5, 2, 3, 20], index=4, memo=[-1 for _ in range(5)]))
print(sol.minTasksEffortsMemo(arr=[10, 5, 2, 3, 20, 40, 3], index=6, memo=[-1 for _ in range(7)]))
print(sol.minTasksEffortsMemo(arr=[10, 5, 2, 3, 20, 40, 2], index=6, memo=[-1 for _ in range(7)]))
print("*"*100)
print(sol.minTasksEffortsBottomUp(arr=[10, 5, 2, 3, 20, 40, 3]))
print(sol.minTasksEffortsBottomUp(arr=[10, 5, 2, 3, 20, 40, 2]))

"""
Follow-Up : No more than two consecutive skipping !!

F(i) = min(F(i-1) + arr[i], # No skipping of Last
           F(i-2) + arr[i-1] # Skipping last but not second last
           F(i-3) + arr[i-2] # Skipping both the last and second last)

"""


class FollowUpSolution:
    def minTasksEfforts(self, arr, index):
        # Base Case
        if index < 0:
            return 0
        if index == 0:
            return arr[index]
        if index == 1:
            return min(arr[index - 1], arr[index])
        if index == 2:
            return min(arr[index], arr[index-1], arr[index-2])

        return min(self.minTasksEfforts(arr, index - 1) + arr[index],
                   self.minTasksEfforts(arr, index - 2) + arr[index - 1],
                   self.minTasksEfforts(arr, index - 3) + arr[index - 2]
                   )

    """
    TC: O(2^N)
    SC: O(N) --> Call Stack
    """

    def minTasksEffortsMemo(self, arr, index, memo):
        # Base Case
        if index < 0:
            return 0
        if index == 0:
            return arr[index]
        if index == 1:
            return min(arr[index - 1], arr[index])
        if memo[index] < 0:
            memo[index] = min(self.minTasksEffortsMemo(arr, index - 1, memo) + arr[index],
                              self.minTasksEffortsMemo(arr, index - 2, memo) + arr[index - 1])
        return memo[index]

    """
    TC: O(2*N)
    SC: O(N)
    """

    @staticmethod
    def minTasksEffortsBottomUp(arr):
        N = len(arr)
        memo = [-1 for _ in range(N + 1)]
        memo[0] = 0
        memo[1] = arr[0]
        memo[2] = min(arr[0], arr[1])

        for i in range(3, N + 1):
            memo[i] = min(memo[i - 1] + arr[i - 1],
                          memo[i - 2] + arr[i - 2])

        return memo[-1]

    """
    TC: O(N)
    SC: O(N)
    """
print("*"*50+"Follow Up Solution"+"*"*50)
followUpSolution = Solution()
print(followUpSolution.minTasksEfforts(arr=[10, 5, 2], index=2))
print(followUpSolution.minTasksEfforts(arr=[10, 5, 2, 3], index=3))
print(followUpSolution.minTasksEfforts(arr=[10, 5, 2, 3, 20], index=4))
print(followUpSolution.minTasksEfforts(arr=[10, 5, 2, 3, 20], index=4))
print(followUpSolution.minTasksEfforts(arr=[10, 5, 2, 3, 20, 40, 3], index=6))
print(followUpSolution.minTasksEfforts(arr=[10, 5, 2, 3, 20, 40, 2], index=6))
