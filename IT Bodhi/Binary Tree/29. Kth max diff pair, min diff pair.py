"""
Kth max diff pair

Given an array, Arr = [2, 6, 8, 9, 12, 15, 18, 21, 25, 28, 30, 35]
Return Kth Pair with Max Diff  --> (j, i) => Diff(Arr[j] - Arr[i]) is Kth Largest

Data Structure Used --> MaxHeap, HashMap or Tuple
HeapNode -: Diff Val|StartIndex|EndIndex

Next Value Pushed to Heap would be two values i.e.
            Diff Val|StartIndex+1|EndIndex
            Diff Val| StartIndex|EndIndex-1

            (i, j) --> (i+1, j) , (i, j-1)
If the signature already exists then don't put it in the MaxHeap
Keep doing this for K iterations.

IN THIS CASE STARTING POINT IS (0, N-1)

TC: O(K*logK)
SC: O(K)

===========================================================================================


Kth min diff pair --> Consecutive Numbers will have min diff

Given an array, Arr = [2, 6, 8, 9, 12, 15, 18, 21, 25, 28, 30, 35]
Return Kth Pair with Max Diff  --> (j, i) => Diff(Arr[j] - Arr[i]) is Kth Smallest

Data Structure Used --> MinHeap, HashMap or Tuple
In starting (i, i+1) will pe pushed.
HeapNode -: Diff Val|StartIndex|EndIndex

While popping the Node it would be pushing two values i.e.
            Diff Val|StartIndex-1|EndIndex
            Diff Val| StartIndex|EndIndex+1

            (i, j) --> (i-1, j), (i, j+1)

Do this for K iterations

IN THIS CASE STARTING POINTS IS NOT KNOWN.

TC: O(K*logN)
SC: O(N)

"""
import math
from heapq import *
from dataclasses import dataclass


@dataclass
class HeapObject:
    val: int
    index1: int
    index2: int

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    @staticmethod
    def kThMaxDiffPair(arr: list[int], K: int):
        size = len(arr)
        maxHeap = []
        cur = HeapObject(arr[-1]-arr[0], 0, size-1)  # Starting Point
        hashKey = cur.index1*size + cur.index2  # index1*size + index2
        hashMap = {hashKey: 1}
        heappush(maxHeap, HeapObject(-cur.val, cur.index1, cur.index2))

        count = 0
        kthMax = HeapObject(-math.inf, None, None)
        while count < K:
            heapObj = heappop(maxHeap)
            count += 1
            if count == K:
                kthMax = heapObj
                break

            hashKey1 = (heapObj.index1+1) * size + heapObj.index2
            if (heapObj.index2 != heapObj.index1+1) and hashKey1 not in hashMap:
                _val = arr[heapObj.index2] - arr[heapObj.index1+1]
                heappush(maxHeap, HeapObject(-_val, heapObj.index1+1, heapObj.index2))
                hashMap[hashKey1] = 1

            hashKey2 = heapObj.index1 * size + heapObj.index2-1
            if (heapObj.index2-1 != heapObj.index1) and hashKey2 not in hashMap:
                _val = arr[heapObj.index2-1] - arr[heapObj.index1]
                heappush(maxHeap, HeapObject(-_val, heapObj.index1, heapObj.index2-1))
                hashMap[hashKey2] = 1

        return kthMax

    @staticmethod
    def kThMinDiffPair(arr: list[int], K: int):
        size = len(arr)
        if size < 1:
            return -1
        minHeap = []
        # Note: In this Starting point is not known, therefore put all the consecutive diff of the nums
        for i in range(1, size):
            cur = HeapObject(arr[i]-arr[i-1], i-1, i)
            hashKey = cur.index1 * size + cur.index2  # index1*size + index2
            hashMap = {hashKey: 1}
            heappush(minHeap, HeapObject(cur.val, cur.index1, cur.index2))

        count = 0
        prevMin = HeapObject(None, None, None)
        kthMin = HeapObject(math.inf, None, None)
        while count < K and minHeap:
            heapObj = heappop(minHeap)
            if prevMin.val != kthMin.val:
                prevMin = kthMin
                count += 1
            else:
                kthMin = heapObj
            if count == K:
                kthMin = heapObj
                break

            hashKey1 = (heapObj.index1 - 1) * size + heapObj.index2
            if heapObj.index1 >= 1 and hashKey1 not in hashMap:
                _val = arr[heapObj.index2] - arr[heapObj.index1-1]
                heappush(minHeap, HeapObject(_val, heapObj.index1-1, heapObj.index2))
                hashMap[hashKey1] = 1

            hashKey2 = heapObj.index1 * size + (heapObj.index2 + 1)
            if heapObj.index2+1 <= size-1 and hashKey2 not in hashMap:
                _val = arr[heapObj.index2+1] - arr[heapObj.index1]
                heappush(minHeap, HeapObject(_val, heapObj.index1, heapObj.index2+1))
                hashMap[hashKey2] = 1

        return kthMin


sol = Solution()
arr = [2, 6, 8, 9, 12, 15, 18, 21, 25, 28, 30, 35]
K = 5
kthMax = sol.kThMaxDiffPair(arr=arr, K=K)
if kthMax.val != -math.inf:
    print(f"{arr[kthMax.index1]} + {arr[kthMax.index2]} Pair is {K}th Largest i.e, {-kthMax.val}")
kthMin = sol.kThMinDiffPair(arr=arr, K=K)
if kthMin.val != math.inf:
    print(f"{arr[kthMin.index1]} + {arr[kthMin.index2]} Pair is {K}th Smallest i.e, {kthMin.val}")
