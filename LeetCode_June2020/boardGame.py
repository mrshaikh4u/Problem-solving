from typing import List
from collections import defaultdict

class Solution:

    def __init__(self):
        self.board = None
        self.used = set(())

    def prepareLookupBoard(self)->{}:
        tracker = defaultdict(list)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                current_list = tracker.get(self.board[i][j])
                if tracker.get(self.board[i][j]) is None:
                    current_list = list()
                current_list.append((i,j))
                tracker.update({self.board[i][j]:current_list})
        return tracker

    def findRec(self,word:str,idx:int,row:int,col:int)->bool:
        if row < 0 or row >= len(self.board) or col <0 or col>=len(self.board[0]) or idx >=len(word) or (row,col) in self.used:
            return False
        elif word[idx] != self.board[row][col]:
            if (row,col) in self.used:
                self.used.remove((row,col))
            return False
        else:
            if idx == len(word)-1:
                return True
            else:
                self.used.add((row,col))
                to_return = self.findRec(word , idx+1,row+1,col) or self.findRec(word , idx+1,row-1,col) or self.findRec(word , idx+1,row,col-1) or self.findRec(word , idx+1,row,col+1)
                if not to_return and (row,col) in self.used:
                    self.used.remove((row,col))
                return to_return


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or len(board)==0:
            return []
        self.board = board
        ch_tracker = self.prepareLookupBoard()
        output = []
        for w in words:
            positions = ch_tracker.get(w[0])

            if positions is None or len(positions)==0:
                continue
            found = False
            for pos in positions:
                self.used = set()
                if not found:
                    if self.findRec(w,0,pos[0],pos[1]):
                        output.append(w)
                        found = True
                else:
                    break
        print(output)
        return output


obj = Solution()
board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]
# words = ["oath","pea","eat","rain","fhiii"]
# board = [["a","b"],["a","a"]]
# words =  ["aba","baa","bab","aaab","aaa","aaaa","aaba"]

board = [["a","b","c"],["a","e","d"],["a","f","g"]]
words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]

obj.findWords(board,words)
