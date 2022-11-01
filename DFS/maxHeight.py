class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:

    def __init__(self):
        self.treeDiameter = 0

    def pathSum(self,root:TreeNode , ch:int , maxHeight:int):
        if root is None:
            return 0
        ch+=1
        if root.left is None and root.right is None:
            return ch
        leftHeight = self.pathSum(root.left,ch,maxHeight)
        rightHeight = self.pathSum(root.right , ch,maxHeight)
        self.treeDiameter = max(self.treeDiameter , leftHeight+rightHeight)
        return self.treeDiameter

    def find_diameter(self, root):
        return self.pathSum(root,0,0)

def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()






