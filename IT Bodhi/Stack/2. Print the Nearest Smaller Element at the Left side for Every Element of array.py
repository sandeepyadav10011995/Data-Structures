"""
Problem : Print the nearest smaller element at the left side for every element of the input integer array

Ex -: 5 8 7 12 4 10 18 13 6 9
      N 5 5 7  N  4 10 10 4 6


Brute Force -: O(N^2)
Optimized Approach -: Using Stack
            Steps :
                1.  If the value on top of the stack is small, then that is the answer.
                2.  If the value is bigger, then pop it and keep checking
                3.  If the stack is empty, then the answer is None

WORST CASE -: O (N) --> In case the array is a sorted array.
Note -: All the deletes combined cannot make more than O(N) time
        N --> for (1, N)
            - Deleting larger elements form the stack   --> O(N) --> Worst Case
            - Print next smaller    --> O(1)
            - Add the cur element to the stack  --> O(1)
"""
