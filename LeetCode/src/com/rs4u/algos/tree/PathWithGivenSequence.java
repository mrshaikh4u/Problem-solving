package com.rs4u.algos.tree;

public class PathWithGivenSequence {
	public static boolean findPath(TreeNode root, int[] sequence) {
		return findPathRec(root, 0, sequence);
	}

	private static boolean findPathRec(TreeNode root, int idx, int[] sequence) {
		if (root == null)
			return false;
		if (idx > sequence.length - 1) {
			return false;
		}
		if (root.val != sequence[idx])
			return false;

		if (idx == sequence.length - 1)
			return true;

		return findPathRec(root.left, idx + 1, sequence) || findPathRec(root.right, idx + 1, sequence);

	}

	public static void main(String[] args) {
		TreeNode root = new TreeNode(1);
		root.left = new TreeNode(0);
		root.right = new TreeNode(1);
		root.left.left = new TreeNode(1);
		root.right.left = new TreeNode(6);
		root.right.right = new TreeNode(5);

		System.out.println("Tree has path sequence: " + PathWithGivenSequence.findPath(root, new int[] { 1, 0, 1 }));
		System.out.println("Tree has path sequence: " + PathWithGivenSequence.findPath(root, new int[] { 1, 1, 5 }));
	}
}
