from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> []:
        queue = deque()
        queue.append(root)
        output = []
        while queue:
            current_length = len(queue)
            max_val = queue[0]
            for i in range(current_length):
                current_node = queue.popleft()
                max_val = max(max_val,current_node.val)
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            output.append(max_val)
        return output

