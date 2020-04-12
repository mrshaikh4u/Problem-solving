package com.rs4u.algos.tree;

import java.util.ArrayList;
import java.util.List;

class AllTreePath {
	public static List<List<Integer>> findPaths(TreeNode root, int sum) {
		List<List<Integer>> allPaths = new ArrayList<>();

		List<Integer> currentList = new ArrayList<Integer>();
		findPathRec(root, sum, allPaths, currentList);

		// TODO: Write your code here
		return allPaths;
	}

	private static void findPathRec(TreeNode root, int sum, List<List<Integer>> allPaths, List<Integer> currentList) {
		if (root == null)
			return;
		if (root.left == null && root.right == null) {
			if (root.val == sum) {
				currentList.add(root.val);
				allPaths.add(currentList);
				return;
			} else {
				return;
			}
		}
		currentList.add(root.val);
		findPathRec(root.left, sum - root.val, allPaths, currentList);
		currentList = new ArrayList<Integer>();
		currentList.add(root.val);
		findPathRec(root.right, sum - root.val, allPaths, currentList);

	}

	public static void main(String[] args) {
		TreeNode root = new TreeNode(12);
		root.left = new TreeNode(7);
		root.right = new TreeNode(1);
		root.left.left = new TreeNode(4);
		root.right.left = new TreeNode(10);
		root.right.right = new TreeNode(5);
		int sum = 23;
		List<List<Integer>> result = AllTreePath.findPaths(root, sum);
		System.out.println("Tree paths with sum " + sum + ": " + result);
	}
}
