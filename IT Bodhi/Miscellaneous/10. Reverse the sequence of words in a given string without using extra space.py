"""
Problem : Reverse the sequence of words in a given string without using extra space

Example -:
Input:      i am very happy today
Output :    today happy very am i

Approach 1: Split the string by space and then construct new string traversing the array in reverse order
        TC: O(N) + O(N) ~ O(N)
        SC: O(N)

Approach 2: Using a stack ~ Logic is similar to above as extra space is being used.
            Keep insert the word in a stack
            Then create a new string while popping the words from stack
        TC: O(N) + O(N) ~ O(N)
        SC: O(N)

Approach 3: Step 1: Reverse the whole string
            Step 2: Then reverse each word
Input:      i am very happy today
Step 1:     yadot yppah yrev ma i
Step 2:     today happy  very am i

        TC: O(N) + O(N) ~ O(N)
        SC: O(1) If input is character array.
"""

class Solution:
    @staticmethod
    def _reverse(nums, i, j):
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    def reverseSequenceOfWordsInAString(self, s: list[list[str]]) -> list[list[str]]:
        N = len(s)
        print(" ".join("".join(word) for word in s))
        # Reverse the whole string
        self._reverse(nums=s, i=0, j=N-1)
        # Reverse each word
        start = 0
        for end in range(N):
            if s[end] == " ":
                self._reverse(nums=s, i=start, j=end-1)
                start = end+1
        print(" ".join("".join(word) for word in s))
        return s

sol = Solution()
print(sol.reverseSequenceOfWordsInAString(s=[["i"], ["a", "m"], ["v", "e", "r", "y"], ["h", "a", "p", "p", "y"],
                                             ["t", "o", "d", "a", "y"]]))
