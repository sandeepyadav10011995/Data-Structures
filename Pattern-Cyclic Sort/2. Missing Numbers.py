"""
    Cyclic Sort -: This pattern describes an interesting approach to deal with problems involving arrays containing
    numbers in a given range.

Question : Given an unsorted array containing n numbers ranging 1 to n. The array can have duplicate. This means that
           one number is missing. Find the missing number.
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
    def find_missing_numbers(nums: list[int]) -> int:  # O(N) --> Inc i, O(N-1) --> Swap
        i = 0
        N = len(nums)
        while i < N:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                CyclicSort.swap(nums, i, j)
            else:
                i += 1
        for k in range(N):
            if nums[k] != k+1:
                return k+1
        return N


arr = [3, 1, 5, 4, 5]
cs = CyclicSort()
num = cs.find_missing_numbers(nums=arr)
print(num)

"""
Overall TC : O(N) + O(N-1) + O(N) ~ O(N)
Overall SC: O(1) --> Inplace
"""
