class Solution:
    def maxRectangleSum(self, matrix):
        # Get the total number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])
        # This is the max rectangle that we will update along the way
        maxRectangle = self._Rectangle()

        # We will try all left bound plantings from index 0 to index cols - 1
        for left in range(cols):
            # We will reset the running row sums all to 0 since this is a new planting of the left bound
            running_rows_sum = [0] * rows
            # For each left bound, we will try all of the right bounds starting at the left bound we are planted at.
            for right in range(left, cols):
                # Add all items in column 'right' to their respective row's running sum
                for i in range(rows):
                    running_rows_sum[i] += matrix[i][right]
                # Perform Kadane's algorithm on the running sum array so that we can determine the best top and bottom
                # bound to choose for the rectangle.
                kadane_result = self._kadane(running_rows_sum)
                # If we notice that this rectangle can achieve a better maxSum than the best we have done so far then
                # we need to adjust our new best
                if kadane_result.max_sum > maxRectangle.interiorSum:
                    # Set a new interiorSum for our maxRectangle
                    maxRectangle.interiorSum = kadane_result.max_sum
                    # The left and the right of the maxRectangle become the 'left' and 'right' where our for loop
                    # pointers are sitting
                    maxRectangle.leftBorderIndex = left
                    maxRectangle.rightBorderIndex = right
                    # Our top and bottom bounds for the max rectangle are going to be the startIndex and endIndex of
                    # the max sub-array region in the 'runningRowSums' sum cache (respectively).
                    maxRectangle.topBorderIndex = kadane_result.start_index
                    maxRectangle.bottomBorderIndex = kadane_result.end_index

        return maxRectangle

    def _kadane(self, arr):
        max_so_far = 0
        max_region_start = -1
        max_region_end = -1
        cur_start = 0
        running_max = 0
        for i in range(len(arr)):
            running_max += arr[i]
            if running_max < 0:
                running_max = 0
                cur_start = i +1
            if running_max > max_so_far:
                max_region_start = cur_start
                max_region_end = i
                max_so_far = running_max
        return self._KadaneResult(max_so_far, max_region_start, max_region_end)

    class _KadaneResult:
        def __init__(self, max_sum, start_index, end_index):
            self.max_sum = max_sum
            self.start_index = start_index
            self.end_index = end_index

    class _Rectangle:
        def __init__(self):
            self.interiorSum = 0
            self.leftBorderIndex = 0
            self.rightBorderIndex = 0
            self.topBorderIndex = 0
            self.bottomBorderIndex = 0
        def rec_dimensions(self):
            print((self.topBorderIndex, self.leftBorderIndex), (self.topBorderIndex, self.rightBorderIndex),
                  (self.bottomBorderIndex, self.leftBorderIndex), (self.bottomBorderIndex, self.rightBorderIndex))

table = [
    [6, -5, -7, 4, -4],
    [-9, 3, -6, 5, 2],
    [-10, 4, 7, -6, 3],
    [-8, 9, -3, 3, -7]
]
sol = Solution()
abc = sol.maxRectangleSum(matrix=table)
abc.rec_dimensions()
