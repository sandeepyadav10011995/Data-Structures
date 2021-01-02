"""
Given a list of prefixes prefixes and a sentence sentence, replace all words in sentence that start with any of the given prefixes in prefixes.

Example:
Inputs:
prefixes = ["cat", "catch", "Alabama"]
sentence = "The cats were catching yarn"

Output: "The cat were cat yarn"
Explanation: "cats" and "catching" were both replaced by their shortest prefix match "cat"

Note:
The shortest matching prefix will win when a word matches multiple prefixes
"""

class Solution:
    def replaceWordsWithPrefix(self, prefixes, sentence):
        words = sentence.split(' ')
        prefix_map = {prefix: True for prefix in prefixes}

        for idx in range(0, len(words)):
            word = words[idx]
            for letter_idx in range(0, len(word)):
                if word[0:letter_idx] in prefix_map:
                    # If it is there then update the word in words and break the loop !!
                    words[idx] = word[0:letter_idx]
                    break

        return ' '.join(words)

prefixes = ["cat", "catch", "Alabama"]
sentence = "The cats were catching yarn"
sol = Solution()
print(sol.replaceWordsWithPrefix(prefixes, sentence))
