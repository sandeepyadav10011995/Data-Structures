"""
    Cyclic Sort -: This pattern describes an interesting approach to deal with problems involving arrays containing
    numbers in a given range.
Question : Given an unsorted array containing n numbers ranging 1 to n. The array can have duplicates. This means that
           some numbers are missing. Find all the duplicates.

Approach 1: Sort the Array and find the duplicate
            TC: O(NlogN)
            SC: O(1)
Approach 2: Update the count of the number at their index
            TC: O(N)
            SC: O(N)
Approach 3: Slow and Fast Pointer --> By moving to the val index
            1st Collision--> Cycle
            Ans = start of the Cycle


Example -:
Input :
Output :
------------------------------------CODE-----------------------------------
"""


class CyclicSort:  # Pretty Complex::
    @staticmethod
    def swap(nums: list[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]

    @staticmethod
    def find_duplicates(nums: list[int]) -> int:  # O(N) --> Inc i, O(N-1) --> Swap
        i = 0
        N = len(nums)
        while i < N:
            if nums[i] <= i+1:
                j = nums[i] - 1
                if nums[i] != nums[j]:
                    CyclicSort.swap(nums, i, j)
                else:
                    return nums[i]
            else:
                i += 1
        return -1


class CyclicSort2:
    @staticmethod
    def find_duplicates(nums: list[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


arr = [3, 1, 4, 2, 4]
cs = CyclicSort()
num = cs.find_duplicates(nums=arr[:])
cs2 = CyclicSort2()
num2 = cs2.find_duplicates(nums=arr[:])
print(num)
print(num2)


"""
Overall TC : O(N)
Overall SC: O(1)
"""