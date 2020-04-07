"""
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.

Example:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

"""

def countElements(arr: List[int]) -> int:
    # Parse the list/array
    unique_num = set(arr)

    # Traverse the list/array
    count = 0
    for num in arr:
        if (num + 1) in unique_num:
            count += 1
    return count
    
