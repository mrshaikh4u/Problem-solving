from typing import List


class Solution:


    def __init__(self):
        self.board = list

    def changeRec(self,row : int , col : int):
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]):
            return
        elif self.board[row][col] !='O':
            return
        self.board[row][col] = '#'
        self.changeRec(row-1,col)
        self.changeRec(row+1 ,col)
        self.changeRec(row , col-1)
        self.changeRec(row , col+1)


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board)==0:
            return
        self.board = board
        for i in range(len(board)):
            j=0
            self.changeRec(i,j)
            j= len(self.board[0])-1
            self.changeRec(i,j)

        for j in range(len(self.board[0])):
            i=0
            self.changeRec(i,j)
            i = len(self.board)-1
            self.changeRec(i,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '#':
                    board[i][j]='O'
                elif board[i][j] =='O':
                    board[i][j] = 'X'


    # def solve(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     if not board or len(board)==0:
    #         return
    #     for i in range(len(board)):
    #         if board[i][0] == 'O':
    #             board[i][0]= '#'
    #             if len(board[i]) > 1 and board[i][1]=='O':
    #                 board[i][1]='#'
    #         if len(board[i])-1 > 0 and board[i][len(board[i])-1] == 'O':
    #             board[i][len(board[i])-1]= '#'
    #             if len(board[i])-2 >0 and board[i][len(board[i])-2]=='O':
    #                 board[i][len(board[i])-2]='#'
    #         if i==0:
    #             for j in range(len(board[i])):
    #                 if board[i][j] == 'O':
    #                     board[i][j]='#'
    #                     if i+1 < len(board) and board[i+1][j] == 'O':
    #                         board[i+1][j] = '#'
    #         if i==len(board)-1:
    #             for j in range(len(board[i])):
    #                 if board[i][j] == 'O':
    #                     board[i][j]='#'
    #                     if i-1 > 0 and board[i-1][j] == 'O':
    #                         board[i-1][j] = '#'
    #     for i in range(len(board)):
    #         for j in range(len(board[i])):
    #             if board[i][j]=='O':
    #                 board[i][j] ='X'
    #             elif board[i][j]=='#':
    #                 board[i][j]='O'







            # for j in range(len(board[0])):
            #     if board[i][j] == 'O':
            #         self.changeRec(board,i,j)

# board = [['X','X','X','X'],
#          ['X','O','O','X'],
#          ['X','X','O','X'],
#          ['X','O','X','X']]

# board = [['X','O','X','X'],
#          ['X','O','O','O'],
#          ['X','O','O','X'],
#          ['X','O','X','X']]

# board = [['X','X','X','X'],
#          ['X','O','O','X'],
#          ['X','O','X','X']]

# board = [['X','O','X','X']]

board = [["O","X","X","O","X"],
         ["X","O","O","X","O"],
         ["X","O","X","O","X"],
         ["O","X","O","O","O"],
         ["X","X","O","X","O"]]

obj = Solution()
for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j],end=' ')
    print()

obj.solve(board)
print('output : ')

for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j],end=' ')
    print()

