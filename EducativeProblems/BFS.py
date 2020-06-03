from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    queue = deque()
    queue.append(root)
    while queue:
        current_length = len(queue)
        for i in range(current_length):
            current_element = queue.popleft()
            result.append(current_element.val)
            if current_element.left is not None:
                queue.append(current_element.left)
            if current_element.right is not None:
                queue.append(current_element.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()