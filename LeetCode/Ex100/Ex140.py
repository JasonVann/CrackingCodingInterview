class Solution_Trie:
    # TLE
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.trie = Trie()
        for word in wordDict:
            self.trie.insert(word)
        self.ans = []
        i = 0
        j = 0
        node = self.trie.root
        self.s = s
        self.l = len(s)
        self.expand(node, 0, [])
        return self.ans

    def expand(self, node, j, path):
        while j < self.l:
            if node.is_end_of_word:
                path2 = path + [node.word]
                # Start from root again
                res = self.expand(self.trie.root, j, path2)
                # Or continue
                '''
                if res:
                    if node.is_end_of_word:
                        path += [node.word]
                    self.ans += [' '.join(path)]
                else:
                '''
                # path.pop()
            idx = ord(self.s[j]) - ord('a')
            if node.child[idx] == None:
                return False
            node = node.child[idx]
            j += 1

        if node.is_end_of_word:
            path = path + [node.word]

            self.ans += [' '.join(path)]
            return True
        return False

class Solution:
    # 500ms
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        lookup = set(wordDict)
        path = {}
        for word in wordDict:
            l = len(word)
            '''
            if l in path:
                path[l] += [word]
            else:
                path[l] = [word]
            '''
        self.ans = []
        self.s = s
        self.l = len(s)
        hit = set(path.keys())

        for i in range(self.l+1):
            for j in range(-1, i):
                if j != -1 and j not in path:
                    continue
                if s[j+1:i] in lookup:
                    hit.add(i-1)
                    extend = []
                    if j not in path:
                        extend = [s[j+1:i]]
                    else:
                        for cur in path[j]:
                            temp = cur + ' ' + s[j+1:i]
                            extend += [temp]
                    if i-1 not in path:
                        path[i-1] = extend
                    else:
                        path[i-1].extend(extend)
        if self.l-1 in path:
            return path[self.l-1]
        return []

    def dfs(self, lookup, word, start, path):
        l = self.l
        for i in range(start+1, l+1):
            temp = self.s[start:i]
            if temp in lookup:
                path2 = path + [temp]
                rest = word[i:]
                if rest in lookup:
                    self.ans.append(path + [rest])
                    return True, None
                ans, temp = self.dfs(lookup, rest, i, path2)
                if temp:
                    self.ans.append(temp)
                    return True, None
                if ans:
                    return True, None
        #temp = ''.join(path)
        if len(path) > 1:
            return True, path
        return False, None


class Solution3:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        lookup = {}
        max_l = 0
        for i, word in enumerate(wordDict):
            l = len(word)
            if l in lookup:
                lookup[l] = [word]
            else:
                lookup[l] += [word]
            max_l = max(l, max_l)
        self.lookup = lookup
        self.l = len(s)
        self.map = set()
        self.path = {}
        for i in range(self.l):
            j = 0
            while j <= max_l:
                if j in lookup:
                    for word in lookup[j]:
                        if s[i:j] != w:
                            pass
            if i in self.path:
                path = self.path[i]
            elif i == 0:
                path = ''
            else:
                continue
            for w in self.lookup:
                t = len(w)
                j = i + t
                path2 = str(path)
                if s[i:j] != w:
                    continue
                if j not in self.path:
                    path = path.split(',')
                    temp = []
                    for a in path:
                        if a == '':
                            temp.append(w)
                        else:
                            temp.append(a + ' ' + w)
                        #path = [a + ' ' + w for a in path]
                    path = temp
                    #path = path + ' ' + w
                    path = ','.join(path)
                    self.path[j] = path
                else:
                    self.path[j] += ',' + path + ' ' + w
                path = str(path2)
            if i in self.path:
                self.path.pop(i)
        #self.search(s, 0, 0, '', [])
        if self.l not in self.path:
            return []
        temp = self.path[self.l]
        #ans = ' '.join(temp[0])
        return temp.split(',')

    def search(self, s, start, j, cur, path):
        while j < self.l:
            cur = cur + s[j]
            if cur in self.lookup:
                if j not in self.map:
                    self.map.add(j) # can reach from 0 to 'j'
                if j not in self.path:
                    self.path[j] = [path + [cur]]
                else:
                    self.path[j].append(path + [cur])
                res = self.search(s, j, j+1, '', path + [cur])
                #self.search(s, j+1, cur)
            j += 1
        return


