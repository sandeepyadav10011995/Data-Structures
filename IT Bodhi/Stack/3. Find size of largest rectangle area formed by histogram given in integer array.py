"""
Problem : Find size of largest rectangle area formed by histogram given in integer array

Approach 1: BruteForce Solution --> O(N^3)

Approach 2: Two Pointers --> O(N^2)

Approach 3: Divide And Conquer --> O(N*logN)
            Worst Case -: O(N^2) --> sorted array
            SC: O(N)

Approach 4: Using Stack --> O(N)
            SC: O(N)
            Will need another data type to store the data as Nodes in stack

"""
import math


class BFSolution:
    @staticmethod
    def largestRectangleArea(nums: list[int]) -> int:
        maxArea = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                minHeight = math.inf
                for k in range(i, j+1):
                    minHeight = min(minHeight, nums[k])
                maxArea = max(maxArea, minHeight * (j-i+1))

        return maxArea


class TwoPointersSolution:
    @staticmethod
    def largestRectangleArea(nums: list[int]) -> int:
        maxArea = 0
        for i in range(len(nums)):
            minHeight = math.inf
            for j in range(i, len(nums)):
                minHeight = min(minHeight, nums[j])
                maxArea = max(maxArea, minHeight * (j-i+1))

        return maxArea


class DivideAndConquerSolution:
    def largestRectangleArea(self, nums: list[int], start, end) -> int:
        # Base Case
        if start > end:
            return 0

        minIndex = start
        for i in range(start, end+1):
            if nums[minIndex] > nums[i]:
                minIndex = i

        return max(nums[minIndex] * (end-start+1),
                   self.largestRectangleArea(nums, start, minIndex-1),
                   self.largestRectangleArea(nums, minIndex+1, end))


class StackData:
    def __init__(self, height, startingIndex):
        self.height = height
        self.startingIndex = startingIndex


class StackSolution:
    @staticmethod
    def largestRectangleArea(heights: list[int]) -> int:
        maxArea = -math.inf
        size = len(heights)

        # Base Case
        if size < 1:
            return 0

        stack = [StackData(height=heights[0], startingIndex=0)]
        for i in range(1, size):
            curValStartingIndex = i
            while stack and stack[-1].height >= heights[i]:
                top = stack.pop()
                curValStartingIndex = top.startingIndex
                area = top.height * (i - curValStartingIndex)
                maxArea = max(maxArea, area)

            stack.append(StackData(height=heights[i], startingIndex=curValStartingIndex))

        # Imp: There could be some elements left in the stack, traverse them as well
        while stack:
            top = stack.pop()
            area = top.height * (size - top.startingIndex)
            maxArea = max(maxArea, area)

        return maxArea
