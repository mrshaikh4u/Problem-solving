from collections import deque
import sys
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    queue = deque()
    queue.append(root)
    maxDepth = -1
    current_height = 0
    while queue:
        current_height+=1
        current_length = len(queue)
        for i in range(current_length):
            current_node = queue.popleft()
            if current_node.left is None and current_node.right is None:
                maxDepth = max(maxDepth,current_height)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
    return maxDepth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()