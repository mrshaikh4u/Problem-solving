package com.rs4u.algos;

import java.util.HashSet;
import java.util.Optional;
import java.util.Set;

/**
 * 
 * Problem statement : Given a non-empty array of integers, every element
 * appears twice except for one. Find that single one.
 * 
 * Note:
 * 
 * Your algorithm should have a linear runtime complexity. Could you implement
 * it without using extra memory?
 * 
 * @author Rahil
 *
 */
public class SingleNumber {
	public int singleNumber(int[] nums) {
		Set<Integer> hs = new HashSet<Integer>();
		for (int i : nums) {
			if (hs.contains(i))
				hs.remove(i);
			else {
				hs.add(i);
			}
		}
		Optional<Integer> optional = hs.stream()
		                               .findFirst();
		if (optional.isPresent())
			return optional.get();
		return Integer.MIN_VALUE;
	}

	public static void main(String[] args) {
		int[] arr = { 4, 1, 2, 1, 2 };
		System.out.println(new SingleNumber().singleNumber(arr));
	}
}
