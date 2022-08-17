
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # Iterative Approach
        if root is None:
            return root
        queue = [root]
        while queue:
            count = len(queue)
            while count:
                node = queue.pop(0)
                if count != 1:
                    node.next = queue[0]
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                count -= 1
        return root
