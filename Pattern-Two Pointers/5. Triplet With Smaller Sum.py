"""
In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain
constraints, the Two Pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a
sub-array.

Problem Statement : Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

Algo: This problem follows the Two Pointers pattern and shares similarities with Triplet Sum to Zero. The only
      difference is that, in this problem, we need to find the triplets whose sum is less than the given target. To meet
      the condition i != j != k we need to make sure that each number is not used more than once.

      Following a similar approach, first, we can sort the array and then iterate through it, taking one number at a
      time. Let’s say during our iteration we are at number ‘X’, so we need to find ‘Y’ and ‘Z’ such that X + Y + Z <
      target.
      At this stage, our problem translates into finding a pair whose sum is less than “target - X" (as from the above
      equation Y + Z == target - X Y+Z==target−X). We can use a similar approach as discussed in Triplet Sum to Zero.

Example 1:
Input: [-1, 0, 2, 3], target=3
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

Example 2:
Input: [-1, 4, 2, 1, 3], target=5
Output: 4
Explanation: There are four triplets whose sum is less than the target:
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]

"""
from typing import List


class TripletWithSmallerSum:
    @staticmethod
    def triplets_with_smaller_sum(nums: List[int], target: int) -> int:
        # Sort the array
        nums.sort()
        count = 0
        for i in range(len(nums)):
            count += TripletWithSmallerSum.search_pair(nums, target-nums[i], i)
        return count

    @staticmethod
    def search_pair(nums, target_sum, first):
        count = 0
        left = first+1
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target_sum: # found the triplet
                # Since nums[right] >= nums[left], therefore we can replace nums[right] by any number between left and
                # right to get to a sum less than the target_sum
                count += right - left
                left += 1
            else:
                right -= 1  # We need a pair with a smaller sum
        return count


def main():
    twss = TripletWithSmallerSum()
    print(twss.triplets_with_smaller_sum([-1, 0, 2, 3], 3))
    print(twss.triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5))


# main()


"""
Time Complexity: O(N*LogN) - Sorting + N*N ==> O(N^2)
Space Complexity: O(N)
"""


"""
Follow Up : Write a function to return the list of all such triplets instead of the count. How will the time complexity 
            change in this case?

Solution: Following a similar approach we can create a list containing all the triplets. Here is the code - only the 
          highlighted lines have changed:


"""


class TripletWithSmallerSum2:
    @staticmethod
    def triplets_with_smaller_sum(nums: List[int], target: int) -> List[List[int]]:
        # Sort the array
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            TripletWithSmallerSum2.search_pair(nums, target-nums[i], i, triplets)
        return triplets

    @staticmethod
    def search_pair(nums, target_sum, first, triplets):
        left = first+1
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target_sum:  # found the triplet
                # Since nums[right] >= nums[left], therefore we can replace nums[right] by any number between left and
                # right to get to a sum less than the target_sum
                for i in range(right, left, -1):
                    triplets.append([nums[first], nums[left], nums[i]])
                left += 1
            else:
                right -= 1  # We need a pair with a smaller sum


def main():
    twss2 = TripletWithSmallerSum2()
    print(twss2.triplets_with_smaller_sum([-1, 0, 2, 3], 3))
    print(twss2.triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()

"""
Time Complexity: O(N*LogN) - Sorting + N*N*N ==> O(N^3)
Space Complexity: O(N)
"""
