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



    Heap Methods:   Add --> PercolateUp(Bottom Up)
                    Delete --> Heapify(Top Down)
    Note : This is for Min Heap, for Max Heap this is vice-versa.
    Add Element --> Min Heap --> Percolate Up --> O(logN)
    def minHeapAdd(arr, val):
        size = len(arr)
        size += 1
        arr[size] = val
        percolateUp(arr, size)


    Delete Element --> Min Heap  --> Heapify --> O(logN)
    def minHeapDelete():
        val = self.nums[0]
        self.swap(0, size)
        size -= 1
        heapify()
        return val

    Update Rules :
                    1. MinHeap  --> Inc Value --> Heapify
                    2. Max Heap --> Dec Value --> Heapify

                    3. Min Heap --> Inc Value --> Percolate Up
                    4. Max Heap --> Dec Value --> Percolate Up

    Note : This comes really handy in Indexed Priority Queue(IPQ) implementation and Updates in IPQ Kruskal's and
    Dijkstra's Algorithm


Question : Implement Heap ?
Example -:
Input :
Output :

------------------------------------CODE-----------------------------------
"""


class Heap:  # Max Heap
    def __init__(self, array: list[int] = []) -> None:
        self.nums = array
        self.arr_size = len(array)

    def swap(self, i: int, j: int) -> None:
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def makeHeap(self, size: int) -> None:
        i = (size // 2) - 1
        while i >= 0:
            self.heapify(i, size)
            i -= 1

    def heapify(self, i: int, size: int) -> None:
        if i >= size: return
        if 2 * i + 1 >= size: return
        if 2 * i + 2 > size:
            max_idx = 2 * i + 1
        else:
            if self.nums[2 * i + 2] > self.nums[2 * i + 1]:
                max_idx = 2 * i + 2
            else:
                max_idx = 2 * i + 1

        if self.nums[max_idx] > self.nums[i]:
            self.swap(max_idx, i)
            self.heapify(max_idx, size)

    def percolate_up(self, i: int) -> None:
        if i == 0: return
        parent = (i - 1) // 2
        if self.nums[i] < self.nums[parent]:
            self.swap(i, parent)
            self.percolate_up(parent)

    def minHeapAdd(self, val):
        self.arr_size += 1
        self.nums[self.arr_size] = val
        self.percolate_up()

    def delete(self) -> int:
        val = self.nums[0]
        self.swap(0, self.arr_size)
        self.heapify(0, self.arr_size)
        return val


"""
Overall TC : 
Overall SC: 
"""
