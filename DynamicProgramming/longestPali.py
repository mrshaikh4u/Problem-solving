from collections import Counter
class Solution:
    def __init__(self):
        self.output=""
        self.substrs=[]
        self.input=""

    def findPaliRec(self,idx):
        if idx >= len(self.input):
            return
        length = len(self.substrs)
        for i in range(length):
            currentList = list(self.substrs[i])
            currentList.append(self.input[idx])
            self.substrs.append(''.join(str(j) for j in currentList))
        self.findPaliRec(idx+1)

    def checkPali(self,input:str):
        counter = Counter(input)
        cnt=0
        for value in counter.values():
            if value%2 != 0:
                cnt+=1
        return not cnt > 1

    def checkPali2(self,input:str):
        return input[::] == input[::-1]


    def longestPalindrome(self, s: str) -> str:
        if not s or len(s)<=1:
            return s
        self.input = s
        self.substrs.append("")
        self.findPaliRec(0)
        del self.substrs[0]
        for i in self.substrs:
            if self.checkPali2(i):
                if len(i) > len(self.output):
                    self.output = i
        return self.output


obj  = Solution()
print(obj.longestPalindrome("cbbd"))