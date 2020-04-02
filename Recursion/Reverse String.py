"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

def reverseString(self, s: List[str]) -> None:
        # Method 1 --> Recursive Approach
        def helper(s, left, right):
            # Edge Case
            if left >= right:
                return s
            else:
                s[left], s[right] = s[right], s[left]
            helper(s, left + 1, right - 1)
        
        N = len(s)
        if N == 0:
            return None
        left = 0
        right = N -1
        return helper(s, left, right)
        
        
        # Method 2 --> Iterative Approach
        # N = len(s)
        # if N == 0:
        #     return None
        # left = 0
        # right = N -1   
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1
        # return s
