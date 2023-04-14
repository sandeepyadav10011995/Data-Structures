"""
Problem : Median of 2 sorted arrays of different size.

X:      X1  X2 | X3  X4  X5  X6             L1=6
Y:      Y1  Y2  Y3  Y4  Y5 | Y6  Y7  Y8     L2=8

X2 <= Y6
Y5 <= X3

Then Median = Avg(max(X2, Y5) + min(X3, Y6)) --> if M+N ==> EVEN
            = Max(X2, Y6)  --> if M+N ==> ODD

To find the partition, we do a binary search on the smaller array
TC: O(log(min(M, N))

"""
import math


class Median:
    def __init__(self):
        self.INF = math.inf
        self.NINF = - math.inf

    def findMedian(self, nums1, nums2):
        # Check which arr is smaller
        if len(nums1) > len(nums2):
            return self.findMedian(nums2, nums1)

        M = len(nums1)
        N = len(nums2)

        low = 0
        high = M

        while low <= high:
            partitionX = (low+high) // 2
            partitionY = (M+N+1)//2 - partitionX

            # If the partitionX is 0 it means there is no left side; use NINF for maxLeftX
            # If the partitionX is M it means there is no right side; use INF for minRightX
            maxLeftX = self.NINF if partitionX == 0 else nums1[partitionX-1]
            minRightX = self.INF if partitionX == M else nums1[partitionX]

            # If the partitionY is 0 it means there is no left side; use NINF for maxLeftY
            # If the partitionY is N it means there is no right side; use INF for minRightY
            maxLeftY = self.NINF if partitionY == 0 else nums1[partitionY - 1]
            minRightY = self.INF if partitionY == N else nums1[partitionY]

            # Found
            if maxLeftX < minRightY and maxLeftY < minRightX:
                if (M + N) % 2 == 0:
                    return (max(maxLeftX, maxLeftY)+min(minRightX, minRightY))//2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:  # Move towards left in X
                high = partitionX - 1
            else:
                low = partitionX + 1

"""
Follow Up-: Kth smallest element of 2 sorted array of different size 
"""

class KthSmallest:
    def __init__(self):
        self.INF = math.inf
        self.NINF = - math.inf

    def findKthSmallest(self, nums1, nums2, K):
        # Check which arr is smaller
        if len(nums1) > len(nums2):
            return self.findKthSmallest(nums2, nums1, K)

        M = len(nums1)
        N = len(nums2)
        if M+N < K:
            return -1

        low = 0
        high = min(M, K-1)

        while low <= high:
            partitionX = (low+high) // 2
            partitionY = K-partitionX-1  # Because of 0 indexed

            # If the partitionX is 0 it means there is no left side; use NINF for maxLeftX
            # If the partitionX is M it means there is no right side; use INF for minRightX
            maxLeftX = self.NINF if partitionX == 0 else nums1[partitionX-1]
            minRightX = self.INF if partitionX == M else nums1[partitionX]

            # If the partitionY is 0 it means there is no left side; use NINF for maxLeftY
            # If the partitionY is N it means there is no right side; use INF for minRightY
            maxLeftY = self.NINF if partitionY == 0 else nums1[partitionY - 1]
            minRightY = self.INF if partitionY == N else nums1[partitionY]

            # Found
            if maxLeftX < minRightY and maxLeftY < minRightX:
                return min(maxLeftX, minRightY)
            elif maxLeftX > minRightY:  # Move towards left in X
                high = partitionX - 1
            else:
                low = partitionX + 1

        return min(nums1[partitionX], nums2[partitionY])
