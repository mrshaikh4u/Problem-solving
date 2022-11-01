class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathRec(root,sum):
    if root is None:
        return False
    if root.left is None and root.right is None:
        if root.val == sum:
            return True
        return False
    return hasPathRec(root.left,sum - root.val) or hasPathRec(root.right ,sum-root.val)



def has_path(root, sum):
    return hasPathRec(root,sum)

def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()