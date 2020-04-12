"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""

# 1st Approach
class MinStack:
  def __init__(self):
    """
    initialize your data structure here.
    """
    self.stack = []
  
  def push(self, x: int) -> None:
    self.stack.append(x)
  
  def pop(self) -> None:
    if len(self.stack) > 0:
      self.stack.pop()
    return
  
  def top(self) -> int:
    if len(self.stack) > 0:
      return self.stack[len(self.stack)]
    return -1
  
  def getMin(self) -> int:
    if len(self.stack) > 0:
      return min(self.stack)
    return -1
  
# Optimized Approach --> Making all the function call time to -> O(1)
class MinStack:
    def __init__(self):
        self.stack = []
    
    def push(self, x: int) -> None:
        if self.stack:
            cur_min = min(self.stack[-1][1], x)
            self.stack.append((x, cur_min))
        else:
            self.stack.append((x, x))
   
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
    
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return -1
    
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return -1
  
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()  
