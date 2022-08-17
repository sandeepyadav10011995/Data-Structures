"""
Approach 1: Brute Force
max_area = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        min_height = float("inf")
        for k in range(i, j+1):
            min_height = min(min_height, nums[k])
        max_area = max(max_area, min_height*(j-i+1))
return max_area
TC: O(N^3)
    

Approach 2: Two Pointers
max_area = 0
for i in range(len(nums)):
    min_height = float("inf")
    for j in range(i, len(nums)):
        min_height = min(min_height, nums[j])
        max_area = max(max_area, min_height*(j-1+1))
return max_area
TC: O(N^2)

Approach 3: Divide And Conquer
start = 0
end = len(nums) - 1

# Edge Case
if start > end: return 0
min_index = start

for i in range(start, end+1):
    if nums[min_index] > nums[i]:
        min_index = i
    return max(nums[min_index]*(end-start+1), lra(nums, start, min_index-1), lra(nums, min_index+1, end))

Approach 4: Stack

class StackData:
    def __init__(self, h, si)
        self.h = h
        self.si = si

max_area = float("-inf")
size = len(heights)

# Base Case
if size < 1: return 0

stack = [StackData(heights[0], 0)]
cvsi = 0
for i in range(1, size):
    cvsi = i
    while stack and stack[-1].h > heights[i]:
        top = stack.pop()
        cvsi = top.si
        area = top.h*(i-cvsi)
        max_area = max(max_area, area)
    stack.append(StackData(heights[i], cvsi))
    
    # Important
    while stack:
        top = stack.pop()
        area = top.h*(size-top.si)
        max_area = max(max_area, area)
return max_area



"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
