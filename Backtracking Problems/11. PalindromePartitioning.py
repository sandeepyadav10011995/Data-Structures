class Solution:
    decompositions = []
    def partition(self, s):
        self._decomposeString(0, s)
        return self.decompositions

    def _decomposeString(self, work_index, string, partial_decomposition=[]):
        # If we have decomposed the whole string then reap the 'partialDecomposition', it is now complete. --> Our Goal
        if work_index == len(string):
            self.decompositions.append(partial_decomposition[:])
            return
        # Take every snippet take from the 'workingIndex' to the end of the string. This is out 'possibility space'
        # that we can recurse into.
        for i in range(work_index, len(string)):
            if self._isPalindrome(work_index, i, string):
                # Our Choices
                # 1.) Choose - Take the snippet & add it to our decomposition 'path'
                palindrome_snippet = string[work_index:i + 1]
                partial_decomposition.append(palindrome_snippet)
                # 2.) Explore - Recurse and advance progress 1 past right bound of the 'palindromicSnippet' which is
                # 'i + 1'
                self._decomposeString(i + 1, string, partial_decomposition)
                # 3.) Un-choose - We are done searching, remove the snippet from our 'path'. Next loop iteration will
                # try another snippet in this stack frame.
                partial_decomposition.pop()

    @staticmethod
    def _isPalindrome(left, right, string):
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True

sol = Solution()
print(sol.partition("aab"))
