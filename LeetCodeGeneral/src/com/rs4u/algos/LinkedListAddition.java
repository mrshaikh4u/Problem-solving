package com.rs4u.algos;

class ListNode {
	int val;
	ListNode next;

	ListNode(int x) {
		val = x;
	}

	public ListNode insert(int data) {
		ListNode newNode = new ListNode(data);
		newNode.next = this;
		return newNode;
	}
}

/**
 * Problem statement :
 * 
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order and each of their nodes
 * contain a single digit. Add the two numbers and return it as a linked list.
 * 
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 * 
 * Example:
 * 
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) Output: 7 -> 0 -> 8 Explanation: 342 +
 * 465 = 807.
 * 
 * @author Rahil
 *
 */
public class LinkedListAddition {

	public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		ListNode temp = l1;
		int carry = 0;
		ListNode prev = null;
		while (l2 != null && l1 != null) {
			int val = (l1.val + l2.val + carry) % 10;
			carry = (l1.val + l2.val + carry) / 10;
			l1.val = val;
			l2 = l2.next;
			prev = l1;
			l1 = l1.next;
		}
		if (l1 == null)
			prev.next = l2;
		while (l2 != null) {
			int val = (l2.val + carry) % 10;
			carry = (l2.val + carry) / 10;
			l2.val = val;
			prev = l2;
			l2 = l2.next;
		}
		while (l1 != null) {
			int val = (l1.val + carry) % 10;
			carry = (l1.val + carry) / 10;
			l1.val = val;
			prev = l1;
			l1 = l1.next;
		}
		if (carry != 0) {
			ListNode newNode = new ListNode(carry);
			prev.next = newNode;
		}

		return temp;
	}

//(2 -> 4 -> 3) + (5 -> 6 -> 4)
	// 9 , 199 - > 208
	// 0,0

	public static void main(String[] args) {
		// 987 + 12 = 789 + 21=> 810 -> 018
		ListNode head1 = new ListNode(0);
//		head1 = head1.insert(4);
//		head1 = head1.insert(2);

		ListNode head2 = new ListNode(1);
//		head2 = head2.insert(6);
//		head2 = head2.insert(5);

		ListNode output = addTwoNumbers(head1, head2);
		// ListNode toReturn = reverseList(output);
		System.out.println(output);
	}

	private static ListNode reverseList(ListNode output) {
		ListNode prev = null;
		while (output != null) {
			ListNode next = output.next;
			output.next = prev;
			prev = output;
			output = next;
		}
		return prev;
	}

}
