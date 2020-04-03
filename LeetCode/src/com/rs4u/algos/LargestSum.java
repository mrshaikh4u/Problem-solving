package com.rs4u.algos;

/**
 * Problem statement : Given an integer array nums, find the contiguous subarray
 * (containing at least one number) which has the largest sum and return its
 * sum.
 * 
 * 
 * @author Rahil
 *
 */
public class LargestSum {

	public static int maxSubArray(int[] nums) {
		if (nums == null || nums.length == 0) {
			return 0;
		}
		if (nums.length == 1)
			return nums[0];
		int currentSum = nums[0];
		int currentMax = nums[0];
		for (int i = 1; i < nums.length; i++) {
			currentSum = Math.max(currentSum + nums[i], nums[i]);
			currentMax = Math.max(currentMax, currentSum);
		}
		return currentMax;
	}

	public static void main(String[] args) {
		int nums[] = { -2, -1 };
		System.out.println(maxSubArray(nums));
	}
}
