"""
Kth max diff pair

Given an array, Arr = [2, 6, 8, 9, 12, 15, 18, 21, 25, 28, 30, 35]
Return Kth Pair with Max Diff  --> (j, i) => Diff(Arr[j] - Arr[i]) is Kth Largest

Data Structure Used --> MaxHeap, HashMap or Tuple
HeapNode -: Diff Val|StartIndex|EndIndex

Next Value Pushed to Heap would be two values i.e.
            Diff Val|StartIndex+1|EndIndex
            Diff Val| StartIndex|EndIndex-1

            (i, j) --> (i+1, j) , (i, j-1)
If the signature already exists then don't put it in the MaxHeap\
Keep doing this for K iterations.

IN THIS CASE STARTING POINT IS (0, N-1)

TC: O(K*logK)
SC: O(K)

===========================================================================================


Kth min diff pair --> Consecutive Numbers will have min diff

Given an array, Arr = [2, 6, 8, 9, 12, 15, 18, 21, 25, 28, 30, 35]
Return Kth Pair with Max Diff  --> (j, i) => Diff(Arr[j] - Arr[i]) is Kth Smallest

Data Structure Used --> MinHeap, HashMap or Tuple
In starting (i, i+1) will pe pushed.
HeapNode -: Diff Val|StartIndex|EndIndex

While popping the Node it would be pushing two values i.e.
            Diff Val|StartIndex-1|EndIndex
            Diff Val| StartIndex|EndIndex+1

            (i, j) --> (i-1, j), (i, j+1)

Do this for K iterations

IN THIS CASE STARTING POINTS IS NOT KNOWN.

TC: O(K*logN)
SC: O(N)

"""

