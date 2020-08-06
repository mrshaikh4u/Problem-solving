class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cnt = 0
        if not word or len(word)==0:
            return False
        for c in word:
            if c.isupper():
                cnt+=1
        if cnt == len(word) or cnt==0:
            return True
        if cnt==1 and word[0].isupper():
            return True
        return False


obj = Solution()
print(obj.detectCapitalUse("USA"))
print(obj.detectCapitalUse("FlaG"))
print(obj.detectCapitalUse("Google"))
print(obj.detectCapitalUse("leetcode"))
