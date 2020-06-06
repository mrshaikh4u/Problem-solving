from typing import List


class Solution:

    def diff(self,word:str , found:str)->int:
        cnt=0
        for i in range(len(word)):
            if word[i]!=found[i]:
                cnt+=1
        return cnt

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or beginWord == endWord:
            return 0
        if endWord not in wordList:
            return 0
        found = []
        found.append(beginWord)
        step = 1
        while endWord not in found:
            current_cnt = len(found)
            i=0
            while i in range(len(wordList)):
                for w in found:
                    if self.diff(wordList[i],w)==1:
                        found.append(wordList[i])
                        wordList.remove(wordList[i])
                        i-=1
                        # break
                i+=1
            if current_cnt == len(found):
                break
            found = found[current_cnt:]
            step+=1

        if endWord in found:
            return step
        return 0

obj  = Solution()
print(obj.ladderLength("a","c",["a","b","c"]))

