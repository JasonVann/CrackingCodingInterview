class Peer:
    '''
    public class Solution {
    public boolean wordBreak(String s, Set<String> dict) {
        boolean[] f = new boolean[s.length() + 1];
        f[0] = true;
        //Second DP
        for(int i=1; i <= s.length(); i++){
            for(int j=0; j < i; j++){
                if(f[j] && dict.contains(s.substring(j, i))){
                    f[i] = true;
                    break;
                }
            }
        }

        return f[s.length()];
    }
}
    '''
    def word_break_SN(s, words):
     	d = [False] * len(s)
     	for i in range(len(s)):
     		for w in words:
     			if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
     				d[i] = True
     	return d[-1]

    def wordBreak(self, s, words):
        # O(n2)
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]

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
