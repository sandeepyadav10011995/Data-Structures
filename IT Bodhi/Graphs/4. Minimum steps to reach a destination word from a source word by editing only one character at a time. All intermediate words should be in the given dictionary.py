"""
Problem -: Minimum steps to reach a destination word from a source word by editing only one character at a time. All
           intermediate words should be in the given dictionary

Important Facts:
Example -: Four-letter words ::  _ _ _ _
Edit Word --> 25 * 4 = 100 :: 25 25 25 25
Delete --> 4  :: 1 1 1 1
Insert --> 26*5 = 130 ::  |_|_|_|_|

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

"""

