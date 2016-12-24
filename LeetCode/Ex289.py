class Ex289(object):
    def reset(self, board):
        for row in board:
            for i in range(len(row)):
                if row[i][1] == 'F':
                    row[i] = 0
                else:
                    row[i] = 1
                    
    def count(self, board, i, j):
        neighbors = [0] * 9
        row = board[i]
        if i > 0:
            if j > 0:
                c1 = board[i-1][j-1]
                if c1 == 1 or (c1 != 0 and c1[0] == 'T'):
                    neighbors[0] = 1
            c2 = board[i-1][j]
            if c2 == 1 or (c2 != 0 and c2[0] == 'T'):
                neighbors[1] = 1
            if j < len(row) - 1:
                c3 = board[i-1][j+1]
                if c3 == 1 or (c3 != 0 and c3[0] == 'T'):
                    neighbors[2] = 1
        if j > 0:
            c4 = board[i][j-1]
            if c4 == 1 or (c4 != 0 and c4[0] == 'T'):
                neighbors[3] = 1
            if i < len(board) - 1:
                c7 = board[i + 1][j-1]
                if c7 == 1 or (c7 != 0 and c7[0] == 'T'):
                    neighbors[6] = 1
        if j < len(row) - 1:
            c6 = board[i][j+1]
            if c6 == 1 or (c6 != 0 and c6[0] == 'T'):
                neighbors[5] = 1
            if i < len(board) - 1:
                c9 = board[i + 1][j+1]
                if c9 == 1 or (c9 != 0 and c9[0] == 'T'):
                    neighbors[8] = 1
        if i < len(board) - 1:
            c8 = board[i + 1][j]
            if c8 == 1 or (c8 != 0 and c8[0] == 'T'):
                neighbors[7] = 1
                
        return sum(neighbors)
            
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                temp = self.count(board, i, j)                
                if row[j] == 1:
                    if temp < 2:
                        row[j] = 'TF'
                    elif temp > 3:
                        row[j] = 'TF'
                    else:
                        row[j] = 'TT'
                else:
                    if temp == 3:
                        row[j] = 'FT'
                    else:
                        row[j] = 'FF'
        self.reset(board)

