"""
In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain
constraints, the Two Pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a
sub-array.

Problem Statement : Given an array of unsorted numbers find all the unique triplets in it that add up to zero.

Algo : Since the array is not sorted and instead of a pair we need to find triplets with a target sum of zero.
       Another difference is that we need to find all the unique triplets. To handle this, we have to skip any duplicate
       number. Since we will be sorting the array, so all the duplicate numbers will be next to each other and easier to
       skip.


Example 1:
    Input: [-3, 0, 1, 2, -1, 1, -2]
    Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
    Explanation: There are four unique triplets whose sum is equal to zero.

"""
from typing import List


class TripletToSumZero:
    @staticmethod
    def search_triplets(nums: List[int]) -> List[List[int]]:
        # Sort the array
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  # To skip the duplicates
                continue
            TripletToSumZero.search_pairs(nums, -nums[i], i+1, triplets)

        return triplets

    @staticmethod
    def search_pairs(nums, target_sum, left, triplets):
        right = len(nums) - 1
        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum == target_sum:
                triplets.append([-target_sum, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1  # Skip same element to avoid duplicate triplets
                while left < right and nums[right] == nums[right+1]:
                    right -= 1  # Skip same element to avoid duplicate triplets
            elif target_sum > cur_sum:
                left += 1  # We need a pair with a bigger sum
            else:
                right -= 1  # We need a pair with a smaller sum


def main():
    ttsz = TripletToSumZero()
    print(ttsz.search_triplets([-3, 0, 1, 2, -1, -1, 1, -2]))


main()


"""
Time Complexity: O(N*LogN) - Sorting + N*N ==> O(N^2)
Space Complexity: O(N)
"""
