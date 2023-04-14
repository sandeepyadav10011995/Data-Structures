"""
Kth max sum pair

Given an array, Arr = [2, 6, 8, 9, 12, 15, 18, 21, 25, 28, 30, 35]
Return Kth Pair with Max Sum  --> (j, i) => Sum(Arr[j] + Arr[i]) is Kth Largest

Data Structure Used --> MaxHeap, HashMap or Tuple
HeapNode -: Sum Val|StartIndex|EndIndex

Next Value Pushed to Heap would be two values i.e.
            Sum Val|StartIndex-1|EndIndex
            Sum Val| StartIndex|EndIndex-1

            (i, j) --> (i-1, j) , (i, j-1)
If the signature already exists then don't put it in the MaxHeap
Keep doing this for K iterations.

IN THIS CASE STARTING POINT IS (N-2, N-1)

TC: O(K*logK)
SC: O(K)

===========================================================================================
Kth min sum pair --> Consecutive Numbers will have min Sum

Given an array, Arr = [2, 6, 8, 9, 12, 15, 18, 21, 25, 28, 30, 35]
Return Kth Pair with Max Sum  --> (j, i) => Sum(Arr[j] - Arr[i]) is Kth Smallest

Data Structure Used --> MinHeap, HashMap or Tuple
In starting (i, i+1) will pe pushed.
HeapNode -: Sum Val|StartIndex|EndIndex

While popping the Node it would be pushing two values i.e.
            Sum Val|StartIndex-1|EndIndex
            Sum Val| StartIndex|EndIndex+1

            (i, j) --> (i+1, j), (i, j+1)
Do this for K iterations

IN THIS CASE STARTING POINTS IS KNOWN (0, 1).

TC: O(K*logK)
SC: O(K)

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
    def kThMaxSumPair(arr: list[int], K: int):
        size = len(arr)
        maxHeap = []
        cur = HeapObject(arr[size-2] + arr[size-1], size-2, size-1)  # Starting Point n-2, n-1
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

            hashKey1 = heapObj.index1 * size + heapObj.index2 - 1
            if (heapObj.index2 - 1 != heapObj.index1) and hashKey1 not in hashMap:
                _val = arr[heapObj.index1] + arr[heapObj.index2-1]
                heappush(maxHeap, HeapObject(-_val, heapObj.index1, heapObj.index2-1))
                hashMap[hashKey1] = 1

            hashKey2 = (heapObj.index1-1) * size + heapObj.index2
            if hashKey2 not in hashMap:
                _val = arr[heapObj.index1-1] + arr[heapObj.index2]
                heappush(maxHeap, HeapObject(-_val, heapObj.index1-1, heapObj.index2))
                hashMap[hashKey2] = 1

        return kthMax

    @staticmethod
    def kThMinSumPair(arr: list[int], K: int):
        size = len(arr)
        if size < 1:
            return -1
        minHeap = []
        cur = HeapObject(arr[0] + arr[1], 0, 1)  # Starting Point 0, 1
        hashKey = cur.index1 * size + cur.index2  # index1*size + index2
        hashMap = {hashKey: 1}
        heappush(minHeap, HeapObject(cur.val, cur.index1, cur.index2))

        count = 0
        kthMin = HeapObject(math.inf, None, None)
        while count < K:
            heapObj = heappop(minHeap)
            count += 1
            if count == K:
                kthMin = heapObj
                break

            hashKey1 = (heapObj.index1 + 1) * size + heapObj.index2
            if (heapObj.index1 + 1 != heapObj.index2) and hashKey1 not in hashMap:
                _val = arr[heapObj.index1+1] + arr[heapObj.index2]
                heappush(minHeap, HeapObject(_val, heapObj.index1+1, heapObj.index2))
                hashMap[hashKey1] = 1

            hashKey2 = heapObj.index1 * size + (heapObj.index2 + 1)
            if hashKey2 not in hashMap:
                _val = arr[heapObj.index1] + arr[heapObj.index2+1]
                heappush(minHeap, HeapObject(_val, heapObj.index1, heapObj.index2+1))
                hashMap[hashKey2] = 1

        return kthMin


sol = Solution()
arr = [2, 6, 8, 9, 12, 15, 18, 21, 25, 28, 30, 35]
K = 5
kthMax = sol.kThMaxSumPair(arr=arr, K=K)
if kthMax.val != -math.inf:
    print(f"{arr[kthMax.index1]} + {arr[kthMax.index2]} Pair is {K}th Largest i.e, {-kthMax.val}")
kthMin = sol.kThMinSumPair(arr=arr, K=K)
if kthMin.val != math.inf:
    print(f"{arr[kthMin.index1]} + {arr[kthMin.index2]} Pair is {K}th Smallest i.e, {kthMin.val}")
