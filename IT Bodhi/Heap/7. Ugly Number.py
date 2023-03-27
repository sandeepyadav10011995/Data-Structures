"""
Problem Statement -: Ugly Number Series. Find the kh ugly number

Numbers which are multiples of 3, 5 and 7.
3, 5, 7, 9, 15, 21, 25, 27, 35, 45, 49, 63, ...

Special Cases: When we are looking for Next Max or Next Min ==> Use Heap


"""
from heapq import *


class UglyNumbers:
    @staticmethod
    def findKthUglyNumber(K: int):
        multiples = [3, 5, 7]
        minHeap = multiples[:]

        kthUglyNumber = None
        uniqueNums = set(minHeap)
        while K > 0:
            # Pop the min element
            num = heappop(minHeap)
            kthUglyNumber = num
            # Push the multiples of the num back in the heap
            for mul in multiples:
                newMul = num*mul
                if newMul not in uniqueNums:
                    uniqueNums.add(newMul)
                    heappush(minHeap, newMul)
            K -= 1

        return kthUglyNumber


def main():
    un = UglyNumbers()
    for i in range(1, 21):
        print(f"{i}th Ugly number is : {un.findKthUglyNumber(i)}")


main()
