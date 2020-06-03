from collections import deque
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result  = []
        queue = deque()
        queue.append(root)
        while queue:
            current_length = len(queue)
            for i in range(current_length):
                current_node = queue.popleft()
                if i==current_length-1:
                    result.append(current_node.val)
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
        return result
