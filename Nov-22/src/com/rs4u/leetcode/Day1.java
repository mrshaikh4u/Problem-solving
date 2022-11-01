package com.rs4u.leetcode;

import java.util.Arrays;

class Day1 {
    public int[] findBall(int[][] grid) {
        if(grid == null)
            return null;
        int [] result = new int[grid[0].length];
        for (int i = 0; i < grid[0].length; i++) {
            result[i] = findBallRec(i,grid,0);
        }
        return result;
    }

    public int findBallRec(int pos,int [][]grid,int rowNum){
        if( pos < 0 ||
                pos > grid[rowNum].length-1 ||
                (pos == 0 && grid[rowNum][pos] == -1) ||
                ( pos == grid[rowNum].length - 1 && grid[rowNum][pos] == 1) ||
                ( grid[rowNum][pos] == 1 &&  grid[rowNum][pos] != grid[rowNum][pos+1]) ||
                ( grid[rowNum][pos] == -1 &&  grid[rowNum][pos] != grid[rowNum][pos-1])
                )
            return -1;
        return rowNum >= grid.length-1 ? pos + grid[rowNum][pos] :findBallRec(pos + grid[rowNum][pos] , grid , rowNum+1);
    }

    public static void main(String[] args) {
        int [][] input1 = {{1,1,1,-1,-1},{1,1,1,-1,-1},{-1,-1,-1,1,1},{1,1,1,1,-1},{-1,-1,-1,-1,-1}};
        int [][] input2 = {{-1}};
        int [][] input3  = {{1,1,1,1,1,1},{-1,-1,-1,-1,-1,-1},{1,1,1,1,1,1},{-1,-1,-1,-1,-1,-1}};
        System.out.println(Arrays.toString(new Day1().findBall(input1)));
        System.out.println(Arrays.toString(new Day1().findBall(input2)));
        System.out.println(Arrays.toString(new Day1().findBall(input3)));
    }
}
