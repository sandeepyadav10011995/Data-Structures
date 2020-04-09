"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

"""
# Stack Approach
class Solution:
  def helper(self, s: str) -> str:
    stack = []
    for letter in s:
      if letter == "#" and len(stack) != 0:
        stack.pop()
      elif letter != "#":
        stack.append(letter)
    return "".join(stack)
    
  def backspaceCompare(self, S: str, T: str) -> bool:
    s1 = self.helper(S)
    s2 = self.helper(T)
    if s1 == s2:
      return True
    return False
  
# TODO: Optimized Approach


