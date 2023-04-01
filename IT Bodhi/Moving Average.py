"""
Problem : Create a program that measures server latency periodically. The program receives one latency (ping) value at
          a time and after each value is received, calculates the average latency for the latest K values.
K = 5
50, 60, 70, 50, 100, 10, ...more values to come later
The values in window (i.e. latest `K` values) should be (60, 70, 50, 100, 10)
The next value 40 comes in. The window is now (70, 50, 100, 10, 40).

Approach -:
    LatencyAverage:
        - init(K: int) -> None
		    - K = 5
		    - self.windowQueue = deque()
		    - self.windowSize = 0
		    - self.windowSum = 0
	    - getAvgLatencyOfPings() -> float
		    - compute the avg
	    - insertPing(pingVal: int) -> None
		    - self._reBalanceQueue()
		    - insert the element in queue and update the windowSum
	    - _reBalanceQueue() -> None
		    - remove the element from queue if size > K
		    - update the windowSum

Follow Up -: Server may have latency spikes and we want the average latency to be tolerant of these values.
             In other words, we ignore the top X values in each K-window.

Example values:

K = 5
X = 2
For the window from previous example (60, 70, 50, 100, 10), the largest 2
values are 100 and 70.
Another example is (70, 70, 50, 100, 10), the largest 2 values are still 100 and
70, note there is another 70 that should be included in the average.




"""
from collections import deque
from heapq import *


class LatencyAverageSimple:
    def __init__(self, K: int) -> None:
        self.K = K
        self.windowQueue = deque()  # O(K) --> Space Complexity
        self.windowSize = 0
        self.windowSum = 0

    def getAvgLatencyOfPings(self) -> float:  # O(1)
        return self.windowSum / self.windowSize

    def insertPing(self, pingVal: int) -> None:  # O(1) + O(1) ~ O(1)
        if self.windowSize >= self.K:
            self._reBalanceQueue()
        # Insert the pingVal
        self.windowQueue.append(pingVal)
        # Update the windowSum and windowSize
        self.windowSum += pingVal
        self.windowSize += 1

    def _reBalanceQueue(self) -> None:  # O(1)
        # pop the first element and update the windowSum and windowSize
        eleMovingOut = self.windowQueue.popleft()
        self.windowSum -= eleMovingOut
        self.windowSize -= 1


class LatencyAverageWithTopXIgnored:
    def __init__(self, K: int, X: int) -> None:
        self.K = K
        self.X = X
        self.windowQueue = deque()
        self.windowSize = 0
        self.windowSum = 0

    def getAvgLatencyOfPings(self) -> float:  # O(K) + O(XlogK) ~ O(XlogK)
        # Make a MaxHeap of size K from queue and pop X element from it. --> XlogK
        tempWindowSum = self.windowSum
        tempSize = self.windowSize
        maxHeap = [-x for x in self.windowQueue]
        heapify(maxHeap)
        ignoredElementsSum = 0
        if self.windowSize == self.K:
            tempSize = self.K - self.X
            for _ in range(self.X):
                ignoredElementsSum += -heappop(maxHeap)
        tempWindowSum -= ignoredElementsSum
        return tempWindowSum / tempSize

    def insertPing(self, pingVal: int) -> None:
        if self.windowSize >= self.K:
            self._reBalanceQueue()
        # Update the windowSum and size
        self.windowQueue.append(pingVal)
        self.windowSum += pingVal
        self.windowSize += 1

    def _reBalanceQueue(self) -> None:
        # pop the first element and update the windowSum and size
        eleMovingOut = self.windowQueue.popleft()
        self.windowSum -= eleMovingOut
        self.windowSize -= 1


class LatencyAverageWithTopXIgnored2:
    def __init__(self, K: int, X: int) -> None:
        self.K = K
        self.X = X
        self.windowQueue = deque()
        self.windowSize = 0
        self.windowSum = 0

    def getAvgLatencyOfPings(self) -> float:  # O(K) + O(XlogK) ~ O(XlogK)
        # Make a MaxHeap of size K from queue and pop X element from it. --> XlogK
        tempWindowSum = self.windowSum
        tempSize = self.windowSize
        maxHeap = [-x for x in self.windowQueue]
        heapify(maxHeap)
        ignoredElementsSum = 0
        if self.windowSize == self.K:
            tempSize = self.K - self.X
            for _ in range(self.X):
                ignoredElementsSum += -heappop(maxHeap)
        tempWindowSum -= ignoredElementsSum
        return tempWindowSum / tempSize

    def insertPing(self, pingVal: int) -> None:
        if self.windowSize >= self.K:
            self._reBalanceQueue()
        # Update the windowSum and size
        self.windowQueue.append(pingVal)
        self.windowSum += pingVal
        self.windowSize += 1

    def _reBalanceQueue(self) -> None:
        # pop the first element and update the windowSum and size
        eleMovingOut = self.windowQueue.popleft()
        self.windowSum -= eleMovingOut
        self.windowSize -= 1


la = LatencyAverageWithTopXIgnored(K=5, X=2)
values = [60, 70, 50, 100, 10, 80, 90, 110, 20, 30]
for value in values:
    la.insertPing(pingVal=value)
    print(la.getAvgLatencyOfPings())
