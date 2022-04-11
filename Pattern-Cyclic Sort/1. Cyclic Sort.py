"""
    Cyclic Sort -: This pattern describes an interesting approach to deal with problems involving arrays containing
    numbers in a given range.

Question : Given an unsorted array containing n numbers ranging 1 to n. Sort the array in O(N) time !!
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
    def sort_numbers(nums: list[int]) -> list[int]:  # O(N) --> Inc i, O(N-1) --> Swap
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                CyclicSort.swap(nums, i, j)
            else:
                i += 1
        return nums


arr = [3, 1, 5, 4, 2]
cs = CyclicSort()
result = cs.sort_numbers(nums=arr)
print(result)

"""
Overall TC : O(N) + O(N-1) ~ O(N)
Overall SC: O(1) --> Inplace
"""
