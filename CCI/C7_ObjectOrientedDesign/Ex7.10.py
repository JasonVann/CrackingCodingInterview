import numpy as np

class MineSweeper():
    def __init__(self, N, mine_num):
        self.board = Board

class Board():
    def __init__(self, N, mine_num):
        self.mine_percent = mine_num/(N*N)

    def initialized_board(self):
        data = []
        for i in range(N):
            row = []
            for j in range(N):
                if np.random.rand() <= self.mine_percent:
                    cell = Cell(True, i, j)
                else:
                    cell = Cell(False, i, j)
                row.append(cell)
            data.append(row)
        self.data = data

    def in_board(self, r, c):
        return 0 <= r and r <= N - 1 and c >= 0 and c <= N - 1

    def get_neighbors(self, r, c):
        res = [(r+i, c+j) for i in (-1, 0, 1) for j in (-1, 0, 1)]
        count = 0
        ans = []
        if r1, c1 in res:
            if not (r1 == r and c1 == c):
                if self.in_board(r1, c1) and not self.data[r1][c1].uncovered:
                    ans.append((r1, c1))
        return ans

    def show_blank(self, r, c):
        neighbors = self.get_neighbors(r, c)
        count = 0
        to_check = []
        while len(neighbors) > 0:
            cell = neighbors.pop(0)
            if not cell.has_mine:
                count += 1
            cell.uncovered = True
            to_check.append(cell)
        cell.display = count
        for cell in to_check:
            self.show_blank(cell.pos)

    def uncover_cell(self, r, c):
        cell = self.data[r][c]
        if not cell.uncover():
            return -1 # Game over
        else:
            self.show_blank(r, c)

    def display_board(self):
        for i in range(N):
            for j in range(N):
                cell = self.data[i][j]:
                if not cell.uncovered:
                    cell.uncover()


class Cell():
    def __init__(self, has_mine, i, j):
        self.has_mine = has_mine
        self.uncovered = False
        self.flag = False
        self.display = 'blank' # or num, or 'mine', or 'flag'
        self.pos = (i, j)

    def flag(self):
        if not self.flag:
            self.flag = True
            self.display = 'flag'

    def uncover(self):
        if not self.uncovered:
            if not self.has_mine:
                return True
            else:
                return False
        return True
