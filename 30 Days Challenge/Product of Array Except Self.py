"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

"""


# Bruteforce Solution

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Calculate the product of all the elements
        product = 1
        for num in nums:
            product *= num
        
        output = []
        for num in nums:
            output.append(product//num)
        
        return output


"""
Note: Can we solve it without division and in O(n).
Follow up: Could we solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)

"""

# Using the Multiplication Associative Property

"""
 nums = [1, 2, 3, 4] --> LP =   [1, 1, 2, 6]
 nums = [1, 2, 3, 4] --> RP =   [24, 12, 4, 1]
 LP * RP --> ans = [24, 12, 8, 6]
 
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get the left product
        LP = [1]
        for i in range(1, len(nums)-1):
            LP.append(LP[-1] * nums[i])
        RP = [1]
        for i in range(len(nums)-1, 0, -1):
            value = RP[-1] * nums[i]
            RP.insert(0, value)
            
        output = [x*y for x, y in zip(LP, RP)]
        return output



