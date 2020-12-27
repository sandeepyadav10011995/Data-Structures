from functools import reduce

class Solution:
    all_three_sums = []
    def _twoSum(self, nums, root_index, seen, target):
        left = root_index + 1
        right = len(nums) - 1

        while left < right:
            three_num_sum = nums[root_index] + nums[left] + nums[right]

            if three_num_sum == target:
                number_list = [nums[left], nums[root_index], nums[right]]
                number_list.sort()
                signature = reduce(lambda acc, num: str(acc)+ str(num), number_list)

                if signature not in seen:
                    self.all_three_sums.append([nums[root_index], nums[left], nums[right]])
                    seen.add(signature)
                left += 1
                right -= 1
            elif three_num_sum < target:
                left += 1
            else:
                right -= 1

    def threeSum(self, nums, target=0):
        nums.sort()
        seen = set()
        second_last_index = len(nums) - 2

        for i in range(0, second_last_index):
            self._twoSum(nums, i, seen, target)

        return self.all_three_sums


nums = [-3, -1, 1, 0, 2, 10, -2, 8]
sol = Solution()
print(sol.threeSum(nums))
