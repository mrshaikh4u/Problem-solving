from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ignore_row_list = [0,len(board)-1]
        ignore_col_list = [0,len(board[0])-1]
        for i in range(len(board)):
            if i in ignore_row_list:
                continue
            for j in range(len(board[i])):
                if j in ignore_col_list or board[i][j]=='X':
                    continue
                if board[i][j]=='O':
                    if (board[i-1][j] =='O' and (i-1)==0) or (board[i+1][j] == 'O' and (i+1)==len(board)-1):
                        pass
                    elif (board[i][j-1] =='O' and j-1==0) or (board[i][j+1]=='O' and j+1==len(board[i])-1):
                        pass
                    else:
                        board[i][j]='X'

obj = Solution()
board =[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print('input : ')
print(board)
obj.solve(board)
print('output : ')
print(board)
