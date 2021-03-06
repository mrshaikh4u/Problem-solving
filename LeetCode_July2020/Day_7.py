from typing import List
class Ans:
    def __init__(self):
        self.ans = 0

class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    continue
                if i-1 < 0 or grid[i-1][j]==0:
                    cnt+=1
                if j-1<0 or grid[i][j-1] ==0:
                    cnt+=1
                if i+1 >= len(grid) or grid[i+1][j]==0:
                    cnt+=1
                if j+1 >= len(grid[0]) or grid[i][j+1]==0:
                    cnt+=1
        return cnt

obj = Solution()
# input = [[0,1,0,0],
#          [1,1,1,0],
#          [0,1,0,0],
#          [1,1,0,0]]
# input = [[0,1,1],
#          [0,0,1],
#          [0,0,1],
#          ]
input = [[1]
         ]
print(obj.islandPerimeter(input))