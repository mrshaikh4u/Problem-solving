package com.rs4u.algos;

import java.util.HashSet;
import java.util.Set;

/**
 * Problem statement : Given a string, find the length of the longest substring
 * without repeating characters.
 * 
 * @author Rahil
 *
 */
public class LongestSubstr {
	public int lengthOfLongestSubstring(String s) {
		if (s == null || s.length() == 0) {
			return 0;
		}
		int maxLen = Integer.MIN_VALUE;
		int ws = 0;
		Set<Character> charSet = new HashSet<Character>();
		for (int we = 0; we < s.length(); we++) {
			while (charSet.contains(s.charAt(we))) {
				charSet.remove(s.charAt(ws++));
			}
			charSet.add(s.charAt(we));
			maxLen = Math.max(maxLen, (we - ws) + 1);
		}
		return maxLen;
	}

	public static void main(String[] args) {
		System.out.println(new LongestSubstr().lengthOfLongestSubstring("abcdef"));
	}
}
