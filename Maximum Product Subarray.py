"""
Given an integer array nums, find a
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.





"""


# Python3 program to find Maximum Product Subarray

# Returns the product
# of max product subarray.


def maxSubarrayProduct(nums, n):
    # max positive product
    # ending at the current position
    max_ending_here = nums[0]

    # min negative product ending at the current position
    min_ending_here = nums[0]

    # Initialize overall max product
    max_so_far = nums[0]

    # /* Traverse through the array.
    # the maximum product subarray ending at an index will be the maximum of the element itself,
    # the product of element and max product ending previously and the min product ending previously. */
    for i in range(1, n):
        temp = max(max(nums[i], nums[i] * max_ending_here),
                   nums[i] * min_ending_here)
        min_ending_here = min(
            min(nums[i], nums[i] * max_ending_here), nums[i] * min_ending_here)
        max_ending_here = temp
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


# Driver code
arr = [1, -2, -3, 0, 7, -8, -2]
n = len(arr)
print(f"Maximum Sub array product is {maxSubarrayProduct(arr, n)}")
