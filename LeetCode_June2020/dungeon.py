from typing import List
from functools import lru_cache
class Solution:

    def __init__(self):
        self.dungeon = [[]]

    @lru_cache(maxsize=10**6)
    def calculateRec(self,row:int ,col:int)->int:
        if row == len(self.dungeon)-1 and col == len(self.dungeon[0])-1:
            return 1 if self.dungeon[row][col] > 0 else - self.dungeon[row][col]+1
        elif row == len(self.dungeon)-1:
          return max(1,self.calculateRec(row , col+1)-self.dungeon[row][col])
        elif col == len(self.dungeon[0]) -1:
            return max(1,self.calculateRec(row+1,col)-self.dungeon[row][col])
        else:
            return max(1,min(self.calculateRec(row+1,col)-self.dungeon[row][col],self.calculateRec(row,col+1)-self.dungeon[row][col]))


    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        self.dungeon = dungeon
        return self.calculateRec(0,0)

obj = Solution()
input = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(obj.calculateMinimumHP(input))