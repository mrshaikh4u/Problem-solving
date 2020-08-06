from typing import List


class Solution:

    def __init__(self):
        self.mat = [[]]

    def minRec(self,row,col):
        if row == 0 and col ==0:
            return self.mat[row][col]-1
        elif row<0 or row >= len(self.mat) or col<0 or col >= len(self.mat[0]):
            return 0
        else:
            topmin   = self.minRec(row-1,col)
            topmin = min(topmin + self.mat[row][col] , topmin)
            rightmin = self.minRec(row , col-1)
            rightmin = min(rightmin+self.mat[row][col] , rightmin)


            max(topmin,rightmin)
            return max(topmin + self.mat[row][col] , rightmin + self.mat[row][col])

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or len(dungeon)==0:
            return 0
        self.mat = dungeon
        output = self.minRec(len(self.mat)-1 , len(self.mat[0])-1)
        return output

obj = Solution()
input = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(obj.calculateMinimumHP(input))
