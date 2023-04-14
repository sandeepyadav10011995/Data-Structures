"""
Problem : Egg Drop: What is the Least amount of eggs drops?
          ==> "To guarantee that I will find the pivotal floor"

Case 1: If I have 1 Egg  ==> I will be conservative and try every floor one by one starting from floor 1 to all the way
                            up to Total Floors

Case 2: If we have 0 Floors ==> We need 0 trail(0 Egg), no matter the Egg amount given

Case 3: If we have 1 Floor ==> We need 1 trail(1 Egg), no matter the Egg amount given

Approach 1: Brute Force
Floor = 100
Egg = 2
Let say we will try to first egg at an interval of 10
Then;
        10      20      30      40      50      60      70      80      90      100
1        1
2
MaxDrop 9      11-19    21-29
Let say first egg breaks at 30 then min total drop = 1(10) + 1(20) + 1(30) + 9(21-29) = 12
Let say first egg breaks at 40 then min total drop = 1(10) + 1(20) + 1(30) + 1(40) + 9(31-39) = 13
Let say first egg breaks at 50 then min total drop = 1(10) + 1(20) + 1(30) + 1(40) + 1(50) + 9(31-39) = 14
Similarly,
Let say first egg breaks at 100 then min total drop = 9(10, 20, 30, 40, 50, 60, 70, 80, 90) +  9(91-99) = 18

Can we optimize this ?
D = 10      D-0     D-1     D-2     D-3     D-4     D-5     D-6     D-7     D-8     D-9
            0       9       8       7       6       5       4       3       2       1
Drops:      10      19      27      34      40      45      49      52      54      55
Let say first egg breaks at 10 then min total drop = 1(10) + 9(0-9) = 10
Let say first egg breaks at 19 then min total drop = 1(10) + 1(19) + 8(11-18)  = 10
Let say first egg breaks at 55 then min total drop = 10(10, 19, 27, 34, 45, 49, 52, 54, 55) = 10
If with D Eggs we can max cover Summation(D) Floors.
From 10 Eggs --> 55 Floors
Therefore;
        11 Eggs --> 66 Floors
        12 Eggs --> 78 Floors
        13 Eggs --> 91 Floors
        14 Eggs --> 105 Floors
        15 Eggs --> 120 Floors

Ex-: For 100 Floors, D = 14

Floor   14      27      39      50      60      69      77      84      90      95      99      102     104     105
Drops   14      14      14      14      14      14      14      14      14      14      14      14      14      14


                                    Break     Not Break
F(N, K) = Min(for i in 1-->N)(1 + Max(F(i-1, K-1), F(N-i, K)))
N==0 --> 0
K==1 --> N

"""
import math


class Solution:
    def eggDrops(self, totalEggs, totalFloors):
        # Base Case
        if totalFloors == 0:
            return totalFloors
        if totalEggs == 1:
            return totalFloors
        return min(max(self.eggDrops(totalEggs - 1, i - 1),
                       self.eggDrops(totalEggs, totalFloors - i))
                   for i in range(1, totalFloors + 1)
                   ) + 1

    def eggDropsMemo(self, totalEggs, totalFloors, memo):
        # Base Case
        if totalFloors == 0:
            return totalFloors
        if totalEggs == 1:
            return totalFloors
        if memo[totalEggs][totalFloors] < 0:
            memo[totalEggs][totalFloors] = min(max(self.eggDropsMemo(totalEggs - 1, i - 1, memo),
                       self.eggDropsMemo(totalEggs, totalFloors - i, memo))
                   for i in range(1, totalFloors + 1)
                   ) + 1
        return memo[totalEggs][totalFloors]


    @staticmethod
    def eggDropsBottomUp(totalEggs, totalFloors):
        memo = [[math.inf for _ in range(totalFloors+1)] for _ in range(totalEggs+1)]

        # Fill the details first 0 and 1st floor
        for egg in range(totalEggs+1):
            memo[egg][0] = 0
            memo[egg][1] = 1

        # Fill the details for 1 Egg
        for floor in range(1, totalFloors+1):
            memo[1][floor] = floor

        # Fill the rest details
        for egg in range(2, totalEggs+1):
            for floor in range(2, totalFloors+1):
                for attemptedFloor in range(1, floor+1):
                    costOfWorstOutcome = max(memo[egg-1][attemptedFloor-1], memo[egg][floor-attemptedFloor]) + 1
                    memo[egg][floor] = min(memo[egg][floor], costOfWorstOutcome)

        return memo[-1][-1]

sol = Solution()
print(sol.eggDrops(totalEggs=2, totalFloors=10))
mem = [[-1 for _ in range(11)] for _ in range(3)]
print(sol.eggDropsMemo(totalEggs=2, totalFloors=10, memo=mem))
print(sol.eggDropsBottomUp(totalEggs=2, totalFloors=10))