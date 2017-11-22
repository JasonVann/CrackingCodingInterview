class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        import collections
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
                #print(39, cur, END, cur[END], words[cur[END]])
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans

words = ["w","wo","wor","worl","world"]
#words = ["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]
words = ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]
#words = ['y', 'yo', 'yod', 'yodn']
#words = reversed(words)
Ex720 = Solution()
print(Ex720.longestWord(words))
