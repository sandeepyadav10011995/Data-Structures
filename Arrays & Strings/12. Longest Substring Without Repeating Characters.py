"""
Given a string s, return the length of the longest substring of s without repeating characters.

Example 1:
Input: : "ABCABADEC"
Output: 5
Explanation: Though there are substrings such as "AB" and "ABC" that have all unique characters, "BADEC" is the longest unique character substring.

Example 2:
Input: : ""
Output: 0

Constraints:
All letters will be uppercase A-Z
"""

class Solution:
    def sliding_window(self, s):
        hash_set = set()
        ans = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] not in hash_set:
                hash_set.add(s[j])
                j += 1
                ans = max(ans, j-i)
            else:
                hash_set.remove(s[j])
                i += 1
        return ans

    def optimized_sliding_window(self, s):
        hash_map = {}
        ans = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] in hash_map:
                i = max(hash_map[s[j]], i)
            ans = max(ans, j-i+1)
            hash_map[s[j]] = j+1
            j += 1
        return ans

string = "abcabcbb"
sol = Solution()
print(sol.sliding_window(string))
print(sol.optimized_sliding_window(string))
