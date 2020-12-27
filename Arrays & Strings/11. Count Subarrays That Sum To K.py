class Solution:
    def subarraySumToK1(self, nums, k): # Time Complexity --> O(N^2)
        cum_sum = [nums[0]]
        for i in range(1, len(nums)):
            cum_sum.append(cum_sum[i-1] + nums[i])

        count = 0
        for start in range(len(nums)):
            for end in range(start, len(nums)):
                temp_sum = cum_sum[end]
                if start != 0:
                    temp_sum -= cum_sum[start-1]
                if temp_sum == k:
                    count += 1
        return count

    def subarraySumToK2(self, nums, k): # Time Complexity --> O(N)
        mapping = {0: 1}
        total = 0
        count = 0
        for i in range(len(nums)):
            total += nums[i]
            if total-k in mapping:
                count += mapping[total-k]
            if total in mapping:
                mapping[total] += 1
            else:
                mapping[total] = 1

        return count

nums = [3, 7, -4, -2, 1, 5]
k = 3
sol = Solution()
print(sol.subarraySumToK1(nums, k))
print(sol.subarraySumToK2(nums, k))
