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

Question:   Given a string and a pattern, find all anagrams of the pattern in the given string.
            Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while
            finding permutations of a string, we get N! permutations (or anagrams) of a string having N characters.
            For example, here are the six anagrams of the string “abc”:
                abc
                acb
                bac
                bca
                cab
                cba
            Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

    Algo:
        This problem follows the Sliding Window pattern and is very similar to Permutation in a String. In this problem,
        we need to find every occurrence of any permutation of the pattern in the string. We will use a list to store
        the starting indices of the anagrams of the pattern in the string.

Example:
    Input: String="ppqp", Pattern="pq"
    Output: [1, 2]
    Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".


------------------------------------------------------ CODE ------------------------------------------------------------
"""
from typing import List


class Anagrams:
    @staticmethod
    def find_string_anagrams(str1: str, pattern: str) -> List[int]:
        matched = 0
        window_start = 0
        char_freq = {}
        for chr in pattern:
            if chr not in char_freq:
                char_freq[chr] = 0
            char_freq[chr] += 1

        result_indices = []
        # Our goal is to match all the characters from the 'char_frequency' with the current window
        # try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char in char_freq:
                # decrement the frequency of matched character
                char_freq[right_char] -= 1
                if char_freq[right_char] == 0:
                    matched += 1
            if matched == len(char_freq):
                result_indices.append(window_start)

            # shrink the window by one character
            if window_end >= len(pattern) - 1:
                left_char = str1[window_start]
                window_start += 1
                if left_char in char_freq:
                    if char_freq[left_char] == 0:
                        matched -= 1
                    char_freq[left_char] += 1

        return result_indices


def main():
    ana = Anagrams()
    print(ana.find_string_anagrams("ppqp", "pq"))
    print(ana.find_string_anagrams("abbcabc", "abc"))


main()

"""
Overall TC : O(N+M) --> O(N+M)
Overall SC: O(M) --> O(M)
"""
