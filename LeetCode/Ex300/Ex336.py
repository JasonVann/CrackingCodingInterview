class Solution(object):
    def palindromePairs3(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # O(n2)
        ans = []
        l = len(words)
        for i in range(l):
            w = words[i]
            for j in range(i+1, l):
                w2 = words[j]
                if self.is_palindrome(w+w2):
                    ans.append([i, j])
                if self.is_palindrome(w2+w):
                    ans.append([j, i])
        return ans

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dic = {}
        res = set()
        palindrome = {}
        for i, w in enumerate(words):
            dic[w] = i
            if w and self.is_palindrome(w):
                palindrome[w] = i
        for i, w in enumerate(words):
            if len(w) == 0:
                for k, v in palindrome.items():
                    res.add((i, v))

            cands = self.expand_for(w)
            for cand in cands:
                if cand in dic:
                    j = dic[cand]
                    res.add((i, j))
            cands = self.expand_rev(w)
            for cand in cands:
                if cand in dic:
                    j = dic[cand]
                    res.add((j, i))
        ans = []
        for (i, j) in res:
            ans.append([i, j])
        return ans

    def expand_for(self, word):
        cands = set([word])
        l = len(word)
        for i in range(l+1):
            cand = word[:] + word[:i][::-1]
            if self.is_palindrome(cand):
                #print(word, cand, word[:i][::-1])
                cands.add(word[:i][::-1])
        cands.remove(word)
        return cands

    def expand_rev(self, word):
        cands = set([word])
        l = len(word)
        for i in range(l+1):
            cand2 = word[-i-1:][::-1] + word[:]
            #reversed(cand2)
            #print(word, cand2, word[-i-1:])
            if self.is_palindrome(cand2):
                cands.add(word[-i-1:][::-1])
        cands.remove(word)
        return cands

    def is_palindrome(self, word):
        l = len(word)
        for i in range(l):
            if word[i] != word[l-i-1]:
                return False
        return True

Ex336 = Solution()
words = ['lls']
words = ["abcd","dcba","lls","s","sssll"]
words = ["a",""]
#words = ['abcd', 'dcba']
print(Ex336.expand_for('sssll'))
print(Ex336.expand_rev('sssll'))
print(Ex336.is_palindrome('abc'))
print(Ex336.palindromePairs(words))


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
