from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return "".join(str(j) for j in (list(permutations(i for i in range(1, n+1)))[k-1]))
