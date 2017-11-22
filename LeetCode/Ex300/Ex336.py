class Solution(object):
    # Trie: https://discuss.leetcode.com/topic/39585/o-n-k-2-java-solution-with-trie-structure-n-total-number-of-words-k-average-length-of-each-word/2
    
    def palindromePairs_n2(self, words):
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

    def palindromePairs_quick(self, words):
        def is_palindrome(check):
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.iteritems():
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back],  k])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        self.dic = {}
        self.res = set()
        self.palindrome = {}
        for i, w in enumerate(words):
            self.dic[w] = i
            if w and self.is_palindrome(w):
                self.palindrome[w] = i
        for i, w in enumerate(words):
            if len(w) == 0:
                for k, v in self.palindrome.items():
                    self.res.add((i, v))

            self.expand_for(w)
            self.expand_rev(w)

        ans = []
        for (i, j) in self.res:
            ans.append([i, j])
        return ans

    def expand_for(self, word):
        #cands = set([word])
        l = len(word)
        for i in range(l+1):
            cand = word[:] + word[:i][::-1]
            comp = word[:i][::-1]

            if comp in self.dic:
                if self.is_palindrome(cand):
                    #print(word, cand, word[:i][::-1])
                    if comp == word:
                        continue
                    j = self.dic[comp]
                    k = self.dic[word]
                    self.res.add((k, j))

    def expand_rev(self, word):
        #cands = set([word])
        l = len(word)
        for i in range(l+1):
            cand2 = word[-i-1:][::-1] + word[:]
            #reversed(cand2)
            #print(word, cand2, word[-i-1:])
            comp = word[-i-1:][::-1]
            if comp in self.dic:
                if self.is_palindrome(cand2):
                    if comp == word:
                        continue
                    j = self.dic[comp]
                    k = self.dic[word]
                    self.res.add((j, k))

    def is_palindrome(self, word):
        return word == word[::-1]
        l = len(word)
        for i in range(l):
            if word[i] != word[l-i-1]:
                return False
        return True

Ex336 = Solution()
words = ['lls']
words = ["abcd","dcba","lls","s","sssll"]
#words = ["a",""]
#words = ['abcd', 'dcba']
#print(Ex336.expand_for('sssll'))
#print(Ex336.expand_rev('sssll'))
#print(Ex336.is_palindrome('abc'))
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
