from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = deque()
    queue = deque()
    queue.append(root)
    while queue:
        current_length = len(queue)
        current_list = []
        for i in range(current_length):
            current_node = queue.popleft()
            current_list.append(current_node.val)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        result.append(current_list)
    result.reverse()
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
