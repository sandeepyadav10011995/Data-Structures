"""
Problem: Compare X with kth largest in a max heap(Binary Tree) ? It can have duplicates as well.
         If it is less than Kth largest --> True else False





"""


class ValueCount:
    def __init__(self, lvc=0, svc=0):
        self.lvc = lvc
        self.svc = svc


class Compare:
    def compareXWithKthLargestBT(self, heapArray: list[int], X: int, K: int, valueCount, index) -> bool:
        size = len(heapArray)
        # Base Case
        if (index >= size - 1) or heapArray[index] < X:
            return False

        if heapArray[index] > X:
            valueCount.lvc += 1

        if heapArray[index] == X:
            valueCount.svc += 1
            return False

        # Check
        if valueCount.lvc >= K:
            return True
        if self.compareXWithKthLargestBT(heapArray, X, K, valueCount, 2 * index + 1):
            return True
        # Explore the right child
        return self.compareXWithKthLargestBT(heapArray, X, K, valueCount, 2 * index + 2)


def main():
    array = [40, 38, 32, 21, 35, 34, 33, 15, 20, 31, 32, 23, 28]
    comp = Compare()
    vc = ValueCount()
    print(comp.compareXWithKthLargestBT(heapArray=array, X=21, K=6, valueCount=vc, index=0))
    print(vc.lvc)
    print(vc.svc)


main()
