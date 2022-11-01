class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt = 0
        s= 0
        while n > s:
            cnt+=1
            s +=1
            n-=s
        return cnt

obj = Solution()
print(obj.arrangeCoins(1))
