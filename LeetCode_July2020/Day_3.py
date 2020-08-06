from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if not cells or len(cells)==0 or N==0:
            return cells
        N = 14 if (N % 14 == 0) else (N % 14)
        dp = []
        dp.append([i for i in cells])
        dp.append([0 for _ in range(len(cells))])
        print(dp)
        f = 0
        while N >= 0:
            dp[f^1][0] = 0
            dp[f^1][len(cells)-1]=0
            for j in range(1,len(cells)-1):
                dp[f^1][j] = 1 if dp[f][j-1] == dp[f][j+1] else 0
            N-=1
            f^=1
        return dp[f^1]

obj= Solution()
input = [1,0,0,1,0,0,1,0]
print(obj.prisonAfterNDays(input,1000000000))
# [0, 0, 0, 1, 0, 0, 1, 0]
# [01010010]
# [0, 0, 1, 1, 1, 0, 0, 0]
