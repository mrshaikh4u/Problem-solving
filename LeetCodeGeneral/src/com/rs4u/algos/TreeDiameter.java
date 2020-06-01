package com.rs4u.algos;

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode(int x) {
		val = x;
	}
};

public class TreeDiameter {

	private static int diameterGlobal = 0;

	public int diameterOfBinaryTree(TreeNode root) {
		calculateHightRec(root);
		return diameterGlobal - 1;
	}

	private int calculateHightRec(TreeNode root) {
		if (root == null)
			return 0;
		int leftHeight = calculateHightRec(root.left);
		int rightHeight = calculateHightRec(root.right);
		int diameter = leftHeight + rightHeight + 1;
		diameterGlobal = Math.max(diameterGlobal, diameter);
		return Math.max(leftHeight, rightHeight) + 1;
	}

	public static void main(String[] args) {
		TreeNode root = new TreeNode(1);
		root.left = new TreeNode(2);
		root.right = new TreeNode(3);
		root.left.left = new TreeNode(4);
		root.right.left = new TreeNode(5);
		root.right.right = new TreeNode(6);
		System.out.println("Tree Diameter: " + new TreeDiameter().diameterOfBinaryTree(root));
		root.left.left = null;
		root.right.left.left = new TreeNode(7);
		root.right.left.right = new TreeNode(8);
		root.right.right.left = new TreeNode(9);
		root.right.left.right.left = new TreeNode(10);
		root.right.right.left.left = new TreeNode(11);
		System.out.println("Tree Diameter: " + new TreeDiameter().diameterOfBinaryTree(root));
	}
}
