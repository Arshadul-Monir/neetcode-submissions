class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            if len(set(i for i in row if i != ".")) != len([i for i in row if i != "."]):
                return False
        
        # check columns
        for i in range(len(board)):
            if len(set(row[i] for row in board if row[i] != ".")) != len([row[i] for row in board if row[i] != "."]):
                return False

        # check squares
        i = 0
        while i < len(board):
            j = 0
            while j < len(board[0]):
                c_square = [board[i][j],    board[i][j+1],      board[i][j+2],
                            board[i+1][j],  board[i+1][j+1],    board[i+1][j+2],
                            board[i+2][j],  board[i+2][j+1],    board[i+2][j+2]]
                
                if len(set(k for k in c_square if k != ".")) != len([k for k in c_square if k != "."]):
                    return False
                j += 3
            i += 3
        return True
        