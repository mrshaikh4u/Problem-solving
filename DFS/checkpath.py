class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkPathRec(root:TreeNode , sequence:list ,idx:int )->bool:
    if root is None or root.val!=sequence[idx]:
        return False
    if root.left is None and root.right is None:
        if idx == len(sequence)-1:
            return True
        return False
    return checkPathRec(root.left,sequence,idx+1) or checkPathRec(root.right , sequence , idx+1)

def find_path(root, sequence):
    return checkPathRec(root , sequence , 0)


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 1, 5])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()