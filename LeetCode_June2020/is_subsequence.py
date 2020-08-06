
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if t is None or len(t)==0:
            return s is None or len(s)==0
        if s is None or len(s)==0:
            return True
        # s = "abc", t = "ahbgdc"
        ptr = 0
        for c in s:
            found = False
            while ptr < len(t):
               if t[ptr] == c:
                   found = True
                   ptr+=1
                   break
               ptr+=1
            if found == False:
                return False
        return True


obj = Solution()
print(obj.isSubsequence("","abcd"))


