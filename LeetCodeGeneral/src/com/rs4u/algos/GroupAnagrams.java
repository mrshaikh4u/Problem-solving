package com.rs4u.algos;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * Problem statement : Given an array of strings, group anagrams together.
 * 
 * Example:
 * 
 * Input: ["eat", "tea", "tan", "ate", "nat", "bat"], Output: [
 * ["ate","eat","tea"], ["nat","tan"], ["bat"] ] Note:
 * 
 * All inputs will be in lowercase. The order of your output does not matter.
 * 
 * @author Rahil
 *
 */
public class GroupAnagrams {
	public List<List<String>> groupAnagrams(String[] strs) {
		List<List<String>> output = new ArrayList();
		if (strs == null || strs.length == 0)
			return output;
		HashMap<String, List<Integer>> positionMap = new HashMap<String, List<Integer>>();
		for (int i = 0; i < strs.length; i++) {
			char[] charArray = strs[i].toCharArray();
			Arrays.sort(charArray);
			String str = String.valueOf(charArray);
			List<Integer> list = positionMap.getOrDefault(str, new ArrayList<Integer>());
			list.add(i);
			positionMap.put(str, list);
		}
		output = prepareOutput(strs, positionMap);

		return output;
	}

	private List<List<String>> prepareOutput(String[] input, HashMap<String, List<Integer>> positionMap) {

		Set<Entry<String, List<Integer>>> entrySet = positionMap.entrySet();
		List<List<String>> output = new ArrayList();
		for (Entry<String, List<Integer>> entry : entrySet) {
			List<String> list = entry.getValue()
			                         .stream()
			                         .map(e -> input[e])
			                         .collect(Collectors.toList());
			output.add(list);
		}
		return output;
	}

	public static void main(String[] args) {
		String[] input = { "duh", "ill" };
		List<List<String>> groupAnagrams = new GroupAnagrams().groupAnagrams(input);
	}
}
