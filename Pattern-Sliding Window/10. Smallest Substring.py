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

Question:   Given a string and a pattern, find the smallest substring in the given string which has all the character
            occurrences of the given pattern.

    Algo:
        This problem follows the Sliding Window pattern and has a lot of similarities with Permutation in a String with
        one difference. In this problem, we need to find a substring having all characters of the pattern which means
        that the required substring can have some additional characters and doesn’t need to be a permutation of the
        pattern. Here is how we will manage these differences:

        1.  We will keep a running count of every matching instance of a character.
        2.  Whenever we have matched all the characters, we will try to shrink the window from the beginning, keeping
            track of the smallest substring that has all the matching characters.
        3.  We will stop the shrinking process as soon as we remove a matched character from the sliding window. One
            thing to note here is that we could have redundant matching characters, e.g., we might have two ‘a’ in the
            sliding window when we only need one ‘a’. In that case, when we encounter the first ‘a’, we will simply
            shrink the window without decrementing the matched count. We will decrement the matched count when the
            second ‘a’ goes out of the window.

Example:
    Input: String="aabdec", Pattern="abc"
    Output: "abdec"
    Explanation: The smallest substring having all characters of the pattern is "abdec"

------------------------------------------------------ CODE ------------------------------------------------------------
"""


class SmallestSubstring:
    @staticmethod
    def find_substring(str1: str, pattern: str) -> str:
        matched = 0
        sub_start = 0
        window_start = 0
        min_length = len(str1) + 1
        char_freq = {}
        for chr in pattern:
            if chr not in char_freq:
                char_freq[chr] = 0
            char_freq[chr] += 1

        # try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char in char_freq:
                # decrement the frequency of matched character
                char_freq[right_char] -= 1
                if char_freq[right_char] >= 0:  # Count every matching of a character
                    matched += 1

            # Shrink the window if we can, finish as soon as we remove a matched character
            while matched == len(pattern):
                if min_length > window_end - window_start + 1:
                    min_length = window_end - window_start + 1
                    sub_start = window_start

                left_char = str1[window_start]
                window_start += 1
                if left_char in char_freq:
                    if char_freq[left_char] == 0:
                        matched -= 1
                    char_freq[left_char] += 1

        if min_length > len(str1):
            return ""
        return str1[sub_start:sub_start + min_length]


def main():
    sss = SmallestSubstring()
    print(sss.find_substring("aabdec", "abc"))
    print(sss.find_substring("aabdec", "abac"))
    print(sss.find_substring("abdbca", "abc"))
    print(sss.find_substring("adcad", "xz"))


main()

"""
Overall TC : O(N+M) --> O(N+M)
Overall SC: O(M) --> O(M)
"""
