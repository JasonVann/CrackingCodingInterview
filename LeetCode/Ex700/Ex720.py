class TrieNode:
    def __init__(self):
        self.child = [None]*26
        self.is_end_of_word = False

class Dis(object):
    def longestWord3(self, words):
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in xrange(1, len(word))):
                    ans = word
        return ans

    def longestWord2(self, words):
        resword, res = '', {''}
        for word in sorted(words):
            if word[:-1] in res:
                res.add(word)
                resword = max(resword, word, key=len)
        return resword

    def longestWord(self, words):
        # Python2
        import collections
        from functools import reduce
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = trie.values()
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                print(39, cur, END, cur[END], words[cur[END]])
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans


class HashTable:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        lookup = set()
        for word in words:
            lookup.add(word)
        best = ''
        for word in words:
            for i in range(len(word)+1):
                if word[:i+1] in lookup:
                    if i > len(best):
                        best = word[:i+1]
                    elif i == len(word) and len(word) == len(best) and word < best:
                        best = word
                else:
                    break
        return best

class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = Trie()
        for word in words:
            trie.addWord(word)
        node = trie.root
        best = ''
        path = ''
        best = self.expand(node, path, best)
        return best

    def expand(self, node, path, best):
        last_node = node
        for idx, child in enumerate(node.child):
            if child:
                new_path = path + chr(idx+ord('a'))
                if child.is_end_of_word:
                    if len(best) < len(new_path):
                        best = new_path
                    elif len(best) == len(new_path) and new_path < best:
                        best = new_path

                    best = self.expand(child, new_path, best)
        return best


class Trie2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        # self.child = [None]*26
        # self.is_end_of_word = False

    def addWord(self, word):
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

words = ["w","wo","wor","worl","world"]
#words = ["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]
words = ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]
#words = ['y', 'yo', 'yod', 'yodn']
#words = reversed(words)
Ex720 = Solution()
Ex720 = Dis()
print(Ex720.longestWord(words))
