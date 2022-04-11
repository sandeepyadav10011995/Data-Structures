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

Question:   Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any
            letter, find the length of the longest substring having the same letters after replacement.

    Algo:
    1.  We will iterate through the string to add one letter at a time in the window.
    2.  We will also keep track of the count of the maximum repeating letter in any window (let’s call it
        maxRepeatLetterCount).
    3.  So, at any time, we know that we do have a window with one letter repeating maxRepeatLetterCount times; this
        means we should try to replace the remaining letters.
        a.  If the remaining letters are less than or equal to k, we can replace them all.
        b.  If we have more than k remaining letters, we should shrink the window as we cannot replace more than k
            letters.

    While shrinking the window, we don’t need to update maxRepeatLetterCount (hence, it represents the maximum repeating
    count of ANY letter for ANY window). Why don’t we need to update this count when we shrink the window? Since we have
    to replace all the remaining letters to get the longest substring having the same letter in any window, we can’t get
    a better answer from any other window even though all occurrences of the letter with frequency maxRepeatLetterCount
    is not in the current window.

Example:
    Input: String="aabccbb", k=2
    Output: 5
    Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".


------------------------------------------------------ CODE ------------------------------------------------------------
"""


class LongestSubstringReplacement:
    @staticmethod
    def length_of_longest_substring(str1: str, k: int) -> int:
        max_length = 0
        window_start = 0
        max_repeat_letter_count = 0
        freq_map = {}
        # try to extend the range [windowStart, windowEnd]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char not in freq_map:
                freq_map[right_char] = 0
            freq_map[right_char] += 1
            max_repeat_letter_count = max(max_repeat_letter_count, freq_map[right_char])
            # Current window size is from window_start to window_end, overall we have a letter which is
            # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
            # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
            # if the remaining letters are more than 'k', it is the time to shrink the window as we
            # are not allowed to replace more than 'k' letters
            if window_end-window_start+1 - max_repeat_letter_count > k:
                left_char = str1[window_start]
                freq_map[left_char] -= 1
                window_start += 1
            max_length = max(max_length, window_end-window_start+1)
        return max_length


def main():
    lsr = LongestSubstringReplacement()
    print(lsr.length_of_longest_substring("aabccbb", 2))
    print(lsr.length_of_longest_substring("abbcb", 1))
    print(lsr.length_of_longest_substring("abccde", 1))


main()

"""
Overall TC : O(N) --> O(N)
Overall SC: O(K) --> O(1)  # Bcz at max char_index_map will store only K=26 english alphabets. So K <= N and K max 
                             value is 26

"""
