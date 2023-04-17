"""
For a given unsorted array, find the first k missing positive numbers in that array.
Constraints:Ignore all negative numbers.

If missing_nums.length ≠ k, add missing numbers up to k.
1 ≤ k ≤ 10^4
1 ≤ missing_nums.length ≤ 200
"""


def find_missing_numbers(arr1, k):
    # Step 1: Traverse the array and mark elements as negative if they are present in the array.
    arr = arr1[:]
    for i in range(len(arr)):
        if 0 < arr1[i] <= len(arr):
            idx = abs(arr1[i]) - 1
            arr[idx] = -(arr1[i])

    # Step 2: Traverse the array again and add missing numbers to the result list.
    result = []
    for i in range(len(arr)):
        if arr[i] >= 0 and len(result) < k:
            result.append(i + 1)

    # Step 3: Add remaining missing numbers to the result list.
    while len(result) < k:
        result.append(len(arr) + 1 + len(result))

    return result


arr = [3, 4, 2, 1, 6, 8]
k = 3
print(find_missing_numbers(arr, k))

