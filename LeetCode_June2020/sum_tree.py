# Definition for a binary tree node.
from Utils import TreeUtils
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Sum:
    def __init__(self):
        self.total = 0

class Solution:

    def findSumRec(self,root:TreeNode,result:Sum,currentSum:int):
        if root is None:
            return
        currentSum = currentSum*10+root.val
        if root.left is None and root.right is None:
            result.total += currentSum
        else:
            self.findSumRec(root.left , result , currentSum)
            self.findSumRec(root.right,result , currentSum)
        currentSum = currentSum-root.val



    def sumNumbers(self, root: TreeNode) -> int:
        result = Sum()
        result.total = 0
        self.findSumRec(root,result,0)
        return result.total


obj = Solution()
tree = TreeUtils.prepareTree()
TreeUtils.printTree(tree)
print(obj.sumNumbers(tree))
