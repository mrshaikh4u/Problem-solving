from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s)-1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1


obj  = Solution()
s = ['b','a','b','a']
print(s)
obj.reverseString(s)
print(s)