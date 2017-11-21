class Ex36(object):
    # 69ms, Beats 97% :)
    def extract_col(self, board, k):
        col = []
        for row in board:
            col.append(row[k])
        return col
        
    def extract_square(self, board, k):
        row = k / 3
        col = k % 3
        res = []
        for row3 in range(3*row, 3*row+3):
            res += board[row3][col*3:3*col+3]
        return res
        
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check row
        for row in board:
            row2 = [(num) for num in row if num != '.']
            
            if len(row2) != len(set(row2)):
                #print 77, row2
                return False
        # check column
        for k in range(9):
            col = self.extract_col(board, k)
            col2 = [(num) for num in col if num != '.']
            if len(col2) != len(set(col2)):
                #print 86, k, col2
                return False
        # check square
        for k in range(9):
            a_square = self.extract_square(board, k)
            a_square2 = [(num) for num in a_square if num != '.']
            if len(a_square2) != len(set(a_square2)):
                #print 93, k, a_square2
                return False
        return True
    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dic = {}
        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                cell = row[j]
                k = (i/3)*3 + j/3
                if cell != '.':
                    if cell not in dic:
                        dic[cell] = [[i], [j], [k]]
                    else:
                        if i in dic[cell][0] or j in dic[cell][1] or k in dic[cell][2]:
                            print 72, dic
                            return False
                        dic[cell][0].append(i)
                        dic[cell][1].append(j)
                        dic[cell][2].append(k)                        
        return True
    '''
    def isValidSudoku(self, board):
        seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
        return len(seen) == len(set(seen))
    '''
    
ex36 = Ex36()
board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
#board = [".........","......3..","...18....","...7.....","....1.97.",".........","...36.1..",".........",".......2."]
board = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
print 36, ex36.isValidSudoku(board)
