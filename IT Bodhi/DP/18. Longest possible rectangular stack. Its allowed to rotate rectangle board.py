"""
Problem : Longest possible rectangular stack.
Ex: rec = [(4, 6), (2, 3), (3, 1), (6, 3), (5, 5)]

Follow Up-: It's allowed to rotate rectangle board
Then put both the combinations in the array.

"""


class Solution:
    @staticmethod
    def maxRectangleStack(rectangles: list) ->int:
        N = len(rectangles)
        lis = [1 for _ in range(N)]
        rectangles.sort(key=lambda x: x[0])

        maxRecStacks = 0
        for i in range(1, N):
            for j in range(i):
                if rectangles[i][1] > rectangles[j][1] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
            maxRecStacks = max(maxRecStacks, lis[i])

        return maxRecStacks

    @staticmethod
    def maxRectangleStackWithRotationAllowed(rectangles: list) -> int:
        N = len(rectangles)
        newRectangles = []
        for x, y in rectangles:
            newRectangles.extend(((x, y), (y, x)))
        maxRectangleLIS = [1 for _ in range(2*N)]
        # When duplicates are expected then go if you want data to be sorted w.r.t Length and Then Breadth.
        # Then sort w.r.t Breadth --> sort w.r.t Length.
        newRectangles.sort(key=lambda x: x[1])  # First
        newRectangles.sort(key=lambda x: x[0])  # Second --> This is the final sort.

        maxRecStacks = 0
        for i in range(1, 2*N):
            for j in range(i):
                if newRectangles[i][1] > newRectangles[j][1] and maxRectangleLIS[i] < maxRectangleLIS[j] + 1:
                    maxRectangleLIS[i] = maxRectangleLIS[j] + 1
            maxRecStacks = max(maxRecStacks, maxRectangleLIS[i])

        return maxRecStacks

sol = Solution()
rectangle=[(4, 6), (2, 3), (3, 1), (6, 3), (5, 5)]
print(sol.maxRectangleStack(rectangle))
print(sol.maxRectangleStackWithRotationAllowed(rectangle))
