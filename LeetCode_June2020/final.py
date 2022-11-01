
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n
        dp = [0 for _ in range(n+2)]
        for i in range(1,n+1,1):
            dp[i]=i
            j=1
            while j*j <= i:
                dp[i]=min(dp[i],dp[i-j*j]+1)
                j+=1
        return dp[n]

obj = Solution()
print(obj.numSquares(13))