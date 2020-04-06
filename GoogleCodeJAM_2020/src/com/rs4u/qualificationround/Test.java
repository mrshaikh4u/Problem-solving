package com.rs4u.qualificationround;

import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

public class Test {
	public static void main(String[] args) {
		char[] charArr = { 'H', 'E', 'E', 'L' };
		System.out.println(new String(charArr).equals("HEEL"));
		List<Integer> firstList = new LinkedList<Integer>();
		firstList.add(10);
		firstList.add(20);
		System.out.println("Before copy list 1");
		firstList.forEach(System.out::print);
		List<Integer> list2 = firstList.stream()
		                               .collect(Collectors.toCollection(LinkedList::new));

		System.out.println("List 2 : ");
		list2.forEach(System.out::print);
		list2.remove(0);
		System.out.println("List 2 : ");
		list2.forEach(System.out::print);

		System.out.println("afer delet list 1");
		firstList.forEach(System.out::print);

	}
}
