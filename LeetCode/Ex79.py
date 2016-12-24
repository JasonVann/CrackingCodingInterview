class Ex79(object):
    def test(self, board, i, j, path, word, idx):
        if idx == len(word):
            return True
        '''
        if i < 0 or j < 0:
            return False
        if i >= len(board) or j >= len(board[0]):
            return False
        '''
        if word[idx] != board[i][j]:
            return False
        if (i, j) in path:
            return False

        path = set(path)
        path.add((i, j))
        # If do this, then no need to keep path, a bit faster
        #t = board[i][j] 
        #board[i][j] = 0
        if j < len(board[0]) - 1:
            r2 = self.test(board, i, j+1, path, word, idx+1)
            if r2:
                return True
        if i < len(board) - 1:
            r3 = self.test(board, i+1, j, path, word, idx+1)
            if r3:
                return True
        if i > 0:
            r1 = self.test(board, i-1, j, path, word, idx+1)
            if r1:
                return True
        if j > 0:
            r4 = self.test(board, i, j-1, path, word, idx+1)
            if r4:
                return True
        #board[i][j] = t
        return False
        
    def exist(self, board, word):
        if len(word) == 0:
            return True
            
        m = len(board)        
        n = len(board[0])
        if n == 0:
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    b =  self.test(board, i, j, set(), word, 0)
                    if b:
                        return True
        return False
        
    def exist0(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        '''
        stack = deque()
        path_cand = deque()
        path = deque()
        started = False
        '''
        if len(word) == 0:
            return True
            
        m = len(board)        
        n = len(board[0])
        if n == 0:
            return False
        dic = {}
        for i in range(m):
            for j in range(n):
                if board[i][j] in word:
                    if board[i][j] in dic:
                        dic[board[i][j]] += [(i, j)]
                    else:
                        dic[board[i][j]] = [(i, j)]
        if len(dic.keys()) < len(set(word)):
            return False
        print 109, dic
        for (i, j) in dic[word[0]]:
            b =  self.test(board, dic, i, j, [], word, 0)
            if b:
                return True
        return False
    '''
    board[y][x] ^= 256 it's a marker that the letter at position x,y is a part of word we search.
    After board[y][x] ^= 256 the char became not a valid letter. After second board[y][x] ^= 256
    it became a valid letter again.
    public boolean exist(char[][] board, String word) {
        char[] w = word.toCharArray();
        for (int y=0; y<board.length; y++) {
            for (int x=0; x<board[y].length; x++) {
                if (exist(board, y, x, w, 0)) return true;
            }
        }
        return false;
    }

    private boolean exist(char[][] board, int y, int x, char[] word, int i) {
        if (i == word.length) return true;
        if (y<0 || x<0 || y == board.length || x == board[y].length) return false;
        if (board[y][x] != word[i]) return false;
        board[y][x] ^= 256;
        boolean exist = exist(board, y, x+1, word, i+1)
            || exist(board, y, x-1, word, i+1)
            || exist(board, y+1, x, word, i+1)
            || exist(board, y-1, x, word, i+1);
        board[y][x] ^= 256;
        return exist;
    }
    '''
    
ex79 = Ex79()
board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
word = 'ABCCED'
board = ["a"]
word = 'a'
print 79, ex79.exist(board, word)

