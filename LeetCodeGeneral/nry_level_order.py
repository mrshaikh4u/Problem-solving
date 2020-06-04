# Definition for a Node.
from typing import List
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        output = []
        if not root:
            return output
        queue = deque()
        queue.append(root)
        while queue:
            current_length = len(queue)
            current_list = []
            for i in range(current_length):
                current_node = queue.popleft()
                current_list.append(current_node)
                for child in current_node.children:
                    queue.append(child)
            output.append(current_list)
        return output


