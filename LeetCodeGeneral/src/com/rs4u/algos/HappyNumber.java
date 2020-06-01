package com.rs4u.algos;

/**
 * 
 * Problem statement : Write an algorithm to determine if a number is "happy".
 * 
 * A happy number is a number defined by the following process: Starting with
 * any positive integer, replace the number by the sum of the squares of its
 * digits, and repeat the process until the number equals 1 (where it will
 * stay), or it loops endlessly in a cycle which does not include 1. Those
 * numbers for which this process ends in 1 are happy numbers.
 * 
 * @author Rahil
 *
 */
public class HappyNumber {

	private static int getSquare(int number) {
		if (number < 0)
			return 0;
		if (number < 10)
			return number * number;
		int square = 0;
		while (number >= 10) {
			int temp = number % 10;
			square += (temp * temp);
			number /= 10;
		}
		if (number > 0)
			square += number * number;
		return square;
	}

	private static boolean isHappy(int n) {
		if (n == 1)
			return true;
		if (n < 1)
			return false;
		int slow = n;
		int fast = n;
		do {
			slow = getSquare(slow);
			fast = getSquare(getSquare(fast));
		} while (slow != fast);
		return slow == 1;
	}

	public static void main(String[] args) {
		System.out.println("isHappy : " + isHappy(19));
	}
}
