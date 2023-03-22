"""
Next larger no in a BST for given no X

Approach 1: Inorder Traversal --> Return the first number greater than X.
            TC: O(N) + O(N)
            SC: O(N)

Approach 2: Optimize 1 using Binary Search
            TC: O(N) + O(logN)
            SC: O(N)

Approach 3: Simple Traversal of BST
            1. Once we find a value which is equal to greater than X
                -> Then keep going left and last left is the Answer
            2. Once we find a value which is equal to smaller than X
                -> Then keep going right and last right is the Answer

"""

