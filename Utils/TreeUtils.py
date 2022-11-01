class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def prepareTree() -> TreeNode :
    #setting root
    root = TreeNode(4)
    root_left = TreeNode(2)
    root_right = TreeNode(7)
    root.left = root_left
    root.right = root_right

    #setting root left
    root_left_left = TreeNode(1)
    root_left_right = TreeNode(3)
    root_left.left = root_left_left
    root_left.right = root_left_right

    #setting root right
    root_right_left = TreeNode(6)
    root_right_right = TreeNode(9)
    root_right.left = root_right_left
    root_right.right = root_right_right
    return root

def printTreeInOrder(root : TreeNode):
    if not root:
        return
    printTreeInOrder(root.left)
    print(root.val , end=' ')
    printTreeInOrder(root.right)

def printTree(root:TreeNode):
    printTreeInOrder(root)