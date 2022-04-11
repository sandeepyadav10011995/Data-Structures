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

Question:   You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two
            baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets. You will be
            given an array of characters where each character represents a fruit tree.
            The farm has following restrictions:
                1. Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
                2. You can start with any tree, but you can’t skip a tree once you have started. --> Contiguous
                3. You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have
                   to pick from a third fruit type.
            Write a function to return the maximum number of fruits in both baskets.

Algorithm:
        1.  First, we will insert characters from the beginning of the string until we have K distinct characters
            in the HashMap.
        2.  These characters will constitute our sliding window. We are asked to find the longest such window having
            no more than K distinct characters. We will remember the length of this window as the longest window so far.
        3.  After this, we will keep adding one character in the sliding window (i.e., slide the window ahead) in a
            stepwise fashion.
        4.  In each step, we will try to shrink the window from the beginning if the count of distinct characters in
            the HashMap is larger than K. We will shrink the window until we have no more than K distinct characters in
            the HashMap. This is needed as we intend to find the longest window.
        5.  While shrinking, we’ll decrement the character’s frequency going out of the window and remove it from the
            HashMap if its frequency becomes zero.
        6.  At the end of each step, we’ll check if the current window length is the longest so far, and if so, remember
            its length.

Example:
Output:

------------------------------------------------------ CODE ------------------------------------------------------------
"""


class FruitsAndBaskets:
    @staticmethod
    def fruits_into_baskets(str1: str, K: int = 2) -> int:
        max_length = 0
        window_start = 0
        fruits_freq = {}
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char not in fruits_freq:
                fruits_freq[right_char] = 0
            fruits_freq[right_char] += 1
            # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
            while len(fruits_freq) > K:  # K value is hard-coded i.e. 2
                left_char = str1[window_start]
                fruits_freq[left_char] -= 1
                if fruits_freq[left_char] == 0:
                    del fruits_freq[left_char]
                window_start += 1  # shrink the window
            # remember the max_length so far
            max_length = max(max_length, window_end - window_start + 1)
        return max_length


def main():
    fab = FruitsAndBaskets()
    print("Maximum number of fruits: " + str(fab.fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fab.fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()

"""
Overall TC : O(2N) --> O(N)
Overall SC: O(1) --> O(1)  # Bcz at max fruit_freq will store only 3 types of fruits !!

Similar Problems
Problem 1: Longest Substring with at most 2 distinct characters. Given a string, find the length of the longest 
           substring in it with at most two distinct characters.

Solution: This problem is exactly similar to our parent problem.

"""
