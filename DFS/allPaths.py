class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getPathRec(root:TreeNode , currentPath:list , allpaths:list,sum):
    if root is None:
        return
    currentPath.append(root.val)
    if root.val == sum:
        if root.left is None and root.right is None:
            listToAdd = [i for i in currentPath]
            allpaths.append(listToAdd)
    else:
        getPathRec(root.left , currentPath , allpaths ,  sum - root.val)
        getPathRec(root.right , currentPath , allpaths , sum - root.val)
    del currentPath[-1]


def find_paths(root, sum):
    allPaths = []
    getPathRec(root,[],allPaths,sum)
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