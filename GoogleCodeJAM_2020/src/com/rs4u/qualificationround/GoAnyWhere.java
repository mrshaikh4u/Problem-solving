package com.rs4u.qualificationround;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Position {
	int r;
	int c;

	public Position(int row, int column) {
		this.r = row;
		this.c = column;

	}

	@Override
	public boolean equals(Object obj) {
		if (obj instanceof Position) {
			Position pos = (Position) obj;
			return pos.c == this.c && pos.r == this.r;
		}
		return false;
	}
}

public class GoAnyWhere {

	public static void main(String[] args) throws IOException {
//		Scanner infile = new Scanner(new File("input"));
		Scanner infile = new Scanner(System.in);
		int T = infile.nextInt();
		for (int i = 0; i < T; i++) {
			int N = infile.nextInt();
			String P = infile.next();
			List<Position> inputPositions = new ArrayList<Position>();
			int r = 0;
			int c = 0;
			for (int j = 0; i < P.length(); i++) {
				if (P.charAt(j) == 'S') {
					r++;
				} else {
					c++;
				}
				inputPositions.add(j, new Position(r, c));
			}
			char arr[] = new char[P.length()];
			c = 0;
			r = 0;
			int k = 0;
			while (k < arr.length) {
				char toTake;
				if (k == 0) {
					toTake = 'S' == P.charAt(k) ? 'E' : 'S';
				} else {
					Position p = new Position(r, c);

				}

			}
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
