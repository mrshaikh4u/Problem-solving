# Definition for a binary tree node.
from collections import deque
from Utils import TreeUtils
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        output = deque()
        output.append(root)
        fm = 1
        while output:
            current_len = len(output)
            start = -1
            cm = 0
            for i in range(current_len):
                cN = output.popleft()
                if cN is not None:
                    if start ==-1:
                        start = i
                    else:
                        cm = (i - start) + 1
                    output.append(cN.left)
                    output.append(cN.right)
            fm = max(fm,cm)
        return fm

obj = Solution()
root1 = TreeUtils.prepareTree()
print("input : ")
TreeUtils.printTree(root1)
print('output : ',obj.widthOfBinaryTree(root1))



root2 = TreeUtils.prepareTree_2()
print("input : ")
TreeUtils.printTree(root2)
print('output : ',obj.widthOfBinaryTree(root2))




