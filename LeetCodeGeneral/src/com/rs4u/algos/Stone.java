package com.rs4u.algos;

import java.util.PriorityQueue;

public class Stone {
	public int lastStoneWeight(int[] stones) {

		if (stones == null || stones.length == 0)
			return 0;
		PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>((a, b) -> b - a);
		for (int stone : stones) {
			maxHeap.offer(stone);
		}

		while (maxHeap.size() > 1) {
			int stoneY = maxHeap.poll();
			int stoneX = maxHeap.poll();
			maxHeap.offer(Math.abs(stoneY - stoneX));
		}
		return maxHeap.peek();
	}

	public static void main(String[] args) {

		int arr[] = { 2, 3, 1 };
		System.out.println(new Stone().lastStoneWeight(arr));
	}
}
