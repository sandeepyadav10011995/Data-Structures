"""
Minimum Platforms | Greedy Algorithms
If the arrivals and departure times of all trains are given then what is the min platform we will need.
In this problem we can sort the respective arrays irrespective of the other
TC: 2NlogN + 2N
SC: O(1)

"""


class Solution2:
    @staticmethod
    def minPlatform(arrival: list[int], departure: list[int]) -> int:
        N = len(arrival)
        arrival.sort()
        departure.sort()

        minPlatform = 1
        platformNeeded = 1
        i, j = 0, 0
        while i < N and j < N:
            if arrival[i] <= departure[j]:
                platformNeeded += 1
                i += 1
            else:
                platformNeeded -= 1
                j += 1

            minPlatform = max(platformNeeded, minPlatform)

        return minPlatform
