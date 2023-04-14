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


Question : Implement Heap ?
Example -:
Input :
Output :

------------------------------------CODE-----------------------------------
Approach 1 : Using arrays
            1. Sort the array --> O(NlogN)
            2. Insertion --> O(N^2)



Approach 2: Using Min Heap
            1. Create a MinHeap using makeHeap i.e. heapify --> O(N)
            2. Pop two elements --> 2*O(logN)
            3. Add them and push the final value in MinHeap  --> O(logN)
            4. Continue step 2-3 until one element if left in MinHeap --> 3*(N-1)*O(logN)

"""

# Built-In Min Heap
from heapq import *


class StringConcatenationCost:
    def __init__(self, nums):
        self.nums = nums

    def costCS(self):
        # Create a MinHeap
        minHeap = self.nums[:]
        heapify(minHeap)  # O(N) --> makeHeap
        print(minHeap)

        # Pop two-min values --> Add them and put the final value back into the minHeap --> until only single value is
        # left
        cost = 0
        while len(minHeap) > 1:
            val1 = heappop(minHeap)  # O(logN)
            val2 = heappop(minHeap)  # O(logN)
            val3 = val1 + val2
            cost += val3
            heappush(minHeap, val3)  # O(logN)
        print(cost)


arr = [10, 15, 6, 2, 105, 200, 5]
arr2 = [101, 100, 2, 1]
scc = StringConcatenationCost(arr2)
scc.costCS()


"""
Overall TC : O(N) + (N-1)3*O(logN) ~ O(NlogN)
Overall SC: O(N)
"""