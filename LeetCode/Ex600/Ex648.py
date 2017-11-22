class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        self.trie = Trie()
        for w in dict:
            self.trie.insert(w)
        res = []
        for word in sentence.split():
            prefix = self.trie.prefix(word)
            if prefix:
                res += [prefix]
            else:
                res += [word]
        return ' '.join(res)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

def replaceWords(roots, sentence):
    import collections
    _trie = lambda: collections.defaultdict(_trie)
    trie = _trie()
    END = True
    for root in roots:
        cur = trie
        for letter in root:
            cur = cur[letter]
        cur[END] = root

    def replace(word):
        cur = trie
        for letter in word:
            if letter not in cur: break
            cur = cur[letter]
            if END in cur:
                return cur[END]
        return word

    return " ".join(map(replace, sentence.split()))

class TrieNode:
    def __init__(self):
        self.child = [None]*26
        self.is_end_of_word = False
        self.val = None


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word, val=None):
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
        node.val = val
        node.is_end_of_word = True

    def prefix(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        path = ''
        for i in range(len(prefix)):
            if node.is_end_of_word:
                return prefix[:i]
            idx = ord(prefix[i])-ord('a')
            if node.child[idx] == None:
                return None
            node = node.child[idx]

        return None

ex648 = Solution()
#ex648.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
print(replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
