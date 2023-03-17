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
Approach 1: Bruteforce
            O(NL)*O(N)
           Total elements * Find Min
Approach 2: MinHeap
            MinHeap of Size N*L  --> O(N*L)
            Total elements --> O(N*L)
            TC : O(N*L)*O(log(N*L)) ~ O(NL*logNL)
            SC: O(NL)

Approach 3: Optimized Heap  -- Using Heap Node
            Heap Node
                    - arr_no
                    - index
            MinHeap of Size N  --> O(N)
            Total elements --> O(N*L)
            TC : O(NL)*O(logN) ~ O(NLlogN)
            SC: O(N)

"""


class HeapNode:
    def __init__(self, arr_no, index):
        self.arr_no = arr_no
        self.index = index


class MergeSortedArrays:
    def __init__(self, array=[]):
        self.nums = array
        self.merged_arr = []
        self.arr_size = len(array)

    def makeHeap(self, min_heap, size):
        i = (size // 2) - 1
        while i >= 0:
            self.heapify(min_heap, i, size)
            i -= 1

    def heapify(self, min_heap, i, size):
        if i >= size: return
        if 2 * i + 1 >= size: return
        pv = self.nums[min_heap[i].arr_no][min_heap[i].index]
        if 2 * i + 2 > size:
            max_i = 2 * i + 1
        else:
            lci = 2 * i + 1
            rci = 2 * i + 2
            lcv = self.nums[min_heap[lci].arr_no][min_heap[lci].index]
            rcv = self.nums[min_heap[rci].arr_no][min_heap[rci].index]
            max_i = lci if lcv < rcv else rci
        max_v = self.nums[min_heap[max_i].arr_no][min_heap[max_i].index]
        if max_v < pv:
            self.swap(min_heap, i, max_i)
            self.heapify(min_heap, max_i, size)

    @staticmethod
    def swap(min_heap, i1, i2):
        min_heap[i1], min_heap[i2] = min_heap[i2], min_heap[i1]

    def mergeSortedArrays(self):
        min_heap = []
        heap_size = self.arr_size - 1
        for i in range(heap_size + 1):
            min_heap.append(HeapNode(i, 0))

        self.makeHeap(min_heap, heap_size)

        while heap_size >= 0:
            val = arr[min_heap[0].arr_no][min_heap[0].index]
            self.merged_arr.append(val)

            if len(arr[min_heap[0].arr_no]) > min_heap[0].index + 1:
                min_heap[0].index += 1
            else:
                self.swap(min_heap, 0, heap_size)
                heap_size -= 1

            self.heapify(min_heap, 0, heap_size)

        return self.merged_arr


arr = [
    [3, 6, 9],
    [2, 4, 8, 10],
    [0, 1, 5, 7]
]
# mergeArrays = MergeSortedArrays(arr)
# m_arr = mergeArrays.mergeSortedArrays()
# print(m_arr)

# Using Built-In Heap

from heapq import *


class HeapNode2:
    def __init__(self, val, arr_no, index):
        self.val = val
        self.arr_no = arr_no
        self.index = index

    def __lt__(self, other):
        # MinHeap based on value
        return self.val < other.val


class MergeSortedArrays2:
    @staticmethod
    def mergeSortedArrays(nums: list[list[int]]) -> list[int]:
        # Base Case
        if nums is None:
            return []
        N = len(nums)
        merged_arr = []
        min_heap = []

        # Put all the arrays first element in min_heap
        for i in range(N):
            heappush(min_heap, HeapNode2(val=nums[i][0], arr_no=i, index=0))

        while min_heap:
            top_node = heappop(min_heap)
            merged_arr.append(top_node.val)

            arr_detail = nums[top_node.arr_no]
            if len(arr_detail) > top_node.index+1:
                heappush(min_heap, HeapNode2(val=arr_detail[top_node.index+1], arr_no=top_node.arr_no, index=top_node.index+1))
        return merged_arr


arr = [
    [3, 6, 9],
    [2, 4, 8, 10],
    [0, 1, 5, 7]
]
mergeArrays = MergeSortedArrays2()
m_arr2 = mergeArrays.mergeSortedArrays(arr)
print(m_arr2)
