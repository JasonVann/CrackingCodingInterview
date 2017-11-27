class TrieNode:
    def __init__(self):
        self.child = [None]*26
        self.is_end_of_word = False


class Trie_Recur:
    # Maybe better to use Trie and TrieNode, not a nested Trie class
    # http://www.geeksforgeeks.org/trie-insert-and-search/
    def __init__(self):
        """
        Initialize your data structure here.
        """
        #self.root = TrieNode()
        self.child = [None]*26
        self.is_end_of_word = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if len(word) == 0:
            self.is_end_of_word = True
            return

        idx = ord(word[0])-ord('a')
        if self.child[idx] == None:
            node = Trie()
            self.child[idx] = node
        else:
            node = self.child[idx]

        node.insert(word[1:])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False

        idx = ord(word[0])-ord('a')
        if self.child[idx] == None:
            return False
        if len(word) == 1 and self.child[idx] and self.child[idx].is_end_of_word:
            return True
        return self.child[idx].search(word[1:])

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if len(prefix) == 0:
            return True

        idx = ord(prefix[0])-ord('a')
        if self.child[idx] == None:
            return False
        if len(prefix) == 1 and self.child[idx]:
            return True
        return self.child[idx].startsWith(prefix[1:])


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

    def eact_search(self, word):
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


def test_Trie():
    word = 'test'
    obj = Trie()
    obj.insert(word)
    param_2 = obj.search(word)
    print(param_2)
    print(obj.search(word[:3]))
    print(obj.search('testb'))
    #param_3 = obj.startsWith(prefix)
    print(obj.startsWith('tes'))
