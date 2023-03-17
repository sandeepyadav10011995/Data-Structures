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
"""


class Heap:  # Max Heap
    @staticmethod
    def swap(nums: list[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]

    def makeHeap(self, nums: list[int], size: int) -> list[int]:
        i = (size//2) - 1
        while i >= 0:
            self.heapify(nums, i, size)
            i -= 1
        return nums

    def heapify(self, nums: list[int], i: int, size: int) -> None:
        if i >= size: return
        if 2*i+1 >= size: return
        if 2*i+2 >= size:
            max_idx = 2*i + 1
        else:
            if nums[2*i+2] > nums[2*i+1]:
                max_idx = 2*i+2
            else:
                max_idx = 2*i+1

        if nums[max_idx] > nums[i]:  # or max_idx != i
            self.swap(nums, max_idx, i)
            self.heapify(nums, max_idx, size)

    def percolate_up(self, nums: list[int], i: int) -> None:
        if i == 0: return
        parent = (i-1) // 2
        if nums[i] > nums[parent]:
            self.swap(nums, i, parent)
            self.percolate_up(nums, parent)


arr = [3, 1, 5, 4, 2, 7, 8, 9]
hs = Heap()
print(hs.makeHeap(arr, len(arr)))

"""
Overall TC : 
Overall SC: 
"""