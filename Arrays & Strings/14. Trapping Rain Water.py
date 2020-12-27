class Solution:
    def trappingWater(self, heights):
        """
        Brute Force : For every building find the left_max and right_max and
        trapped water = min(left_max, right_max)- height[building] --> Time O(N^2) and O(1) Space

        DP : Make two arrays i.e. left_max_array and right_max_array and then apply same logic --> Time O(N) and Space O(N)
        Two Pointers : Time O(N) and Space O(1)
        :param heights:
        :return:
        """
        ans = 0
        left, right = 0, len(heights)-1
        left_max, right_max = 0, 0
        while left < right:
            if heights[left] < heights[right]:
                if heights[left] >= left_max:
                    left_max = heights[left]
                else:
                    ans += left_max - heights[left]
                left += 1
            else:
                if heights[right] >= right_max:
                    right_max = heights[right]
                else:
                    ans += right_max - heights[right]
                right -= 1
        return ans

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trappingWater(heights))
