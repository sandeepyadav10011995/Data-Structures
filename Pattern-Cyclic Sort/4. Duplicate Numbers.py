"""
    Cyclic Sort -: This pattern describes an interesting approach to deal with problems involving arrays containing
    numbers in a given range.

Question : Given an unsorted array containing n numbers ranging 1 to n. The array can have duplicates. This means that
           some numbers are missing. Find all the duplicates.
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
    def find_duplicates(nums: list[int]) -> int:  # O(N) --> Inc i, O(N-1) --> Swap
        i = 0
        N = len(nums)
        while i < N:
            if nums[i] <= i+1:
                j = nums[i] - 1
                if nums[i] != nums[j]:
                    CyclicSort.swap(nums, i, j)
                else:
                    return nums[i]
            else:
                i += 1
        return -1


arr = [3, 1, 2, 2, 5]
cs = CyclicSort()
num = cs.find_duplicates(nums=arr)
print(num)


"""
Overall TC : 
Overall SC: 
"""
