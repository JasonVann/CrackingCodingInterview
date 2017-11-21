class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.ans = []
        state = ['.'*n]*n
        self.expand(state, 0)
        return self.ans

    def expand(self, state, i):
        if i == self.n:
            self.ans.append(state)
            return
        for j in range(0, self.n):
            if not self.check_constraint(state, i, j):
                continue

            state2 = state.copy()
            state2[i] = state2[i][:j] + 'Q' + state2[i][j+1:]
            #state2[i, j] = 'Q'
            self.expand(state2, i+1)

    def check_constraint(self, state, i, j):
        if state[i][j] == 'Q':
            return False
        if 'Q' in state[i]:
            return False
        for k in range(self.n):
            if state[k][j] == 'Q':
                return False
        if i < j:
            s = i
            b = j
        else:
            s, b = j, i
        '''
        for m in range(1, s+1):
            if (i-m) >=0 and (j-m) >= 0 and state[i-m][j-m] == 'Q':
                return False
        for m in range(1, self.n+1-b):
            if (i+m) < self.n and (j+m) < self.n and state[i+m][j+m] == 'Q':
                return False
        '''
        for m in range (0, self.n):
            # m+n == i+j, m-n = i-j
            if i+j-m >=0 and i+j-m < self.n and state[m][i+j-m] == 'Q':
                return False
            if m+j-i >= 0 and m+j-i < self.n and state[m][m+j-i] == 'Q':
                return False

            '''
            if (i-m) >=0 and (j-m) >= 0 and state[i-m][j-m] == 'Q':
                return False

            if (i+m) < self.n and (j-m) >= 0 and state[i+m][j-m] == 'Q':
                return False
            if (i-m) >=0 and (j+m) < self.n and state[i-m][j+m] == 'Q':
                return False

            if (i+m) < self.n and (j+m) < self.n and state[i+m][j+m] == 'Q':
                return False
            '''
        return True

    def format_str(self, board):
        ans = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                if [i, j] in board:
                    if board[i][j] == 'Q':
                        row.append('Q')
                    elif board[i][j] == 'F':
                        row.append('.')

ex51 = Solution()
ans = ex51.solveNQueens(2)
print(ans)
