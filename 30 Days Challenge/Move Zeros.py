"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

"""
1-->        [0 1 0 3 12]
            l
               r
2-->        [1 0 0 3 12]            
               l
                   r
3-->        [1 3 0 0 12]
                 l
                      r 
4-->        [1 3 12 0 10]
"""

def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    N = len(nums)
    l = 0
    r = 0
    while r < N:
        if nums[l] == 0 and nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
        elif nums[r] == 0:
            r += 1
        else:
            l += 1
            r += 1
