"""
Problem -: Union Of Two Sorted Array(Can Have Duplicates)
           Union = All the unique elements from both the arrays
           Intersection = All the elements that are present in both the arrays.(Repetition is allowed)

------------------    Union    ----------------------------------
BruteForce Solution -: Using Set
                       TC: O(N+M)
                       SC: O(N+M)

Optimal Approach -: Two Pointers with Set
                    TC: O(M+N)
                    SC: O(M+N) --> To store the output(Auxiliary)
---------------------------------------------------------------------

------------------------ Intersection  ----------------------------------
Bruteforce Solution -: Iterating on arr and check it's corresponding another array using visited logic.
                        TC: O(N*M)
                        SC: O(M)
Optimal Solution -: Using Two Pointers.
                TC:
                SC:
"""


class Solution:
    @staticmethod
    def unionArray(nums1: list[int], nums2: list[int]) -> list[int]:
        N = len(nums1)
        M = len(nums2)

        unionNums = []
        p1, p2 = 0, 0

        while p1 < N and p2 < M:
            if nums1[p1] <= nums2[p2]:
                if not unionNums or unionNums[-1] != nums1[p1]:
                    unionNums.append(nums1[p1])
                p1 += 1
            else:
                if not unionNums or unionNums[-1] != nums2[p2]:
                    unionNums.append(nums2[p2])
                p2 += 1

        while p1 < N:
            if not unionNums and unionNums[-1] != nums1[p1]:
                unionNums.append(nums1[p1])
            p1 += 1

        while p2 < M:
            if not unionNums and unionNums[-1] != nums2[p2]:
                unionNums.append(nums2[p2])
            p2 += 1

        return unionNums

    @staticmethod
    def intersectionOfSortedArrayBF(nums1: list[int], nums2: list[int]) -> list[int]:
        intersectionNums = []
        visited = [0 for _ in range(len(nums2))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and visited[j] == 0:
                    intersectionNums.append(nums1[i])
                    visited[j] = 1
                    break
                elif nums1[i] < nums2[j]:
                    break

        return intersectionNums

    @staticmethod
    def intersectionOfSortedArrayOA(nums1: list[int], nums2: list[int]) -> list[int]:
        intersectionNums = []
        N = len(nums1)
        M = len(nums2)
        i, j = 0, 0
        while i < N and j < M:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] == nums2[j]:
                intersectionNums.append(nums1[i])
                i += 1
                j += 1
            else:
                j += 1

        return intersectionNums


sol = Solution()
print(sol.unionArray(nums1=[1, 1, 2, 3, 4, 5], nums2=[2, 3, 4, 4, 5, 6]))
