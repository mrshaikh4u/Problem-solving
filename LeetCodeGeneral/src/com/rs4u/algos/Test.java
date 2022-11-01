package com.rs4u.algos;

import java.util.Arrays;

public class Test {
	public static void main(String[] args) {
		String str = "bca";
		String str2 = "cba";
		char[] charArray = str.toCharArray();
		char[] charArray2 = str2.toCharArray();
		Arrays.sort(charArray);
		Arrays.sort(charArray2);
		System.out.println(new String(charArray).equals(new String(charArray2)));
	}
}
