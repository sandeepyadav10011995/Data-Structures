"""
Problem : Implement Queue with getMax() feature

The optimized implementation uses a deque to store the elements in the max_queue list, with the largest element at the
front of the deque and the smallest element at the back. This allows the enqueue() method to add elements to the back of
the max_queue list in O(1) time on average, because the smaller elements are automatically removed from the back of the
deque when a larger element is added to the front. The worst case time complexity of enqueue() is still O(n) when the
elements are added to the queue in non-decreasing order, but this case is less common in practice.
"""


class MaxQueue:
    def __init__(self):
        self.queue = []
        self.max_queue = []

    def enqueue(self, val):
        self.queue.append(val)
        # Remove the elements smaller than the current element from the back of the max_queue
        while self.max_queue and self.max_queue[-1] < val:
            self.max_queue.pop()
        self.max_queue.append(val)

    def dequeue(self):
        if not self.queue:
            return None
        val = self.queue.pop(0)
        if val == self.max_queue[0]:
            self.max_queue.pop(0)
        return val

    def getMax(self):
        if not self.max_queue:
            return None
        return self.max_queue[0]
