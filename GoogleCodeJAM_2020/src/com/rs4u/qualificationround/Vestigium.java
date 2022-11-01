package com.rs4u.qualificationround;

import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class Vestigium {
	public static void main(String[] args) throws IOException {
//		Scanner infile = new Scanner(new File("input"));
		Scanner infile = new Scanner(System.in);
		int T = infile.nextInt();
		for (int tc = 0; tc < T; tc++) {
			int sumVal = 0;
			int numberOfRows = 0;
			int numberOfColums = 0;
			int N = infile.nextInt();
//			int[][] inputMatrix = new int[N][N];
			Map<Integer, Boolean> columnCounted = new HashMap<Integer, Boolean>();
			Map<Integer, HashSet<Integer>> columnSet = new HashMap<Integer, HashSet<Integer>>();
			for (int i = 0; i < N; i++) {
				Set<Integer> rowHS = new HashSet<Integer>();
				boolean rowCounted = false;
				for (int j = 0; j < N; j++) {
					if (!columnSet.containsKey(j)) {
						columnSet.put(j, new HashSet<Integer>());
						columnCounted.put(j, false);
					}
					int elementIxJ = infile.nextInt();
					if (rowHS.contains(elementIxJ)) {
						if (!rowCounted) {
							numberOfRows++;
							rowCounted = true;
						}
					} else {
						rowHS.add(elementIxJ);
					}
					if (i == j) {
						sumVal += elementIxJ;
					}
					// TODO remove
					// inputMatrix[i][j] = elementIxJ;
					if (columnSet.get(j)
					             .contains(elementIxJ)) {
						if (!columnCounted.get(j)) {
							numberOfColums++;
							columnCounted.put(j, true);
						}
					} else {
						columnSet.get(j)
						         .add(elementIxJ);
					}
				}
			}
//			printInput(tc, inputMatrix);
			System.out.println("Case #" + (tc + 1) + ": " + sumVal + " " + numberOfRows + " " + numberOfColums);
		}

	}

	private static void printInput(int t, int[][] inputMatrix) {

		System.out.println("Input for test case : " + (t + 1));
		for (int[] is : inputMatrix) {
			for (int element : is) {
				System.out.print(element + " ");
			}
			System.out.print("\n");
		}
	}
}
