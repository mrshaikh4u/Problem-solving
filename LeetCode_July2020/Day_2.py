# Definition for a binary tree node.
from typing import List
from Utils import TreeUtils
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        output = [[root.val]]
        queue = deque()
        queue.append(root)
        while queue:
            current_length = len(queue)
            new_list = []
            for i in range(current_length):
                current_item = queue.popleft()
                if current_item.left is not None:
                    new_list.append(current_item.left.val)
                    queue.append(current_item.left)
                if current_item.right is not None:
                    new_list.append(current_item.right.val)
                    queue.append(current_item.right)
            if len(new_list) > 0:
                output.append(new_list)
        output.reverse()
        return output


obj = Solution()
new_tree = TreeUtils.prepareTree()
TreeUtils.printTree(new_tree)
print(obj.levelOrderBottom(new_tree))