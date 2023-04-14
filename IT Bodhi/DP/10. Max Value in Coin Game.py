"""
Problem : Max value in coin game
Ex-: [5, 10, 15, 2, 7, 3]
You can pick up the coin either from Left or Right side
There are two players
    0   1   2   3   4   5
   [5,  10, 15, 2,  7,  3]
A   5
B   10

In this recursion is not absolute but relative on the other person choice
                                If we select i then remaining window is (i+1---j) # Left
                                If we select j then remaining window is (i---j-1) # Right
maxGain(i, j) = max(arr[i] + min(maxGain(i+2,j), maxGain(i+1, j-1)) # Left
                    arr[j] + min(maxGain(i+1,j-1), maxGain(i, j-2))) # Right

DP --> LENGTH WISE  --> 2, 3, 4, 5

"""
import datetime


class Solution:
    def maxValueCoinGame(self, arr, start, end) -> int:
        # Base Case
        if start == end:
            return arr[start]
        if start == end-1:  # Only two are left
            return max(arr[start], arr[start+1])

        return max(arr[start] + min(self.maxValueCoinGame(arr, start+2, end), self.maxValueCoinGame(arr, start+1, end-1)),
                   arr[end] + min(self.maxValueCoinGame(arr, start+1, end-1), self.maxValueCoinGame(arr, start, end-2)))

    def maxValueCoinGameMemo(self, arr, start, end, memo) -> int:
        # Base Case
        if start == end:
            return arr[start]
        if start == end - 1:  # Only two are left
            return max(arr[start], arr[start + 1])
        if memo[start][end] < 0:
            memo[start][end] = max(arr[start] + min(self.maxValueCoinGame(arr, start + 2, end),
                                        self.maxValueCoinGame(arr, start + 1, end - 1)),
                       arr[end] + min(self.maxValueCoinGame(arr, start + 1, end - 1),
                                      self.maxValueCoinGame(arr, start, end - 2)))
        return memo[start][end]

    # @staticmethod
    # def maxValueCoinGameBottomUp(arr):


nums = [5, 10, 15, 2, 7, 3]
sol = Solution()
t1 = datetime.datetime.now()
print(sol.maxValueCoinGame(arr=nums, start=0, end=5))
t2 = datetime.datetime.now()
print(t2-t1)
t3 = datetime.datetime.now()
print(sol.maxValueCoinGameMemo(arr=nums, start=0, end=5, memo=[[-1 for _ in range(6)] for _ in range(6)]))
t4 = datetime.datetime.now()
print(t4-t3)

