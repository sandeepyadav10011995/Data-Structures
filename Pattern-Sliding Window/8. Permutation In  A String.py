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

Question:   Given a string and a pattern, find out if the string contains any permutation of the pattern.
            Permutation is defined as the re-arranging of the characters of the string.
            For example, “abc” has the following six permutations:
                abc
                acb
                bac
                bca
                cab
                cba
                If a string has ‘n’ distinct characters, it will have n! permutations.

    Algo:
        This problem follows the Sliding Window pattern, and we can use a similar sliding window strategy as discussed
        in Longest Substring with K Distinct Characters. We can use a HashMap to remember the frequencies of all
        characters in the given pattern. Our goal will be to match all the characters from this HashMap with a sliding
        window in the given string. Here are the steps of our algorithm:
        1.  Create a HashMap to calculate the frequencies of all characters in the pattern.
        2.  Iterate through the string, adding one character at a time in the sliding window.
        3.  If the character being added matches a character in the HashMap, decrement its frequency in the map.
            If the character frequency becomes zero, we got a complete match.
        4.  If at any time, the number of characters matched is equal to the number of distinct characters in the
            pattern (i.e., total characters in the HashMap), we have gotten our required permutation.
        5.  If the window size is greater than the length of the pattern, shrink the window to make it equal to the
            pattern’s size. At the same time, if the character going out was part of the pattern, put it back in the
            frequency HashMap.

Example:
    Input: String="oidbcaf", Pattern="abc"
    Output: true
    Explanation: The string contains "bca" which is a permutation of the given pattern.


------------------------------------------------------ CODE ------------------------------------------------------------
"""


class StringPermutations:
    @staticmethod
    def find_permutation(str1: str, pattern: str) -> bool:
        matched = 0
        window_start = 0
        char_freq = {}
        for chr in pattern:
            if chr not in char_freq:
                char_freq[chr] = 0
            char_freq[chr] += 1

        # our goal is to match all the characters from the 'char_frequency' with the current window
        # try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char in char_freq:
                # decrement the frequency of matched character
                char_freq[right_char] -= 1
                if char_freq[right_char] == 0:
                    matched += 1
            if matched == len(char_freq):
                return True

            # shrink the window by one character
            if window_end >= len(pattern) - 1:
                left_char = str1[window_start]
                window_start += 1
                if left_char in char_freq:
                    if char_freq[left_char] == 0:
                        matched -= 1
                    char_freq[left_char] += 1

        return False


def main():
    sp = StringPermutations()
    print('Permutation exist: ' + str(sp.find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(sp.find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(sp.find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(sp.find_permutation("aaacb", "abc")))


main()

"""
Overall TC : O(N+M) --> O(N+M)
Overall SC: O(M) --> O(M)
"""
