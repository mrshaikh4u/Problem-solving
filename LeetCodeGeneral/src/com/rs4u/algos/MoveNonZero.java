package com.rs4u.algos;

import java.util.Arrays;

/**
 * Problem statement : Given an array nums, write a function to move all 0's to
 * the end of it while maintaining the relative order of the non-zero elements.
 * 
 * Example:
 * 
 * Input: [0,1,0,3,12] Output: [1,3,12,0,0]
 * 
 * @author Rahil
 *
 */
public class MoveNonZero {

	public static void moveZeroes(int[] nums) {
		if (nums == null || nums.length == 0)
			return;
		int slow = 0;
		int fast = 0;
		while (fast < nums.length) {
			if (nums[fast] != 0) {
				int temp = nums[slow];
				nums[slow] = nums[fast];
				nums[fast] = temp;
				slow++;
			}
			fast++;
		}
	}

	public static void main(String[] args) {
		int[] arr = { 0, 1, 1, 1, 0 };
		moveZeroes(arr);
		Arrays.stream(arr)
		      .forEach(System.out::print);
	}
}
