import math




class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MaxSum:
    def __init__(self):
        self.sum = 0

def maxSumRec(root:TreeNode , maxSum:MaxSum)-> int:
    if root is None:
        return 0
    leftSum = maxSumRec(root.left , maxSum)
    rightSum = maxSumRec(root.right , maxSum)
    totalSum = leftSum + rightSum + root.val
    is_negative = False
    if totalSum<0:
        is_negative = True
    maxSum.sum = max(abs(maxSum.sum) , abs(totalSum),abs(root.val))
    if is_negative:
        maxSum.sum  = maxSum.sum - (maxSum.sum)*2
    return max(leftSum , rightSum) + root.val

def find_maximum_path_sum(root):
    maxSum = MaxSum()
    maxSumRec(root,maxSum)
    return maxSum.sum


def main():
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    #
    # print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(3)
    # root.right.left = TreeNode(5)
    # root.right.right = TreeNode(6)
    # root.right.left.left = TreeNode(7)
    # root.right.left.right = TreeNode(8)
    # root.right.right.left = TreeNode(9)
    # print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    #
    # root = TreeNode(-1)
    # root.left = TreeNode(-3)
    # print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    root = TreeNode(2)
    root.left = TreeNode(-1)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))


main()