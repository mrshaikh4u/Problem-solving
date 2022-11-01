package com.rs4u.algos;

import java.util.HashSet;
import java.util.Set;

/**
 * A robot is located at the top-left corner of a m x n grid (marked 'Start' in
 * the diagram below).
 * 
 * The robot can only move either down or right at any point in time. The robot
 * is trying to reach the bottom-right corner of the grid (marked 'Finish' in
 * the diagram below).
 * 
 * @author Rahil
 *
 */
class Point {
	private int row;
	private int col;

	@Override
	public boolean equals(Object obj) {
		if (obj instanceof Point) {
			Point p = (Point) obj;
			return p.col == this.col && p.row == this.row;
		}
		return false;
	}

	@Override
	public int hashCode() {
		return 4 * (this.row + this.col);
	}

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

class Output {
	private int result;

	public int getResult() {
		return result;
	}

	public void setResult(int result) {
		this.result = result;
	}

}

public class UniquePaths {

	public static void main(String[] args) {

		int m = 7;
		int n = 3;

		int row = n;
		int col = m;

		Set<Point> failedPath = new HashSet<Point>();
		Output output = new Output();
		if (hasPath(row, col, failedPath, output)) {
			System.out.println(output.getResult());
		}

	}

	private static boolean hasPath(int row, int col, Set<Point> failedPath, Output output) {

		if (row < 0 || col < 0)
			return false;

		boolean isOrigin = (row == 0) && (col == 0);
		Point p = new Point(row, col);
		boolean found = false;
		if (failedPath.contains(p)) {
			return false;
		}

		if (isOrigin) {
			output.setResult(output.getResult() + 1);
			found = true;
		}

		if (hasPath(row - 1, col, failedPath, output)) {
			output.setResult(output.getResult() + 1);
			found = true;
		}
		if (hasPath(row, col - 1, failedPath, output)) {
			output.setResult(output.getResult() + 1);
			found = true;
		}
		failedPath.add(p);
		return found;
	}

}