class Solution_ND:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        lookup = {}
        for i, word in enumerate(wordDict):
            lookup[word] = i
        self.lookup = lookup
        self.l = len(s)
        self.map = set()
        self.path = {}
        for i in range(self.l):
            if i in self.path:
                path = self.path[i]
            elif i == 0:
                path = ''
            else:
                continue
            for w in self.lookup:
                t = len(w)
                j = i + t
                path2 = str(path)
                if s[i:j] != w:
                    continue
                if j not in self.path:
                    path = path.split(',')
                    temp = []
                    for a in path:
                        if a == '':
                            temp.append(w)
                        else:
                            temp.append(a + ' ' + w)
                        #path = [a + ' ' + w for a in path]
                    path = temp
                    #path = path + ' ' + w
                    path = ','.join(path)
                    self.path[j] = path
                else:
                    self.path[j] += ',' + path + ' ' + w
                path = str(path2)
        #self.search(s, 0, 0, '', [])
        if self.l not in self.path:
            return []
        temp = self.path[self.l]
        #ans = ' '.join(temp[0])
        return temp.split(',')

    def search(self, s, start, j, cur, path):
        while j < self.l:
            cur = cur + s[j]
            if cur in self.lookup:
                if j not in self.map:
                    self.map.add(j) # can reach from 0 to 'j'
                if j not in self.path:
                    self.path[j] = [path + [cur]]
                else:
                    self.path[j].append(path + [cur])
                res = self.search(s, j, j+1, '', path + [cur])
                #self.search(s, j+1, cur)
            j += 1
        return

class Solution2:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        S = set()
        for word in wordDict:
            S.add(word)
        self.ans = []
        i = 0
        j = 0
        self.s = s
        self.l = len(s)
        self.expand(0, [])
        return self.ans

    def expand(self, j, path):
        while j < self.l:
            if node.is_end_of_word:
                path2 = path + [node.word]
                # Start from root again
                res = self.expand(self.trie.root, j, path2)
                # Or continue
                '''
                if res:
                    if node.is_end_of_word:
                        path += [node.word]
                    self.ans += [' '.join(path)]
                else:
                '''
                # path.pop()
            idx = ord(self.s[j]) - ord('a')
            if node.child[idx] == None:
                return False
            node = node.child[idx]
            j += 1

        if node.is_end_of_word:
            path = path + [node.word]

            self.ans += [' '.join(path)]
            return True
        return False

class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.is_end_of_word = False
        self.word = ''


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
            idx = ord(word[i]) - ord('a')
            if node.child[idx] == None:
                node2 = TrieNode()
                node.child[idx] = node2
            node = node.child[idx]
        node.is_end_of_word = True
        node.word = word

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
            idx = ord(word[i]) - ord('a')
            if word[i] != '.':
                if node.child[idx] == None:
                    return False
                else:
                    node = node.child[idx]
            else:
                for j in range(26):
                    if node.child[j] != None:
                        res = self.node_search(word[i + 1:], node.child[j])
                        if res:
                            return True
                return False
        return node.is_end_of_word

    def eact_search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
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
            idx = ord(prefix[i]) - ord('a')
            if node.child[idx] == None:
                return False
            node = node.child[idx]
        return True


Ex140 = Solution()
word = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
#word = "aaaaaaa"
#wordDict = ["aaaa","aa"]
word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(Ex140.wordBreak(word, wordDict))
