class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathForSumMidRec(root:TreeNode ,allPaths:list ,currentPath:list , S:int):
    if root is None:
        return
    currentPath.append(root.val)
    cs = 0
    for i in range(len(currentPath)-1 , -1,-1):
        cs+=currentPath[i]
        if cs==S:
            allPaths.append(list(currentPath[i:]))
            break
    pathForSumMidRec(root.left ,allPaths,currentPath,S)
    pathForSumMidRec(root.right,allPaths,currentPath,S)
    del currentPath[-1]


def count_paths(root, S):
    allpaths = []
    pathForSumMidRec(root,allpaths,[],S)
    return allpaths



def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()