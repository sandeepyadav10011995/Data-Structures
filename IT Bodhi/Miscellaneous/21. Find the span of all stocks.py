"""
Problem : Find the span of all stocks.
Span :: How long we can move on the left side till the price is greater than prev prices.
Example -: arr = [5, 10, 8, 6, 12, 9, 4, 5, 6]
           span = 1  2   1  1   5  1  1  2  3

Approach 1: Brute Force : For every number see on the count of values less on the left.
        TC: O(N^2)

Approach 2: Using Stack using index
            Step 1: Push the entry in the stack
                    Entry -> (value, index)
            Step 2: Keep popping the element from the stack until the stack top entry value > cur entry value
            Step 3: New Entry index = Popped entry index
        TC: O(N)
        SC: O(N)

"""
from dataclasses import dataclass


@dataclass
class StockEntry:
    value: int
    startIdx: int


class Solution:
    @staticmethod
    def findStocksSpan(prices: list[int]) -> list[int]:
        N = len(prices)
        spanResult = []

        stack = []
        for i in range(N):
            stockEntry = StockEntry(value=prices[i], startIdx=i)
            while stack and stack[-1].value < stockEntry.value:
                poppedEntry = stack.pop()
                stockEntry.startIdx = poppedEntry.startIdx
            stack.append(stockEntry)
            spanResult.append(i-stockEntry.startIdx+1)

        return spanResult


sol = Solution()
print(sol.findStocksSpan(prices=[5, 10, 8, 6, 12, 9, 4, 5, 6]))
