class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        lookup = {}
        for i, word in enumerate(wordDict):
            lookup[word] = i
        self.lookup = lookup
        self.l = len(s)
        self.map = set()
        self.search(s, 0, '')
        return (self.l-1) in self.map

    def search(self, s, j, cur):
        while j < self.l:
            cur = cur + s[j]
            if cur in self.lookup:
                if j not in self.map:
                    self.map.add(j) # can reach from 0 to 'j'
                    res = self.search(s, j+1, '')
                    #self.search(s, j+1, cur)
            j += 1
        return

Ex139 = Solution()
s = "aaaaaaa"
wordDict = ["aaaa","aa"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(Ex139.wordBreak(s, wordDict))
