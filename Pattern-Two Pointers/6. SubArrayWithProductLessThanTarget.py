"""
In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain
constraints, the Two Pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a
sub-array.

Problem Statement : Given an array with positive numbers and a positive target number, find all of its contiguous
                    sub-arrays whose product is less than the target number.

Algo : This problem follows the Sliding Window and the Two Pointers pattern and shares similarities with Triplets with
       Smaller Sum with two differences:
In this problem, the input array is not sorted.
Instead of finding triplets with sum less than a target, we need to find all sub-arrays having a product less than the
target. The implementation will be quite similar to Triplets with Smaller Sum.

Example 1:
Input: [2, 5, 3, 10], target=30
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous sub-arrays whose product is less than the target.

Example 2:
Input: [8, 2, 6, 5], target=50
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
Explanation: There are seven contiguous sub-arrays whose product is less than the target.

"""
from typing import List
from collections import deque


class SubArrayWithProductLessThanTarget:
    @staticmethod
    def find_sub_arrays(nums: List[int], target: int) -> List[List[int]]:
        result = []
        product = 1
        left = 0
        for right in range(len(nums)):
            product *= nums[right]
            while product >= target and left <= right:
                product /= nums[left]
                left += 1
            # Since all the product of all numbers from left to right is less than the target therefore,
            # all sub-arrays from left to right will have a product less than the target too; to avoid duplicates, we
            # will start with a sub-array containing only nums[right and then extend it.
            temp_list = deque()
            for i in range(right, left-1, -1):
                temp_list.appendleft(nums[i])
                result.append(list(temp_list))
        return result


def main():
    sawpltt = SubArrayWithProductLessThanTarget()
    print(sawpltt.find_sub_arrays([2, 5, 3, 10], 30))
    print(sawpltt.find_sub_arrays([8, 2, 6, 5], 50))


main()


"""
Time Complexity: N(for-loop)*N*N(creating sub-arrays) ==> O(N^3)
Space Complexity: O(N)
"""
