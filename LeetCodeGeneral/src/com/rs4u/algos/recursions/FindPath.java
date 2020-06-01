package com.rs4u.algos.recursions;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Point {
	private int row;
	private int col;

	public Point(int row, int col) {
		super();
		this.row = row;
		this.col = col;
	}

	public int getRow() {
		return row;
	}

	public void setRow(int row) {
		this.row = row;
	}

	public int getCol() {
		return col;
	}

	public void setCol(int col) {
		this.col = col;
	}

}

/**
 * Problem statement : Robot in a Grid: Imagine a robot sitting on the upper
 * left corner of grid with r rows and c columns. The robot can only move in two
 * directions, right and down, but certain cells are "off limits" such that the
 * robot cannot step on them. Design an algorithm to find a path for the robot
 * from the top left to the bottom right.
 * 
 * @author Rahil
 *
 */
public class FindPath {

	public static void main(String[] args) {

		int[][] arr = new int[4][5];
		Set<Point> failedPath = new HashSet<Point>();
		List<Point> path = new ArrayList<Point>();
		if (hasPath(arr.length, arr[0].length, arr, failedPath, path)) {
			// TODO return path;
			System.out.println("path present");
		}
	}

	private static boolean hasPath(int row, int col, int[][] arr, Set<Point> failedPath, List<Point> path) {
		if (row < 0 || col < 0)
			return false;
		boolean isOrigin = row == 0 && col == 0;

		Point p = new Point(row, col);

		if (failedPath.contains(p))
			return false;

		if (isOrigin || hasPath(row - 1, col, arr, failedPath, path) || hasPath(row, col - 1, arr, failedPath, path)) {
			path.add(new Point(row, col));
			return true;
		}
		failedPath.add(new Point(row, col));
		return false;

	}

}
