from functools import lru_cache
class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0

    @lru_cache(maxsize=10**6)
    def findRec(self,row:int , col:int)->int:
        if row >= self.n or col>=self.m or row<0 or col<0:
            return 0
        elif row == 0 and col==0:
            return 0
        elif ( row ==0 and col==1) or (col ==0 and row ==1):
            return 1
        else:
            cnt = self.findRec(row-1,col) + self.findRec(row,col-1)
            return cnt


    def uniquePaths(self, m: int, n: int) -> int:
        self.m = m
        self.n = n
        if m ==1 and n==1:
            return 1
        return self.findRec(n-1,m-1)

obj = Solution()
print(obj.uniquePaths(7,3))
print(obj)
