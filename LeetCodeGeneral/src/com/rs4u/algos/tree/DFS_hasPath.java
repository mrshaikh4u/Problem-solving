package com.rs4u.algos.tree;

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode(int x) {
		val = x;
	}
};

class DFS_hasPath {

	private static boolean hasPathRec(TreeNode root, int sum) {

		if (root == null) {
			return false;
		}
		if (root.left == null && root.right == null) {
			return sum == root.val;
		}
		return hasPathRec(root.left, sum - root.val) || hasPathRec(root.right, sum - root.val);

	}

	public static boolean hasPath(TreeNode root, int sum) {
		return hasPathRec(root, sum);
	}

	public static void main(String[] args) {
		TreeNode root = new TreeNode(1);
		root.left = new TreeNode(2);
		root.right = new TreeNode(3);
		root.left.left = new TreeNode(4);
		root.left.right = new TreeNode(5);
		root.right.left = new TreeNode(6);
		root.right.right = new TreeNode(7);
		System.out.println("Tree has path: " + DFS_hasPath.hasPath(root, 10));
		System.out.println("Tree has path: " + DFS_hasPath.hasPath(root, 16));
	}
}
