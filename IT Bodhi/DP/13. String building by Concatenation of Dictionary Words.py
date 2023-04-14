"""
Problem : Find if a string could be made by concatenation of dictionary words.
Ex-: BlueAndGreenLight




"""


class Solution:
    def isSubWords(self, s: str, index: int, size: int, dictionary) -> bool:
        # Base Case
        if index == size:
            return True

        for i in range(size):
            if s[index:i+1] in dictionary:
                if self.isSubWords(s, i+1, size, dictionary):
                    return True
        return False

    """
        TC: O(N^N)
        SC: O(N)
    """

    def isSubWordsTopDown(self, s: str, index: int, size: int, dictionary, memo) -> bool:
        # Base Case
        if index == size:
            return 1

        if memo[index] < 0:
            for i in range(size):
                if s[index:i+1] in dictionary:
                    if self.isSubWordsTopDown(s, i+1, size, dictionary, memo) == 1:
                        memo[index] = 1
                        break
        if memo[index] == -1:
            memo[index] = 0
        return memo[-1] == 1

    """
        TC: O(N^2)
        SC: O(N)
    """


sol = Solution()
print(sol.isSubWords(s="BLUEGREENLIGHT", index=0, size=17, dictionary={"BLUE": 1, "GREEN": 1, "AND": 1, "LIGHT": 1}))
print(sol.isSubWords(s="BLUEOFGREENLIGHT", index=0, size=17, dictionary={"BLUE": 1, "GREEN": 1, "AND": 1, "LIGHT": 1}))
print(sol.isSubWords(s="BLUEANDGREENLIGHT", index=0, size=17, dictionary={"BLUE": 1, "GREEN": 1, "AND": 1, "LIGHT": 1}))
print("*"*100)
mem = [-1 for _ in range(17)]
print(sol.isSubWordsTopDown(s="BLUEGREENLIGHT", index=0, size=17, dictionary={"BLUE": 1, "GREEN": 1, "AND": 1, "LIGHT": 1}, memo=mem))
print(sol.isSubWordsTopDown(s="BLUEOFGREENLIGHT", index=0, size=17, dictionary={"BLUE": 1, "GREEN": 1, "AND": 1, "LIGHT": 1}, memo=mem))
print(sol.isSubWordsTopDown(s="BLUEANDGREENLIGHT", index=0, size=17, dictionary={"BLUE": 1, "GREEN": 1, "AND": 1, "LIGHT": 1}, memo=mem))

