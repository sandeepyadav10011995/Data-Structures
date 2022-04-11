"""
    Cyclic Sort -: This pattern describes an interesting approach to deal with problems involving arrays containing
    numbers in a given range.

Question : Given an unsorted array containing n numbers ranging 1 to n. The array can have duplicates. This means that
           some numbers are missing. Find all the missing numbers.
Example -:
Input :
Output :

------------------------------------CODE-----------------------------------
"""


class CyclicSort:
    @staticmethod
    def swap(nums: list[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]

    @staticmethod
    def find_missing_numbers(nums: list[int]) -> list[int]:  # O(N) --> Inc i, O(N-1) --> Swap
        i = 0
        N = len(nums)
        while i < N:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                CyclicSort.swap(nums, i, j)
            else:
                i += 1
        missing_nums = []
        for k in range(N):
            if nums[k] != k+1:
                missing_nums.append(k+1)
        return missing_nums


arr = [5, 1, 5, 5, 5]
cs = CyclicSort()
miss_nums = cs.find_missing_numbers(nums=arr)
print(miss_nums)

"""
Overall TC : O(N) + O(N-1) + O(N) ~ O(N)
Overall SC: O(1) --> Inplace
"""
