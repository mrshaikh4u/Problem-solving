package com.rs4u.algos.recursions;

public class Fib {

	private static int fib(int n, int prev, int curr) {
		if (n <= 0)
			return prev + curr;
		return fib(--n, curr, prev + curr);

	}

	public static void main(String[] args) {
		int prev = 0;
		int current = 1;
		int n = 1;
		System.out.println(fib(n - 2, prev, current));
	}
}
