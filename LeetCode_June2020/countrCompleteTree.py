# Definition for a binary tree node.
from Utils import TreeUtils
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Counter:
    def __init__(self):
        self.cnt=0

class Solution:
    def coundRec(self,root:TreeNode,counter:Counter):
        if root is None:
            return
        counter.cnt+=1
        self.coundRec(root.left,counter)
        self.coundRec(root.right,counter)
    def countNodes(self, root: TreeNode) -> int:
        counter = Counter()
        counter.cnt=0
        self.coundRec(root,counter)
        return counter.cnt


obj = Solution()
tree = TreeUtils.prepareTree()
# TreeUtils.printTree(tree)
print(obj.countNodes(tree))