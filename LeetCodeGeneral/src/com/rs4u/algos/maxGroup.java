package com.rs4u.algos;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.PriorityQueue;

public class maxGroup {

	public static int countLargestGroup(int n) {
		Map<Integer, Integer> numFrequencyMap = new HashMap<>();

		for (int i = 1; i <= n; i++) {
			int grpSum = findSum(i);
			numFrequencyMap.put(grpSum, numFrequencyMap.getOrDefault(grpSum, 0) + 1);
		}
		PriorityQueue<Map.Entry<Integer, Integer>> minHeap = new PriorityQueue<Map.Entry<Integer, Integer>>(
		        (e1, e2) -> e2.getValue() - e1.getValue());

		for (Map.Entry<Integer, Integer> entry : numFrequencyMap.entrySet()) {
			minHeap.offer(entry);
		}
		Integer value = minHeap.peek()
		                       .getValue();
		int cnt = 0;
		for (Entry<Integer, Integer> entry : minHeap) {
			if (entry.getValue()
			         .intValue() == value.intValue())
				cnt++;
		}
		return cnt;
	}

	private static int findSum(int i) {
		int sum = 0;
		while (i >= 10) {
			sum += i % 10;
			i /= 10;
		}
		sum += i;
		return sum;
	}

	public static void main(String[] args) {

		System.out.println(countLargestGroup(1786));
	}
}
