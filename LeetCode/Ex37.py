import time
from collections import defaultdict

start_time = time.time()

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        dic = defaultdict(list)
        unknown = defaultdict(list)
        d_r = defaultdict(list)
        d_v = defaultdict(list)
        d_sq = defaultdict(list)
        l_board = []
        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                cell = row[j]
                i_sq = 3 * (i / 3) + j / 3
                if cell == '.':
                    #unknown.append((i, j))
                    d_r[i] += [None]
                    d_v[j] += [None]
                    #d_sq[i_sq] += [None]
                else:
                    val = int(cell)
                    dic[val] += [(i, j)]
                    d_r[i] += [val]
                    d_v[j] += [val]
                    d_sq[i_sq] += [val]

        l_board = []
        for i in range(9):
            l_board.append([])
        while True:
            found_count = 0
            for i in range(9):
                row = []
                for j in range(9):

                    if board[i][j] != '.':
                        row.append(int(board[i][j]))
                    else:
                        cell = d_r[i][j]
                        if cell != None:
                            continue
                        all = [x for x in range(1, 10)]
                        false = d_r[i] + d_v[j]
                        i_sq = 3 * (i / 3) + j / 3
                        false += d_sq[i_sq]
                        candidate = list(set(all) - set(false))

                        if len(candidate) == 1:
                            d_r[i][j] = candidate[0]
                            d_v[j][i] = candidate[0]
                            d_sq[i_sq] += candidate
                            found_count += 1
                        '''
                        else:
                            unknown[len(candidate)] += [[candidate, (i, j)]]
                            row.append(list(candidate))
                        '''
                l_board[i] = row
            if found_count == 0:
                break

        #Then clean up unknown
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] == '.' and d_r[i][j] == None:
                    all = [x for x in range(1, 10)]
                    false = d_r[i] + d_v[j]
                    i_sq = 3 * (i / 3) + j / 3
                    false += d_sq[i_sq]
                    candidate = list(set(all) - set(false))

                    if len(candidate) > 1:
                        unknown[len(candidate)] += [[candidate, (i, j)]]
                        row.append(list(candidate))
            l_board[i] = row

        # Then backtrack


        print l_board
        return

board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
sol = Solution()
sol.solveSudoku(board)

print time.time() - start_time