"""
Problem -: Rotate array by K places

Brute Force Solution -: Left Rotate One Element one by one K times using temp val
            TC: O(K*N)
            SC: O(1)

Better Solution:
        0  1  2  3  4  5  6
nums = [1, 2, 3, 4, 5, 6, 7]
D = 3
N = 7
TC: O(N)
SC: O(K)

prevIdx(I)  curIdx = I-D
        3 --> 0
        4 --> 1
        5 --> 2
        6 --> 3

Temp Array
prevIdx(I)   curIdx = I - (N-D)
        0 --> 4
        1 --> 5
        2 --> 6

Optimal Solution: Reverse Logic
                 Step 1: Reverse Arr(0, D)
                         Reverse Arr(D, N)
                 Step 2: Reverse Arr(0, N)
TC: O(2N) ~ O(N)
SC: O(1)
"""


class Rotation:
    @staticmethod
    def leftRotateArrayByDPlacesBetterSolution(nums: list[int], N: int, D: int) -> list[int]:
        D %= N

        if D == 0:
            return nums

        temp = [nums[i] for i in range(D)]

        for i in range(D, N):
            nums[i-D] = nums[i]

        for i in range(N-D, N):
            nums[i] = temp[i-(N-D)]

        return nums

    @staticmethod
    def _reverse(nums, i, j):
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def leftRotateArrayByDPlacesOptimalSolution(self, nums: list[int], N: int, D: int) -> list[int]:
        D %= N

        if D == 0:
            return nums

        # # Reverse Arr(0, D)
        # nums[:D].reverse()
        # # Reverse Arr(D, N)
        # nums[D:N].reverse()
        # # Reverse Arr(0, N)
        # nums[:N].reverse()

        # Reverse Arr(0, D-1)
        self._reverse(nums, 0, D-1)
        # Reverse Arr(D, N-1)
        self._reverse(nums, D, N-1)
        # Reverse Arr(0, N-1)
        self._reverse(nums, 0, N-1)

        return nums


arr = [1, 2, 3, 4, 5, 6, 7]
arr1 = [1, 2, 3, 4, 5, 6, 7]
N, D = 7, 3
sol = Rotation()
print(sol.leftRotateArrayByDPlacesBetterSolution(arr, N, D))
print(sol.leftRotateArrayByDPlacesOptimalSolution(arr1, N, D))