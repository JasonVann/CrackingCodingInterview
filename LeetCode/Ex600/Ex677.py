class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.trie.insert(key, val)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.trie.startsWith(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

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

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        total = 0
        for i in range(len(prefix)):
            idx = ord(prefix[i])-ord('a')
            if node.child[idx] == None:
                return total
            node = node.child[idx]
        stack = [node]
        if node.is_end_of_word:
            total += node.val
        while stack:
            node = stack.pop()
            for child in node.child:
                if child:
                    if child.is_end_of_word:
                        if child.val:
                            total += child.val
                    stack.append(child)
        return total



# Your MagicDictionary object will be instantiated and called as such:
obj = MapSum()
obj.insert('apple', 4)
#obj.insert('app', 2)
#obj.insert('app', 3)
print(obj.sum('apple'))
