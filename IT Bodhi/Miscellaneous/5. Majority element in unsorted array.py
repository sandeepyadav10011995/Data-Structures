"""
Problem : Majority element in unsorted array.

Approach 1: Using Hash Map
            TC: O(N) + O(N)
            SC: O(N)


Can we do this without space complexity and in O(N) time complexity?
Approach 2: Yes :: Using Voting Algorithm
        TC: O(N)
        SC: O(1)


Follow Up-: Given an integer array nums, find all the elements that appear more than N/3 times?
            Could you solve the problem in linear time and O(1) space?

Intuition -: nums :: array of length --> N

CASE 1: There can be at most one majority element which is more than N/2 times.

CASE 1: There can be at most two majority element which is more than N/3 times.

CASE 1: There can be at most three majority element which is more than N/4 times.

Therefore, we only need 4 variables
    - Two for holding potential candidates.
    - Two for holding corresponding counters.

"""

from collections import Counter

class Solution:
    @staticmethod
    def findMajorityUsingHashMap(arr: list[int]) -> int:
        counters = Counter(arr)
        maxCount, maxValue = 0, None
        for num, count in counters:
            if count > maxCount:
                maxValue = num

        return maxValue

    @staticmethod
    def findMajorityUsingVotingSystem(arr: list[int]) -> int:
        count = 0
        candidate = None

        for num in arr:
            if count == 0:
                candidate = num
                count += 1 if num == candidate else -1

        return candidate


class FollowUpSolution:
    @staticmethod
    def findMajority(arr: list[int]) -> list[int]:
        if not arr: return []

        count1, count2 = 0, 0
        candidate1, candidate2 = None, None

        for num in arr:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        return [candidate1, candidate2]