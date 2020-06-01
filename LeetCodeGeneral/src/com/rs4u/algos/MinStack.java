package com.rs4u.algos;

import java.util.Stack;

class Item {
	public Item(int x) {
		this.val = x;
	}

	int val;
	int nextMin;
}

public class MinStack {
	private Stack<Item> myStack;
	private int minElement;

	public MinStack() {
		myStack = new Stack<Item>();
		minElement = Integer.MAX_VALUE;
	}

	public void push(int x) {
		Item item = new Item(x);
		if (item.val <= minElement) {
			item.nextMin = minElement;
			minElement = item.val;
		}
		myStack.push(item);
	}

	public void pop() {
		Item removedItem = myStack.pop();
		if (removedItem.val == minElement) {
			minElement = removedItem.nextMin;
		}
	}

	public int top() {
		return myStack.peek().val;
	}

	public int getMin() {
		return this.minElement;
	}

	public static void main(String[] args) {
		MinStack minStack = new MinStack();
		minStack.push(512);
		minStack.push(-1024);
		minStack.push(512);
		minStack.push(-1024);
		minStack.pop();
		System.out.println(minStack.getMin()); // --> Returns -3.
		minStack.pop();
		System.out.println(minStack.getMin());
		minStack.pop();
		System.out.println(minStack.getMin());// --> Returns 0.
//		System.out.println(minStack.getMin()); // --> Returns -2.
	}

}
