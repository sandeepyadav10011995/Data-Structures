"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, 
return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"
 

Constraints:
1 <= s.length, t.length <= 105
s and t consist of English letters.

Follow up: Could you find an algorithm that runs in O(n) time? --> Important
"""
from collections import Counter

class Answer:
    def __init__(self, min_window_size, start, end):
        self.min_window_size = min_window_size
        self.start = start
        self.end = end

class Solution:
    def minWindow(self, s, t):
        # Edge Case
        if not s or not t:
            return ""
        # Dict to keep the count of unique chars in desired output
        dict_t = Counter(t)
        # Dict for the sliding window that keeps count of unique charcters.
        sliding_window = {}
        
        # Count of all the unique chars required in t
        required = len(dict_t)
        # Counter that keeps track of unique char required in t present in the sliding window
        formed = 0
        
        # Answer to store to store the min_window_size and the start and end points
        ans = Answer(flaot("inf"), 0, 0)
        
        # Two Pointers to traverse the string
        left, right = 0, 0
        
        while right < len(s):
            char = s[right]
            # Make an entry or Update the sliding window --> Expanding
            sliding_window[char] = sliding_window.get(char, 0) + 1
            # If the char contributes to get desired substring
            if char in dict_t and sliding_window[char] == dict_t[char]:
                formed += 1
            # Try if we can Contract --> "Just Like Caterpillar"    
            while left <= right and formed == required:
                char = s[left]
                # Update the ans
                if right - left + 1 < ans.min_window_size:
                    ans = Answer(right-left+1, left, right)
                sliding_window[char] -= 1
                # Update the "formed" if the char contributes to "formed" 
                if char in dict and sliding_window[char] < dict_t[char]:
                    formed -= 1
                l += 1
            right += 1
            
        return "" if ans.min_window_size == float("inf") else s[ans.start:ans.right+1]
    
    
