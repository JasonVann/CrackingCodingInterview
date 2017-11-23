#import sys
#sys.setrecursionlimit(650000)

class Solution:
    # 500ms
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lookup = set()
        for word in words:
            if len(word) != 0:
                lookup.add(word)
        self.ans = set()
        for word in words:
            if len(word) == 0:
                continue
            self.dfs(lookup, word, word, [])
        return list(self.ans)

    def dfs(self, lookup, word, orig, path):
        l = len(word)
        for i in range(1, l+1):
            temp = word[:i]
            if temp in lookup:
                path2 = path + [temp]
                rest = word[i:]
                if rest in lookup:
                    self.ans.add(orig)
                    return True, None
                ans, temp = self.dfs(lookup, rest, orig, path2)
                if temp:
                    self.ans.add(temp)
                    return True, None
                if ans:
                    return True, None
        temp = ''.join(path)
        if temp == orig and len(path) > 1:
            return True, temp
        return False, None

class Solution_by_letter:
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lookup = set()
        for word in words:
            lookup.add(word)
        self.ans = []
        for word in words:
            self.dfs(lookup, word, word, [])
        ans = set()
        for l in self.ans:
            temp = ''.join(l)
            if temp not in ans:
                ans.add(temp)
        return list(ans)

    def dfs(self, lookup, word, orig, path):
        l = len(word)
        for i in range(1, l+1):
            temp = word[:i]
            if temp in lookup:
                path2 = path + [temp]
                rest = word[i:]
                path2 = self.dfs(lookup, rest, orig, path2)
                if path2:
                    self.ans.append(path2)
        temp = ''.join(path)
        if temp == orig and len(path) > 1:
            return path
        return None

Ex472 = Solution()
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(Ex472.findAllConcatenatedWordsInADict(words))

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
