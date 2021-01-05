"""
Given two sorted arrays, return a new array that represents their intersection.

Example 1:
Input:
[1,2,3,5]
[1,2]

Output:
[1,2]

Example 2:
Input:
[1,2,2,3]
[1,1,4]

Output:
[1]

Constraints
Each element in the result must be unique. --> Set

Approach 1 : Brute Force  Time Complexity : O(m*n)
Approach 2 : Binary Search  Time Complexity : O( min(m,n) * log(max(m,n)) )
Approach 3 : Using Unique values of max array in set and then linearly check on another
             Time Complexity : O(m+n)
             Space Complexity : O(max(m,n))
Approach 4 : Two Pointers --> Time Complexity : O(m+n) Using the Sorted Array property for this.
"""


class Solution:
    def intersectionPoint(self, nums1, nums2):
        intersection = set()
        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                intersection.add(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return list(intersection)

sol = Solution()
print(sol.intersectionPoint(nums1=[1,2,3,5] , nums2=[1, 2]))
