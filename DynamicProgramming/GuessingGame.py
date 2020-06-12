import math
class Solution:
    def divisorGame(self, N: int) -> bool:
        aliceTurn = True
        while N >= 2:
            exist = False
            sqrt = math.sqrt(N)
            i = sqrt if isinstance(math.sqrt(N),int) else round(sqrt)
            while i > 0 and i < N:
                if N % i == 0:
                    exist = True
                    N = N-i
                    break
                i-=1
            if not exist and not aliceTurn:
                return True
            if aliceTurn:
                print('alice guessed : ',(N+i)-i)
                aliceTurn = False
            else:
                print('bob guessed : ',(N+i)-i)
                aliceTurn = True
        return not aliceTurn

obj  = Solution()
print(obj.divisorGame(4))