"""
Stack : LIFO --> Last In First Out
    Add --> O(1)
    Delete --> O(1)
    Search --> O(N)
    Update --> O(1)

Queue : FIFO --> First In First Out => Head, Tail
    Add --> O(1)
    Delete --> O(1)
    Search --> O(N)
    Update --> O(1)

LinkedList/DLL : Head, Tail
    Add --> O(1)
    Delete --> O(1)
    Search --> O(N)
    Update --> O(1)


BST : Balanced
    Add --> logN
    Delete --> O(1) if leaf else logN
    Search --> logN
    Update --> logN

    UnBalanced
    Add --> O(N)
    Delete --> O(N)
    Search --> O(N)
    Update --> O(N)

Hash
    Add --> O(1)
    Delete --> O(1)
    Search --> O(1)
    Update --> O(1)

Heap
    Add --> logN
    Delete --> logN
    Search --> O(N)
    Update --> logN

Check if a number belongs to ugly number series or not ?


"""


class Solution:
    @staticmethod
    def check(num: int) -> bool:
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        while num % 7 == 0:
            num /= 7

        return num == 1

"""
Missing & repeated no from 1st N numbers in sorted array

"""

