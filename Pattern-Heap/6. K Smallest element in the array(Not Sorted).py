"""
Approach 1 : Bruteforce Solution : Sorting
            1. Sort the array
            2. Return the N-K elements

Approach 2: Divide & Conquer
            1. Quick Sort Partition Logic

Approach 3: Heap
            1. Using Min Heap
                a. Make Heap using all the numbers i.e N elements
                b. Extract top K elements from the heap
                c. TC: O(N) --> Make Heap
                       K*logN --> Extraction
                       ~ O(N + KlogN)
                d. SC: O(N)

            2. Using Max Heap
                a. Make Max Heap of only K size.
                b. TC: O(K*logK + (N-K)*logK) ~ O(N*logK)
                c. SC: O(K)
"""


class QuickSort:
    def __init__(self, nums):
        self.nums = nums

    def _swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def _getPivot(self, low, high):
        pivot = high
        mid = low + (high-low)//2
        if self.nums[low] < self.nums[mid]:
            if self.nums[mid] < self.nums[high]:
                pivot = mid
        elif self.nums[low] < self.nums[high]:
            pivot = low

        return pivot

    def _partition(self, low, high):
        pivot_index = self._getPivot(low, high)
        pivot_value = self.nums[pivot_index]
        # Swap the pivot_index value with high index value
        self._swap(pivot_index, high)

        for i in range(low, high):
            # all elements less than 'pivot_value' will be before the index 'low'
            if self.nums[i] < pivot_value:
                self._swap(i, low)
                low += 1
        # put the pivot_value in its correct place
        self._swap(low, high)
        return low

    def _quickSort(self, low: int, high: int):
        if low < high:
            pi = self._partition(low, high)
            self._quickSort(low, pi-1)
            self._quickSort(pi+1, high)

    def quickSort(self, ):
        self._quickSort(0, len(self.nums)-1)
        return self.nums


# arr = [3, 1, 5, 6, 4, 2, 7, 8, 9]
# qs = QuickSort(nums=arr)
# print(qs.quickSort())


class KSmallestElements:
    @staticmethod
    def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    @staticmethod
    def getPivot(nums, low, high):
        mid = low + (high-low)//2
        pivot = high
        if nums[low] < nums[mid]:
            if nums[mid] < nums[high]:
                pivot = mid
        elif nums[low] < nums[high]:
            pivot = low

        return pivot

    @staticmethod
    def partition(nums, low, high):
        pi = KSmallestElements.getPivot(nums, low, high)
        pv = nums[pi]
        KSmallestElements.swap(nums, pi, high)

        for i in range(low, high):
            if nums[i] < pv:
                KSmallestElements.swap(nums, i, low)
                low += 1
        KSmallestElements.swap(nums, low, high)
        return pi

    @staticmethod
    def kthSmallest(nums: list[int], start: int, end: int, K: int):
        if start > end:
            return None
        pi = KSmallestElements.partition(nums, start, end)
        if pi == K-1:
            return nums[:K]
        if pi > K-1:
            # Search Lower Part
            return KSmallestElements.kthSmallest(nums, start, pi - 1, K)
        # Search Higher Part
        return KSmallestElements.kthSmallest(nums, pi+1, end, K)


# arr = [3, 1, 5, 6, 4, 2, 7, 8, 9]
# ks = KSmallestElements()
# print(ks.kthSmallest(arr, 0, len(arr)-1, 3))

# Max Heap

from heapq import *


class KthSmallestElement:
    @staticmethod
    def find_kth_smallest(nums, k):
        max_heap = []
        # Put the first k elements in max_heap
        for i in range(k):
            heappush(max_heap, -nums[i])

        # go through the remaining numbers of the array, if the number from the array is smaller than the
        # top(biggest) number of the heap, remove the top number from heap and add the number from array
        for i in range(k, len(nums)):
            if -nums[i] > max_heap[0]:
                heappop(max_heap)
                heappush(max_heap, -nums[i])

        return -max_heap[0]


# arr = [3, 1, 5, 6, 4, 2, 7, 8, 9]
# ks = KthSmallestElement()
# print(ks.find_kth_smallest(arr, 3))


# Min Heap
from heapq import *


class KthSmallestMinHeap:
    @staticmethod
    def find_kth_smallest(nums, k):
        min_heap = nums[:]
        heapify(min_heap)

        for i in range(k-1):
            heappop(min_heap)

        return min_heap[0]


arr = [3, 1, 5, 6, 4, 2, 7, 8, 9]
ks = KthSmallestMinHeap()
print(ks.find_kth_smallest(arr, 3))
