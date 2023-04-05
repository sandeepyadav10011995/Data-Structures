"""
Problem: Median of 2 sorted arrays of same size.
M=N
Approach 1: Merge both the arrays and return the median.
            TC: O(M+N)
            SC: O(M+N)
Approach 2: Comparing Median
            TC: logN

"""


class Solution:
    def getMedian(self, nums1: list[int], nums2: list[int], N: int) -> int:
        # Base Case
        if N == 0:
            return -1
        elif N == 1:
            return (nums1[0] + nums2[0])//2
        elif N == 2:
            return (max(nums1[0], nums2[0]) + min(nums1[1], nums2[1]))//2
        else:
            median1 = self._median(nums1, N)
            median2 = self._median(nums2, N)
            
            if median1 > median2:
                if N % 2 == 0:
                    return self.getMedian(nums1=nums1[:N//2+1], 
                                          nums2=nums2[N//2-1:], 
                                          N=N//2+1)
                else:
                    return self.getMedian(nums1=nums1[N // 2 - 1:],
                                          nums2=nums2[:N // 2 + 1],
                                          N=N // 2 + 1)
            else:
                if N % 2 == 0:
                    return self.getMedian(nums1=nums1[N // 2 - 1:],
                                          nums2=nums2[:N // 2 + 1],
                                          N=N // 2 + 1)
                else:
                    return self.getMedian(nums1=nums1[:N // 2 + 1],
                                          nums2=nums2[N // 2 - 1:],
                                          N=N // 2 + 1)

    def _median(self, nums1, N) -> int:
        pass
