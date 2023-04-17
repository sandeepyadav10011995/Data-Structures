"""
Longest Consecutive Sequence

Approach 1: Sort the array
            TC: O(NlogN) + O(N)
            SC: O(N)
Approach 2: HashMap or HashSet
           TC: O(N) + O(N) + O(N) ~ O(3N)  ~ O(N)
           SC: O(N)
           if the number less than num does not exist then start the count logic.
           else -> continue
           Worst Case -: Dec sorted array

"""

class Solution:
    @staticmethod
    def longestConsecutive(nums: list[int]) -> int:
        hashSet = set()
        for num in nums:
            hashSet.add(num)

        maxLongestConsecutive = 0
        for num in nums:
            if num-1 not in hashSet:
                curNum = num
                curLen = 1
                while curNum+1 in hashSet:
                    curNum += 1
                    curLen += 1
                maxLongestConsecutive = max(maxLongestConsecutive, curLen)
        return maxLongestConsecutive

