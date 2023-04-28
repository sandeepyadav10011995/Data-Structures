"""
Problem : Find the number that appears once and the other twice

BruteForce: Linear Search and get the count of each number
            TC: O(N^2)

Better: Hashing --> Arr of size maxNumber+1

        Map <Key, count>
        Unordered Map -: O(N)
        TC: O(N) + O(N/2 + 1) ~ O(3N/2 + 1) ~O(N)
        SC: O(N/2+1) ~ O(N)

        Ordered Map -: O(N*logM) M = N/2+1
        TC: O(N*logM) + O(M)
        SC: O(M)

Optimal: XOR Logic
        TC: O(N)
        SC: O(1)
"""


class Solution:
    @staticmethod
    def findElementAppearingOnceXORLogic(nums: list[int]) -> int:
        onceElement = 0
        for num in nums:
            onceElement ^= num

        return onceElement


sol = Solution()
print(sol.findElementAppearingOnceXORLogic(nums=[1, 1, 2, 3, 3, 4, 4]))
