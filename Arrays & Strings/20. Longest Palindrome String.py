"""
Given a string, determine the length of the longest possible palindromic string that can be constructed using the characters of the string.

Example 1:
Input: "aabbc"
Output: 5
Explanation: The longest palindromes possible are {"abcba", "bacab"}

Example 2:
Input: "abbcccd"
Output: 5
Explanation: The original string length is 7, but the longest palindromes are {"cbcbc",  "bcccb"}; 'a' and 'd' were not used.

Example 3:
Input: "aA"
Output: 1
Explanation: since the input is case-sensitive; the longest palindromes are {"a", "A"}

Example 4:
Input: "xyz"
Output: 1

Example 5:
Input: "ccc"
Output: 3

"""
# Approach One : Hash Map and calculating the frequency of each character.
# Approach Two : Hash Set and using it as a Stack.

class Solution:
    def longestPalindrome(self, s):
        matched = 0
        hash_set = set()
        for c in s:
            if c in hash_set:
                hash_set.remove(c)
                matched += 1
            else:
                hash_set.add(c)

        longest_palindrome = matched * 2
        if hash_set:
            longest_palindrome += 1
        return longest_palindrome

s = 'aaabbbccccdd'
sol = Solution()
print(sol.longestPalindrome(s))
