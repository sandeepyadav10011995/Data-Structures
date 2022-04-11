"""
------------------------------------------------ SLIDING WINDOW --------------------------------------------------------
Types of Sliding Window -:
1. Fixed Length : When k, i.e. sliding window size is provided as a constraint.
2. Dynamic Variant: Caterpillar

How to recognize these problems ?
Things we iterate over sequentially;
    a. Contiguous Sequence of elements.
    b. Sliding arrays, linked-lists

In terms of the way questions are asked ? => Min, Max, Largest, Shortest
Questions Variants
1. Fixed Length: Max Sub-array of size k
2. Dynamic Variant: Smallest Sum (equal to S) => Will need to use Auxiliary DS, i.e. Arrays or Hashmap
                    a. Largest sub-string with no more than k distinct characters.
                    b. String Permutations

Question:   Given a string and a list of words, find all the starting indices of substrings in the given string that
            are a concatenation of all the given words exactly once without any overlapping of words. It is given that
            all words are of the same length.


Algo :  This problem follows the Sliding Window pattern and has a lot of similarities with Maximum Sum Sub-array of Size
        K. We will keep track of all the words in a HashMap and try to match them in the given string. Here are the set
        of steps for our algorithm:
            1.  Keep the frequency of every word in a HashMap.
            2.  Starting from every index in the string, try to match all the words.
            3.  In each iteration, keep track of all the words that we have already seen in another HashMap.
            4.  If a word is not found or has a higher frequency than required, we can move on to the next character in
                the string.
            5.  Store the index if we have found all the words.

Example 1:
    Input: String="catfoxcat", Words=["cat", "fox"]
    Output: [0, 3]
    Explanation: The two substring containing both the words are "catfox" & "foxcat".

Example 2:
    Input: String="catcatfoxfox", Words=["cat", "fox"]
    Output: [3]
    Explanation: The only substring containing both the words is "catfox".

------------------------------------------------------ CODE ------------------------------------------------------------
"""
from typing import List


class WordConcatenation:
    @staticmethod
    def find_word_concatenation(str1: str, words: List[str]) -> List[int]:
        result_indices = []
        words_count = len(words)
        word_length = len(words[0])
        # Edge Case
        if words_count == 0 or word_length == 0:
            return result_indices

        words_freq = {}
        for word in words:
            if word not in words_freq:
                words_freq[word] = 0
            words_freq[word] += 1

        # try to extend the range [window_start, window_end]
        for i in range((len(str1)-words_count*word_length)+1):
            words_seen = {}
            for j in range(0, words_count):
                next_word_index = i + j * word_length
                # Get the next word from the string
                word = str1[next_word_index:next_word_index+word_length]
                if word not in words_freq:  # Break if we don't need this word
                    break
                # Add the word to the 'words_seen' dict
                if word not in words_seen:
                    words_seen[word] = 0
                words_seen[word] += 1

                # No need to process further if the word has higher frequency than required
                if words_seen[word] > words_freq.get(word, 0):
                    break

                if j + 1 == words_count:  # Store index if we have found all the words
                    result_indices.append(i)

        return result_indices


def main():
    wc = WordConcatenation()
    print(wc.find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(wc.find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()

"""
Overall TC : O(N+M) --> O(N*M*Len)
Overall SC: O(M) --> O(N+M)
"""
