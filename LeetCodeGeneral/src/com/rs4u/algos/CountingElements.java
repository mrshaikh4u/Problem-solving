package com.rs4u.algos;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

/**
 * Problem statement :
 * 
 * Given an integer array arr, count element x such that x + 1 is also in arr.
 * 
 * If there're duplicates in arr, count them seperately. Example 1:
 * 
 * Input: arr = [1,2,3] Output: 2 Explanation: 1 and 2 are counted cause 2 and 3
 * are in arr.
 * 
 * @author Rahil
 *
 */
public class CountingElements {

	public int countElements(int[] arr) {
		int cnt = 0;
		if (arr == null || arr.length == 0)
			return cnt;
		HashMap<Integer, Integer> requirement = new HashMap<Integer, Integer>();
		Set<Integer> existance = new HashSet<Integer>();
		for (Integer element : arr) {
			if (existance.contains(element + 1)) {
				cnt++;
			} else {
				requirement.put(element + 1, requirement.getOrDefault(element + 1, 0) + 1);
			}
			if (requirement.containsKey(element)) {
				cnt += requirement.get(element);
				requirement.remove(element);
			}
			existance.add(element);
		}
		return cnt;
	}

	public static void main(String[] args) {
		int[] arr = { 2, 2, 1 };
		int cnt = new CountingElements().countElements(arr);
		System.out.println(cnt);

	}
}
