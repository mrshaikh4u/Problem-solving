package com.rs4u.algos;

import java.util.HashMap;
import java.util.Map.Entry;
import java.util.Set;

public class Palindrome {
	public static boolean canConstruct(String s, int k) {

		if (s == null)
			return false;
		if (s.length() == 1) {
			if (k == 1)
				return true;
			return false;
		}
		if (s.length() < k)
			return false;

		HashMap<Character, Integer> freqMap = new HashMap<Character, Integer>();

		for (char c : s.toCharArray()) {
			freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
		}
		if (k == freqMap.size())
			return true;
		Set<Entry<Character, Integer>> entrySet = freqMap.entrySet();
		int cntDefault = 0;
		for (Entry<Character, Integer> entry : entrySet) {
			if (entry.getValue() == k || entry.getValue() / 2 != k)
				continue;
			cntDefault++;
			if (cntDefault > 1)
				return false;
		}
		return true;
	}

	public static void main(String[] args) {
		System.out.println(canConstruct("leetcode", 3));
	}
}
