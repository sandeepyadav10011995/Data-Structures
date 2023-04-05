"""
Problem : Count of all sub-array which sum is a multiple of K
Edge Cases : When the array contains zero and negative values.

Example -: arr=[4, 2, 3, 4, 2, 7, 1, 1, 3, 1, 5] K=3

index       0   1   2   3   4   5   6   7   8   9   10

cumSum      4   6   9   13  15  22  23  24  27  28  33
mod         1   0   0   1   0   1   2   0   0   1   0
arr         4   2   3   4   2   7   1   1   3   1   5
count       0   1   2   1   3   2   0   4   5   3   6

prefixModMap = {0: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
                1: 1 -> 2 -> 3 -> 4
                2: 1

"""


class SubArray2:
    @staticmethod
    def countSubArrayWithSumK(nums: list[int], K: int) -> int:
        N = len(nums)
        count = 0
        prefixCountMap = {0: 1}
        cumSum = 0

        for i in range(N):
            cumSum += nums[i]
            mod = cumSum % K
            if mod in prefixCountMap:
                count += prefixCountMap[mod]
                prefixCountMap[mod] += 1
            else:
                prefixCountMap[mod] = 1
            # Increment the count of sub-arrays whose sum is a multiple of K by one, if r is 0
            # (which means the running sum is a multiple of K)
            if mod == 0:
                count += 1

        return count

    @staticmethod
    def countSubArrayWithSumK2(nums: list[int], K: int) -> int:
        N = len(nums)
        count = 0
        prefixModulusMap = {0: 1}
        cumSum = 0

        for i in range(N):
            cumSum += nums[i]
            mod = cumSum % K
            if mod in prefixModulusMap:
                count += prefixModulusMap[mod]
            # Increment the count of sub-arrays whose sum is a multiple of K by one, if r is 0
            # (which means the running sum is a multiple of K)
            if mod == 0:
                count += 1
            prefixModulusMap[mod] = prefixModulusMap.get(mod, 0) + 1

        return count


print("*"*100)
sb2 = SubArray2()
arr=[4, 2, 3, 4, 2, 7, 1, 1, 3, 1, 5]
print(sb2.countSubArrayWithSumK(nums=arr, K=3))
print(sb2.countSubArrayWithSumK2(nums=arr, K=3))