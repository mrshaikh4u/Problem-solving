package com.rs4u.qualificationround;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class SolutionBK {
	public static void main(String[] args) throws IOException {
		Scanner infile = new Scanner(new File("input"));
//		Scanner infile = new Scanner(System.in);
		int T = infile.nextInt();
		for (int i = 0; i < T; i++) {
			String inputStr = infile.next();
			int N = infile.nextInt();
			int num2 = calculate(N);
			System.out.println("Case #" + (i + 1) + ": " + (N - num2) + " " + num2);
		}
	}

	private static int calculate(int n) {
		int num2 = 0;
		int multiplier = 1;
		int digit = 0;
		while (n >= 10) {
			digit = n % 10;
			if (digit == 4) {
				digit = 3;
			}
			num2 += digit * multiplier;
			n /= 10;
			multiplier *= 10;
		}
		if (n == 4) {
			digit = 3;
		}
		num2 += digit * multiplier;
		return num2;
	}
}
