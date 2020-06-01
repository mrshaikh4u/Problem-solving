package com.rs4u.algos;

import java.util.PriorityQueue;

/**
 * 
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * 
 * Find the median of the two sorted arrays. The overall run time complexity
 * should be O(log (m+n)).
 * 
 * You may assume nums1 and nums2 cannot be both empty.
 * 
 * @author Rahil
 *
 */
public class MedianOfTwoList {

	private static boolean isEmpty(int[] list) {
		return list == null || list.length == 0;
	}

	private static double findMedian(int[] nums1, int[] nums2) {

		if (isEmpty(nums1) && isEmpty(nums2)) {
			return 0;
		}

		PriorityQueue<Double> maxHeap = new PriorityQueue<Double>((a, b) -> Double.compare(b, a));
		PriorityQueue<Double> minHeap = new PriorityQueue<Double>((a, b) -> Double.compare(a, b));

		for (double item : nums1) {
			if (maxHeap.size() == 0 || item < maxHeap.peek()) {
				maxHeap.add(item);
			} else {
				minHeap.add(item);
			}

			if (maxHeap.size() > minHeap.size() + 1) {
				minHeap.add(maxHeap.poll());
			} else if (maxHeap.size() < minHeap.size()) {
				maxHeap.add(minHeap.poll());
			}

		}
		for (double item : nums2) {
			if (maxHeap.size() == 0 || item < maxHeap.peek()) {
				maxHeap.add(item);
			} else {
				minHeap.add(item);
			}

			if (maxHeap.size() > minHeap.size() + 1) {
				minHeap.add(maxHeap.poll());
			} else if (maxHeap.size() < minHeap.size()) {
				maxHeap.add(minHeap.poll());
			}

		}

		if (maxHeap.size() > minHeap.size())
			return maxHeap.peek();
		else
			return (maxHeap.peek() + minHeap.peek()) / 2;
	}

	public static void main(String[] args) {
		int[] arr1 = {};
		int[] arr2 = { 1, 2, 3, 4, 5, 6 };
		System.out.println(findMedian(arr1, arr2));
	}

}
