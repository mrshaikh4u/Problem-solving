package com.rs4u.algos;

import java.util.HashSet;

public class Twice {
	public static void main(String[] args) {

//		int i1 = 1;
//		int i2 = 2;
//		int item2 = i1 ^ i2;
//		System.out.println(item2);
//		item2 ^= i2;
//		System.out.println(item2);

//		
		int a[] = { 3, 2, 1, 5, 1, 2 };
		HashSet<Integer> hs = new HashSet<Integer>();
		for (int item : a) {
			if (!hs.add(item))
				hs.remove(item);
		}
		for (Integer integer : hs) {
			System.out.println(integer);
		}
//		for (int i = 0; i < a.length; i++) {
//			if (item1 == a[i])
//				continue;
//			a[0] ^= a[i];
//		}
//		System.out.println(a[0]);
	}
}
