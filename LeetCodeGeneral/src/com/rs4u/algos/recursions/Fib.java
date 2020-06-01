package com.rs4u.algos.recursions;

public class Fib {

	static int fib(int i, int[] mem) {
		if (i == 0)
			return 0;
		if (i == 1)
			return 1;
		if (mem[i] == 0) {
			mem[i] = fib(i - 1, mem) + fib(i - 2, mem);
		}
		return mem[i];
	}

	public static void main(String[] args) {
		int i = 6;
		int[] mem = new int[i + 1];
		System.out.println(fib(i, mem));
	}
}
