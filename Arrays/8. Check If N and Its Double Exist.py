"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M (N = 2 * M).
More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:
Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example 3:
Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.


Constraints:
2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3

"""


class Solution:
    def checkIfExist(self, nums):
        res = set(arr)
        zero_count = 0
        for num in arr:
            if num == 0:
                zero_count += 1
                continue
            if num * 2 in res:
                return True
        if zero_count > 1:
            return True
        return False

arr = [-2,0,10,-19,4,6,-8]
sol = Solution()
print(sol.checkIfExist(arr))
