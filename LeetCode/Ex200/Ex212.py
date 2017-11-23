#https://discuss.leetcode.com/topic/33246/java-15ms-easiest-solution-100-00

class Peer_trie:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
    #make trie
        trie={}
        for w in words:
            t=trie
            for c in w:
                if c not in t:
                    t[c]={}
                t=t[c]
            t['#']='#'
        self.res=set()
        self.used=[[False]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board,i,j,trie,'')
        return list(self.res)

    def find(self,board,i,j,trie,pre):
        if '#' in trie:
            self.res.add(pre)
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return
        if not self.used[i][j] and board[i][j] in trie:
            self.used[i][j]=True
            self.find(board,i+1,j,trie[board[i][j]],pre+board[i][j])
            self.find(board,i,j+1,trie[board[i][j]],pre+board[i][j])
            self.find(board,i-1,j,trie[board[i][j]],pre+board[i][j])
            self.find(board,i,j-1,trie[board[i][j]],pre+board[i][j])
            self.used[i][j]=False

class Peer:
    def findWords(self, board, words):
        # Complex number
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[None] = True
        board = {i + 1j*j: c
                 for i, row in enumerate(board)
                 for j, c in enumerate(row)}

        found = []
        def search(node, z, word):
            if node.pop(None, None):
                found.append(word)
            c = board.get(z)
            if c in node:
                board[z] = None
                for k in range(4):
                    search(node[c], z + 1j**k, word + c)
                board[z] = c
        for z in board:
            search(root, z, '')

        return found

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.board = board
        lookup = set(words)
        self.ans = set()
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)

        self.m = len(board)
        if self.m == 0:
            return self.ans
        self.n = len(board[0])
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                idx = ord(c)-ord('a')
                if self.trie.root.child[idx]:
                    seen = set()
                    seen.add((i, j))
                    word = [c]
                    node = self.trie.root.child[idx]
                    if node.is_end_of_word:
                        word = ''.join(word)
                        self.ans.add(word)
                    self.helper(node, seen, word, i, j)

        return list(self.ans)

    def helper(self, node, seen, word, i, j):
        cand = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for (r_idx, c_idx) in cand:
            if r_idx < 0 or r_idx >= self.m or c_idx < 0 or c_idx >= self.n:
                continue
            if (r_idx, c_idx) not in seen:
                c = self.board[r_idx][c_idx]
                idx = ord(c)-ord('a')
                if node.child[idx]:
                    seen.add((r_idx, c_idx))
                    node2 = node.child[idx]
                    full_word = word + [c]
                    if node2.is_end_of_word:
                        temp = ''.join(full_word)
                        self.ans.add(temp)
                    self.helper(node2, seen, full_word, r_idx, c_idx)
                    seen.remove((r_idx, c_idx))

class TrieNode:
    def __init__(self):
        self.child = [None]*26
        self.is_end_of_word = False




class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in range(len(word)):
            idx = ord(word[i])-ord('a')
            if node.child[idx] == None:
                node2 = TrieNode()
                node.child[idx] = node2
            node = node.child[idx]
        node.is_end_of_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False

        node = self.root
        if '.' not in word:
            return self.exact_search(word)
        return self.node_search(word, node)

    def node_search(self, word, node):
        for i in range(len(word)):
            idx = ord(word[i])-ord('a')
            if word[i] != '.':
                if node.child[idx] == None:
                    return False
                else:
                    node = node.child[idx]
            else:
                for j in range(26):
                    if node.child[j] != None:
                        res = self.node_search(word[i+1:], node.child[j])
                        if res:
                            return True
                return False
        return node.is_end_of_word

    def exact_search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in range(len(word)):
            idx = ord(word[i])-ord('a')
            if node.child[idx] == None:
                return False
            node = node.child[idx]
        return node.is_end_of_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in range(len(prefix)):
            idx = ord(prefix[i])-ord('a')
            if node.child[idx] == None:
                return False
            node = node.child[idx]
        return True


Ex212 = Peer()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain", "eate"]
#board = [["a"]]
#words = ["a"]
#board = [["a","a"]]
#words = ["aaa"]
res = Ex212.findWords(board, words)
print(res)
