from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
    queue = deque()
    queue.append(root)
    while queue:
        current_length = len(queue)
        for i in range(current_length):
            current_node = queue.popleft()
            if i==current_length-1:
                current_node.next = None
            else:
                current_node.next = queue[0]
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
    return root

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()