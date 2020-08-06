class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def allpathRToL(root:TreeNode,currentPath:list,allPaths:list):
    if root is None:
        return
    currentPath.append(root.val)
    if root.left is None and root.right is None:
        currentSum = sum(currentPath)
        maxSum=0
        if allPaths is not None and len(allPaths) >0:
            maxSum = sum(allPaths[0])
        if currentSum > maxSum:
            allPaths.clear()
            allPaths.append(list(currentPath))
    else:
        allpathRToL(root.left,currentPath,allPaths)
        allpathRToL(root.right,currentPath,allPaths)
    del currentPath[-1]


def find_paths(root, sum):
    allPaths = []
    allpathRToL(root,[],allPaths)
    return allPaths


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()