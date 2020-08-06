class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumRec(root:TreeNode , cs ):
    if root is None:
        return 0
    cs = (cs*10) + root.val
    if root.left is None and root.right is None:
        return cs
    return sumRec(root.left , cs) + sumRec(root.right ,cs)

def find_sum_of_path_numbers(root):
    return sumRec(root,0)



def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()