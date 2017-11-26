class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        self.lookup = {}
        self.cand = [chr(ord('a')+i) for i in range(26)]
        for word in wordList:
            for i in range(0, len(word)):
                new_word = word[:i] + word[i+1:]
                if new_word in self.lookup:
                    temp = self.lookup[new_word]
                    if i in temp:
                        temp[i] += [word]
                    else:
                        temp[i] = [word]
                    self.lookup[new_word] = temp
                else:
                    temp = {}
                    temp[i] = [word]
                    self.lookup[new_word] = temp
        self.l = len(wordList)

        self.ans = []
        self.beginWord = beginWord
        self.endWord = endWord

        self.best = self.l+1
        if endWord not in wordList:
            return self.ans
        self.dfs(beginWord)
        return self.ans

    def dfs(self, beginWord):
        from collections import deque
        queue = deque()
        queue.append((beginWord, [beginWord]))
        while len(queue) != 0:
            word, path = queue.pop()
            for i in range(0, len(word)):
                part = word[:i] + word[i+1:]
                if part not in self.lookup:
                    continue
                for new_word in self.lookup[part][i]:
                    #new_word = word[:i] + c + word[i+1:]
                    if new_word in path:
                        continue
                    if new_word == self.endWord:
                        temp = path + [new_word]
                        if len(temp) < self.best:
                            self.best = len(temp)
                            self.ans = []
                            self.ans.append(temp)
                        elif len(temp) == self.best:
                            self.ans.append(temp)
                    #elif new_word in self.lookup:
                    queue.append((new_word, path + [new_word]))

    def bfs(self, beginWord):
        from collections import deque
        queue = deque()
        queue.append((beginWord, [beginWord]))
        while len(queue) != 0:
            word, path = queue.popleft()
            for i in range(0, len(word)):
                part = word[:i] + word[i+1:]
                if part not in self.lookup:
                    continue
                for new_word in self.lookup[part][i]:
                    #new_word = word[:i] + c + word[i+1:]
                    if new_word in path:
                        continue
                    if new_word == self.endWord:
                        temp = path + [new_word]
                        if len(temp) < self.best:
                            self.best = len(temp)
                            self.ans = []
                            self.ans.append(temp)
                        elif len(temp) == self.best:
                            self.ans.append(temp)
                    #elif new_word in self.lookup:
                    queue.append((new_word, path + [new_word]))

class Solution2:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        self.lookup = set()
        for word in wordList:
            self.lookup.add(word)
        self.l = len(wordList)
        self.ans = []
        self.beginWord = beginWord
        self.endWord = endWord
        self.cand = [chr(ord('a')+i) for i in range(26)]
        self.best = self.l+1
        if endWord not in self.lookup:
            return self.ans
        self.bfs(beginWord)
        return self.ans

    def bfs(self, beginWord):
        from collections import deque
        queue = deque()
        queue.append((beginWord, [beginWord]))
        while len(queue) != 0:
            word, path = queue.popleft()
            for i in range(0, len(word)):
                for c in self.cand:
                    if c == word[i]:
                        continue
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in path:
                        continue
                    if new_word == self.endWord:
                        temp = path + [new_word]
                        if len(temp) < self.best:
                            self.best = len(temp)
                            self.ans = []
                            self.ans.append(temp)
                        elif len(temp) == self.best:
                            self.ans.append(temp)
                    elif new_word in self.lookup:
                        queue.append((new_word, path + [new_word]))

    def dfs(self, word, path, depth):
        if depth > self.l or depth > self.best:
            return False
        for i in range(0, len(word)):
            for c in self.cand:
                if c == word[i]:
                    continue
                new_word = word[:i] + c + word[i+1:]
                if new_word in path:
                    continue
                if new_word == self.endWord:
                    temp = path + [new_word]
                    if len(temp) < self.best:
                        self.best = len(temp)
                        self.ans = []
                        self.ans.append(temp)
                    elif len(temp) == self.best:
                        self.ans.append(temp)
                elif new_word in self.lookup:
                    self.dfs(new_word, path + [new_word], depth + 1)

Ex126 = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
beginWord = "qa"
endWord = "sq"
wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
print(Ex126.findLadders(beginWord, endWord, wordList))
