"""
Problem : Rain water collected in a histogram structure.

Approach 1: Brute Force
            For every building find the leftMax and rightMax and trapped water = min(leftMax, rightMax) - heights[building]
         TC: O(N^2)
         SC: O(1)

Approach 2: DP
            Make two array i.e, leftMaxArray and rightMaxArray and then apply the same logic
        TC: O(N)
        SC: O(N)

Approach 2: DP Optimized i.e, Two Pointer Approach
        For every building we need to decide whether left building or right building will trap the water.
        TC: O(N)
        SC: O(1)
Problem -: What if when we have multiple max heights building.

Follow Up-: Container With Most Water
Same Two Pointer Approach


"""

class RainWater:
    @staticmethod
    def trappingWater(heights: list[int]) -> int:
        N = len(heights)
        trappedWater = 0
        left, right = 0, N-1
        leftMax, rightMax = 0, 0
        while left < right:
            if heights[left] < heights[right]:
                if heights[left] >= leftMax:
                    leftMax = heights[left]
                else:
                    trappedWater += leftMax - heights[left]
                left += 1
            else:
                if heights[right] >= rightMax:
                    rightMax = heights[right]
                else:
                    trappedWater += rightMax - heights[right]
                right -= 1

        return trappedWater


rw = RainWater()
buildingHeights = [6, 8, 5, 3, 2, 4, 6, 9, 11, 7, 3, 2, 5, 6, 9, 5, 2, 5, 7, 5, 3, 2, 1]
buildingHeights2 = [6, 8, 5, 3, 2, 4, 6, 9, 11, 7, 3, 2, 5, 11, 9, 5, 2, 5, 7, 5, 3, 2, 1]
print(rw.trappingWater(heights=buildingHeights))
print(rw.trappingWater(heights=buildingHeights2))

"""
Follow Up -: Container With Most Water
Ex-: heights = [1,8,6,2,5,4,8,3,7]
"""


class Container:
    @staticmethod
    def maxArea(heights: list[int]) -> int:
        N = len(heights)
        maxArea = 0
        left, right = 0, N-1

        while left < right:
            maxArea = max(maxArea, min(heights[left], heights[right])*(right-left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea


container = Container()
cHeights = [1,8,6,2,5,4,8,3,7]
print(container.maxArea(heights=cHeights))
