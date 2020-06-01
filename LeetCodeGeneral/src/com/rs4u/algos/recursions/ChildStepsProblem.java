package com.rs4u.algos.recursions;

import java.util.Arrays;

/**
 * Problem statement: Triple Step: A child is running up a staircase with n
 * steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a
 * method to count how many possible ways the child can run up the stairs.
 * 
 * @author Rahil
 *
 */
public class ChildStepsProblem {

	static long steps(int i, long[] mem) {
		if (i < 0) {
			return 0;
		} else if (i == 0) {
			return 1;
		}
		if (mem[i] == -1) {
			mem[i] = steps(i - 1, mem) + steps(i - 2, mem);
		}
		return mem[i];
	}

	public static void main(String[] args) {
		int i = 3;
		long mem[] = new long[i + 1];
		Arrays.fill(mem, -1);
		System.out.println(steps(i, mem));
	}
}
