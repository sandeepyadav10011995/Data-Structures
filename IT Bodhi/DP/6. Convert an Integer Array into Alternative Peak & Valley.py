"""
Problem: Convert an integer array into alternative peak & valley
Ex -: arr = [4, 1, 3, 8, 2, 5, 21, 42, 6]

Approach 1: Sort the array --> O(N*logN)
            Swap alternate values --> O(N)
        TC: O(N*logN) + O(N) ~ O(NlogN)
        SC: O(N)
    Problem -: What if we have duplicate/repeated values

Approach 2: Partition Method around mid-values --> O(N) --> Can be done in-place
            Then put the large and small numbers alternatively. --> O(N)
        TC: O(N) + O(N) ~ O(2N)
        SC: O(N)

        In Worst Case --> O(N^2)

Approach 3: Invariance --> Left ==> Right

"""


class Solution:
    @staticmethod
    def waveArrayWithSortLogic(arr):
        # Sort the array
        arr.sort()

        # Swap adjacent elements
        for i in range(0, len(arr)-1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]

        return arr

    @staticmethod
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def getPivot(arr, low, high):
        mid = low + (high - low) // 2
        pivot = high
        if arr[low] < arr[mid]:
            if arr[mid] < arr[high]:
                pivot = mid
        elif arr[low] < arr[high]:
            pivot = low

        return pivot

    def doPartition(self, arr, low, high):
        if low == high:
            return low
        pi = self.getPivot(arr, low, high)
        pv = arr[pi]
        self.swap(arr, pi, high)

        for i in range(low, high):
            if arr[i] < pv:
                self.swap(arr, i, low)
                low += 1
        self.swap(arr, low, high)
        return low

    def partition(self, arr, i, start, end):
        index = self.doPartition(arr, start, end)
        if index == i-1:
            return i
        if index < i-1:
            return self.partition(arr, i, index+1, end)
        else:
            return self.partition(arr, i, start, index-1)

    def waveArrayWithPartitionLogic(self, arr):
        size = len(arr)
        self.partition(arr, size//2, 0, size-1)
        # Fill the elements
        result = []
        return result

    @staticmethod
    def waveArrayWithInvarianceLogic(arr):
        N = len(arr)
        # Swap alternate numbers
        for i in range(0, N, 2):  # O(N)
            # If cur even element is smaller than previous; put greater value at even index
            if i > 0 and arr[i] > arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]

            # If cur even element is smaller than next; put greater value at even index
            if i < N-1 and arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        return arr


"""
TC: O(N)
SC: O(1)
"""

sol = Solution()
print(sol.waveArrayWithSortLogic(arr=[4, 16, 8, 5, 9, 18, 7, 6]))
print(sol.waveArrayWithPartitionLogic(arr=[4, 16, 8, 5, 9, 18, 7, 6]))
print(sol.waveArrayWithInvarianceLogic(arr=[4, 16, 8, 5, 9, 18, 7, 6]))
