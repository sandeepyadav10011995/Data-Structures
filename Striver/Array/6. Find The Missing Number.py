"""
Problem : Find the Missing Number

Brute Force -: Search for the num in the array (1-N)
              TC: O(N^2)
              SC: O(1)

Better Solution: Hashing
                Mark the num as present in the hash else the is not present (1-N)
                TC: O(N)Map + O(N)Array ~ O(2N)
                SC: O(N)

Optimal Solution: Placing the num at it's right position
                  TC: O(2N)
                  SC: O(1)

                 Cumulative Sum : sumSum = n*(n+1)/2
                                  arrSum = sum(Arr)
                                  missingNum = cumSum-arrSum
                 TC: O(N)
                 SC: O(1)

                 XOR Logic: As it avoids integer overflow
                     number ^ number = 0
                     number ^ 0 = number

"""
import datetime


class Solution:
    @staticmethod
    def missingNumberCumSum(nums: list[int], N: int) -> int:
        start = datetime.datetime.now()
        cumSum = N*(N+1)//2
        arrSum = 0
        for num in nums:
            arrSum += num

        missingNum = cumSum - arrSum
        end = datetime.datetime.now()
        print(end-start)
        return missingNum

    @staticmethod
    def missingNumberXORLogic1(nums: list[int], N: int) -> int:  # TC: O(2N)
        start = datetime.datetime.now()
        XOR1 = 0
        for i in range(N):
            XOR1 ^= (i+1)

        XOR2 = 0
        for j in range(N-1):
            XOR2 ^= nums[j]
        end = datetime.datetime.now()
        print(end - start)
        return XOR1 ^ XOR2

    @staticmethod
    def missingNumberXORLogic2(nums: list[int], N: int) -> int:  # TC: O(N)
        start = datetime.datetime.now()
        XOR1 = 0
        XOR2 = 0
        for j in range(N-1):  # XOR2 = 1^2^4^5
            XOR2 ^= nums[j]
            XOR1 ^= (j + 1)

        # Apply XOR1 Nth as well XOR1 = 1^2^3^4^5
        XOR1 ^= N
        end = datetime.datetime.now()
        print(end - start)
        return XOR1 ^ XOR2


sol = Solution()
print(sol.missingNumberCumSum(nums=[1, 2, 4, 5], N=5))
print(sol.missingNumberXORLogic1(nums=[1, 2, 4, 5], N=5))
print(sol.missingNumberXORLogic2(nums=[1, 2, 4, 5], N=5))
print(sol.missingNumberXORLogic1(nums=[3,1,2,5,6], N=5))
