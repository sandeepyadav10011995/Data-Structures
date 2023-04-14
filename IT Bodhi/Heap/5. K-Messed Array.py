"""
    Heap -: Three important properties -:
    1. Binary Tree
    2. Complete Binary Tree : This is the reason why heap can be represented as an Array.
    3. Parent Children Relation :
                                a. Max Heap : Parent > Left & Right Child
                                b. Min Heap : Parent < Left & Right Child

    Implement Heap -: 1. Percolate Up --> Bottom Up Approach
                      2. Heapify --> Top Down Approach
                         Note : For Heapify, we need to run only loop for N/2 elements only because N/2 elements are
                                leaf nodes --> Complete Binary Tree(CBT)

    Let discuss the Time Complexity for both the Approach -:
    Percolate Up -: O(NlogN)
    S1 = 2^0*1 + 2^1*2 + 2^3*3 + ... + 2^(logN-1)*logN
    S1 = NlogN

    Heapify -: O(2N) ~ O(N)
    S2 = 2^0*logN + 2^1*(logN-1) + ... + 2^(logN-1)*1
    2S2 = 2*logN + 2^2*(logN-1) + ... + 2^(logN)*1

    Sub 2S2 - S2 = S2
    S2 = 2^1(1-0) + 2^2(2-1) + ... + 2^(logN)*(logN-(logN-1)) -logN
    S2 = 2^1 + 2^2 + ... + 2^(logN) - logN
    S2 = 2^(logN+1) - logN
    S2 = 2N - logN ~ 2N


Question : K-Messed Array i.e an element can present between i-K to i+k in the array, So we have restore the array,
           you have to sort the array in minimum time.
            2 4 5  7 9 12 15 17
Example -: [4 2 7 12 5 9 17 15]
            0 1 2  3 4 5  6  7
Input :
Output :

------------------------------------CODE-----------------------------------
 Approach 1: Sorting
            TC: O(NlogN)

Suppose k<<<<N, then above sol is not a good solution

Approach 2: MinHeap of Fixed Window size
            TC: O(NlogK)
"""
from heapq import *


class KMessedArray:
    @staticmethod
    def kMessedArray(nums, k):
        min_heap = []
        window_size = k+1
        # First put the first k+1 elements in the minHeap
        for i in range(window_size):
            heappush(min_heap, nums[i])

        # Go through the rest of the array and sort the array.
        for j in range(window_size, len(nums)+window_size):
            nums[j-window_size] = heappop(min_heap)
            if j < len(nums):
                heappush(min_heap, nums[j])

        return nums


arr = [4, 2, 7, 12, 5, 9, 17, 15]
kma = KMessedArray()
print(kma.kMessedArray(nums=arr, k=2))
