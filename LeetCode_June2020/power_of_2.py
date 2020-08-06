class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        while n > 1:
            mod = n % 2
            if mod !=0 :
                return False
            n /= 2
        return n == 1

obj = Solution()
print(obj.isPowerOfTwo(0))