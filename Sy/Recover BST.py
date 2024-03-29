Time: O(n)
Space: O(h)

class Solution:
  def recoverTree(self, root: Optional[TreeNode]) -> None:
    def swap(x: Optional[TreeNode], y: Optional[TreeNode]) -> None:
      temp = x.val
      x.val = y.val
      y.val = temp

    def inorder(root: Optional[TreeNode]) -> None:
      if not root:
        return

      inorder(root.left)

      if self.pred and root.val < self.pred.val:
        self.y = root
        if not self.x:
          self.x = self.pred
        else:
          return
      self.pred = root

      inorder(root.right)

    inorder(root)
    swap(self.x, self.y)

  pred = None
  x = None  # 1st wrong node
  y = None  # 2nd wrong node

Approach 2: Iterative (stack)
Time: O(n)
Space: O(h)


class Solution:
  def recoverTree(self, root: Optional[TreeNode]) -> None:
    pred = None
    x = None  # 1st wrong node
    y = None  # 2nd wrong node
    stack = []

    while root or stack:
      while root:
        stack.append(root)
        root = root.left
      root = stack.pop()
      if pred and root.val < pred.val:
        y = root
        if not x:
          x = pred
      pred = root
      root = root.right

    def swap(x: Optional[TreeNode], y: Optional[TreeNode]) -> None:
      temp = x.val
      x.val = y.val
      y.val = temp

    swap(x, y)

Approach 3: Morris
Time: O(n)O(n)
Space: O(1)O(1)

class Solution:
  def recoverTree(self, root: Optional[TreeNode]) -> None:
    pred = None
    x = None  # 1st wrong node
    y = None  # 2nd wrong node

    def findPredecessor(root: Optional[TreeNode]) -> Optional[TreeNode]:
      pred = root.left
      while pred.right and pred.right != root:
        pred = pred.right
      return pred

    while root:
      if root.left:
        morrisPred = findPredecessor(root)
        if morrisPred.right:  # already connected before
          # start the main logic
          if pred and root.val < pred.val:
            y = root
            if not x:
              x = pred
          pred = root
          # end of the main logic
          morrisPred.right = None  # break the connection
          root = root.right
        else:
          morrisPred.right = root  # connect it!
          root = root.left
      else:
        # start the main logic
        if pred and root.val < pred.val:
          y = root
          if not x:
            x = pred
        pred = root
        # end of the main logic
        root = root.right

    def swap(x: Optional[TreeNode], y: Optional[TreeNode]) -> None:
      temp = x.val
      x.val = y.val
      y.val = temp

    swap(x, y)
