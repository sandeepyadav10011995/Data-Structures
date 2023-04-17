"""
Problem : Given a non-empty unsorted array taken from a range of 1 to n. Due to some data error, one of the numbers is
          duplicated, which results in another number missing. Create a function that returns the corrupt pair (missing,
          duplicated).

Approach 1: Create an array of N+1 length and update the count of num at its index
            TC: O(N) + O(N)
            SC: O(N)
Approach 2: Summation of array
            Drawback --> Will change the array
            X-Y = S
            X^2 + Y^2 = SS
            X+Y = S`
            Then we can compute X and Y respectively.
            TC: O(N)
            SC: O(1)
Approach 3: XOR property
            Steps:
                1. XOR all arr[i] --> x  -> O(N)
                2. x ^ (1^2^3^...^N)) ==> x^y = num -> O(N)
                4. Separate in 2 buckets -> O(N)
                5. Separate (1...N) in 2 buckets -> O(N)
                6. XOR both buckets to find the missing and duplicate number.
                TC: O(N)
"""


def find_corrupt_pair(nums):
    # Initialize missing and duplicated
    missing = None
    duplicated = None

    # Function for swapping
    def swap(arr, first, second):
        arr[first], arr[second] = arr[second], arr[first]
    # Apply cyclic sort on the array

    i = 0
    # Traversing the whole array
    while i < len(nums):
        # Determining what position the specific element should be at
        correct = nums[i] - 1
        # Check if the number is at wrong position
        if nums[i] != nums[correct]:
            # Swapping the number to it's correct position
            swap(nums, i, correct)
        else:
            i += 1

    # Finding the corrupt pair(missing, duplicated)

    for j in range(len(nums)):
        if nums[j] != j + 1:
            duplicated = nums[j]
            missing = j + 1
    return missing, duplicated


# Driver code
def main():
    array1 = [3, 1, 2, 5, 2]
    array2 = [3, 1, 2, 3, 6, 4]
    array3 = [4, 1, 2, 1, 6, 3]
    array4 = [4, 3, 4, 5, 1]
    array5 = [5, 3, 5, 6, 2, 1]
    array6 = [1, 2, 3, 4, 5]
    array7 = [5, 4, 3, 2, 1]
    array = [array1, array2, array3, array4, array5, array6, array7]
    for i in range(len(array)):
        print(i + 1,  ".\tGiven array: ", array[i], sep="")
        result = find_corrupt_pair(array[i])

        if result[0]:
            print("\n\tCorrupt pair: ", result[0], ", ", result[1], sep="")
        else:
            print("\n\tNo corrupt pair found.")
        print("-"*100)


if __name__ == '__main__':
    main()
