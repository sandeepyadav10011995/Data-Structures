"""
Given an input sequence arr, generate its power set.

A "power set" is the set of all subsets that can be formed from a sequence/set.

A set is a collection of distinct objects. A subset is a set that only contains elements found in the original set.

Example:
Input: [1, 2, 3]
Output:
[
  [], # the empty set
  [1,2,3],
  [1,2],
  [1,3],
  [1],
  [2,3],
  [2],
  [3]
]

Constraints:
All items in the provided sequence will be unique
"""
class Solution:
    def powerset(self, inputSet):
        '''
        :type inputSet: list of int
        :rtype: list of list of int
        '''
        self.powerset = []
        self.generatePowerset(0, inputSet)
        return self.powerset
        
    def generatePowerset(self, cur_idx, inputSet, subset=[]):
        # Base Case --> Our Goal
        if cur_idx == len(inputSet):
            self.powerset.append(subset[:])
            return
        
        # Two Cases
        # Yes --> Consider The Item
        subset.append(inputSet[cur_idx]) # Our Choice
        self.generatePowerset(cur_idx+1, inputSet, subset) # Explore
        subset.pop() # Unchoose --> Backtrack
        
        # No --> Don't consider The Item
        self.generatePowerset(cur_idx+1, inputSet, subset)

