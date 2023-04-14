"""
Problem : Gas station to complete the entire trip.
Approach 1: One Pass :: Check for every station
        TC : O(N^2)
Edge Case :: It is impossible to perform the trip if sum(gas) < sum(cost)
            Return -1

Approach 2: Single Pass with Cumulative Sum
    TC: O(N)

"""


class GasStation:
    @staticmethod
    def canCompleteTrip(gas: list[int], cost: list[int]) -> int:
        N = len(gas)
        totalTank = 0
        curTank = 0
        startStation = 0
        for i in range(N):
            totalTank += gas[i] - cost[i]
            curTank += gas[i] - cost[i]
            if curTank < 0:  # If one couldn't get here
                startStation = i+1  # Pick the next station as the start station
                curTank = 0  # start with an empty tank

        return startStation if totalTank >= 0 else -1

