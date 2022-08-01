"""
The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two
pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when
dealing with cyclic LinkedLists or arrays.

By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to
meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

Problem Statement: Any number will be called a happy number if, after repeatedly replacing it with a number equal to the
                   sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will
                   never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Example 1:
Input: 23
Output: true (23 is a happy number)
Explanations: Here are the steps to find out that 23 is a happy number:

Example 2:
Input: 12
Output: false (12 is not a happy number)
Explanations: Here are the steps to find out that 12 is not a happy number:

"""


class HappyNumbers:
    @staticmethod
    def find_happy_number(num: int) -> bool:
        # Two Pointers --> Slow and Fast Pointer
        slow = num
        fast = num
        while True:
            slow = HappyNumbers.find_sq_sum(slow)  # Move one step
            fast = HappyNumbers.find_sq_sum(HappyNumbers.find_sq_sum(fast))  # Move two steps
            if slow == fast:  # Found the cycle
                break
        return slow == 1

    @staticmethod
    def find_sq_sum(num: int) -> int:
        _sum = 0
        while num > 0:
            digit = num % 10
            _sum += digit*digit
            num //= 10
        return _sum


def main():
    hn = HappyNumbers()
    print(hn.find_happy_number(23))
    print(hn.find_happy_number(12))


main()


"""
Time Complexity: O(N)
Space Complexity: O(1)
"""






