class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        lookup = {}
        rev = {}
        for w in words:
            if w in lookup:
                lookup[w] += 1
            else:
                lookup[w] = 1
        for w, count in lookup.items():
            if count in rev:
                rev[count] += [w]
            else:
                rev[count] = [w]
        res = []
        keys = list(rev.keys())
        print(keys)
        keys = sorted(keys, reverse=True)
        for key in keys:
            w = rev[key]
            w = sorted(w)
            if len(w) < k:
                res += w
                k -= len(w)
            else:
                res += w[:k]
                break
        #print(lookup)
        #print(rev)
        return res

Ex692 = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(Ex692.topKFrequent(words, k))
