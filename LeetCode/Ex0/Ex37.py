import time
from collections import defaultdict
import pprint

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

            if found_count == 0:
                break

        #Then find unknown
        has_unknown = False
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

        # Then backtrack
        guess = []
        #return

        back_track_count = 0
        m = 2
        n = 0
        i_sel = 0
        while True:

            k = unknown.keys()
            if len(k) == 0:
                break

            if n >= len(unknown[m]):
                n = 0
                m += 1
                while m not in unknown.keys() and m < max(unknown.keys()):
                    m += 1
            if m > max(unknown.keys()):
                break

            cand, (i, j) = unknown[m][n]

            i_sq = 3 * (i / 3) + j / 3

            while True:
                found = False
                if i_sel >= len(cand):
                    break
                if cand[i_sel] not in d_r[i] and cand[i_sel] not in d_v[j] and cand[i_sel] not in d_sq[i_sq]:
                    found = True
                    break
                else:
                    i_sel += 1
                    if i_sel >= len(cand):
                        break
            if found:
                guess.append([cand, (m, n), (i, j), i_sel])
                d_r[i][j] = cand[i_sel]
                d_v[j][i] = cand[i_sel]
                d_sq[i_sq] += [cand[i_sel]]
                i_sel = 0
            else:
                # Conflict, backtrack
                cand, (m, n), (i, j), i_sel = guess.pop()
                back_track_count += 1
                d_r[i][j] = None
                d_v[j][i] = None
                i_sq = 3 * (i / 3) + j / 3
                d_sq[i_sq].remove(cand[i_sel])
                #cand.pop(0)
                i_sel += 1
                continue

            last_check = (m, n)
            n = n + 1

            #break

        print back_track_count
        for i in range(9):
            row = d_r[i]
            row = [str(x) for x in row]
            d_r[i] = row

        for i in range(9):
            board[i] = ''.join(d_r[i])

        pp = pprint.PrettyPrinter(width = 4, depth=2)
        pp.pprint(d_r)
        return

board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board = ["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
board = ["........1", ".........",".........",".........",".........",".........",".........",".........","........."]
board = ["....54.9.",".1...9.26","...67....", "..8....61","1.......4","63....5..","....83...","25.4...1.",".9.21...."]
sol = Solution()
sol.solveSudoku(board)

print time.time() - start_time