"""
Problem : Implement Stack with getMin() feature

The optimized implementation uses a separate stack to store the minimum elements encountered so far. The push() method
adds elements to both the main stack and the minimum stack in O(1) time. If the value being pushed is less than or equal
to the current minimum value on the minimum stack, it is added to the minimum stack as well. The pop() method removes
elements from both the main stack and the minimum stack in O(1) time. If the value being popped is the current minimum
value on the minimum stack, it is removed from the minimum stack as well. The getMin() method returns the current
minimum value on the minimum stack in O(1) time.

"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.stack:
            return None
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def getMin(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]
