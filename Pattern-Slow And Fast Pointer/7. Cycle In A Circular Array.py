"""
The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two
pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when
dealing with cyclic LinkedLists or arrays.

By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to
meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

Problem Statement: We are given an array containing positive and negative numbers. Suppose the array contains a number
                   ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is
                   negative move backwards ‘M’ indices. You should assume that the array is circular which means two
                   things:

                   a. If, while moving forward, we reach the end of the array, we will jump to the first element to
                      continue the movement.
                   b. If, while moving backward, we reach the beginning of the array, we will jump to the last element
                      to continue the movement.

                   Write a method to determine if the array has a cycle. The cycle should have more than one element and
                   should follow one direction which means the cycle should not contain both forward and backward
                   movements.

Algo: This problem involves finding a cycle in the array and, as we know, the Fast & Slow pointer method is an efficient
      way to do that. We can start from each index of the array to find the cycle. If a number does not have a cycle we
      will move forward to the next element. There are a couple of additional things we need to take care of:

      a. As mentioned in the problem, the cycle should have more than one element. This means that when we move a
         pointer forward, if the pointer points to the same element after the move, we have a one-element cycle.
         Therefore, we can finish our cycle search for the current element.

      b. The other requirement mentioned in the problem is that the cycle should not contain both forward and backward
         movements. We will handle this by remembering the direction of each element while searching for the cycle. If
         the number is positive, the direction will be forward and if the number is negative, the direction will be
         backward. So whenever we move a pointer forward, if there is a change in the direction, we will finish our
         cycle search right there for the current element.

Example 1:
Input: [1, 2, -1, 2, 2]
Output: true
Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0

Example 2:
Input: [2, 2, -1, 2]
Output: true
Explanation: The array has a cycle among indices: 1 -> 3 -> 1

Example 3:
Input: [2, 1, -1, -2]
Output: false
Explanation: The array does not have any cycle.

"""
from typing import List


class CircularArrayCycle:
    @staticmethod
    def circular_array_loop_exists(nums: List[int]) -> bool:
        # The Cycle can start from any index
        for i in range(len(nums)):
            is_forward = nums[i] >= 0  # If we are moving forward or not
            slow, fast = i, i
            # If slow or fast becomes "-1", this means we can't find cycle for this number
            while True:
                # Move one step for slow pointer
                slow = CircularArrayCycle.find_next_index(nums, is_forward, slow)
                # Move one step for fast pointer
                fast = CircularArrayCycle.find_next_index(nums, is_forward, fast)
                if fast != -1:
                    # Move another step for fast pointer
                    fast = CircularArrayCycle.find_next_index(nums, is_forward, fast)
                if slow == -1 or fast == -1 or slow == fast:
                    break
            if slow != -1 and slow == fast:
                return True
        return False

    @staticmethod
    def find_next_index(nums: List[int], is_forward: bool, current_index: int) -> int:
        direction = nums[current_index] >= 0
        # Edge Case 1: Change in direction, return -1
        if is_forward != direction:
            return -1
        next_index = (current_index + nums[current_index]) % len(nums)

        # Edge Case 2: One Element Cycle, return -1
        if next_index == current_index:
            return -1
        return next_index


def main():
    cac = CircularArrayCycle()
    print(cac.circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(cac.circular_array_loop_exists([2, 2, -1, 2]))
    print(cac.circular_array_loop_exists([2, 1, -1, -2]))


main()


"""
Time Complexity: O(N^2)
Space Complexity: O(1)
"""




