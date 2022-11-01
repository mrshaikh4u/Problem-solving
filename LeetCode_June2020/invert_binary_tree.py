# Definition for a binary tree node.
from Utils import TreeUtils
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertRec(self,root:TreeNode)->TreeNode:
        if not root or (not root.left and not root.right):
            return root
        self.invertRec(root.left)
        self.invertRec(root.right)
        root.left , root.right = root.right , root.left
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.invertRec(root)

root = TreeUtils.prepareTree()
TreeUtils.printTreeInOrder(root)
obj = Solution()
new_root = obj.invertTree(root)
print('output : ')
TreeUtils.printTreeInOrder(new_root)


