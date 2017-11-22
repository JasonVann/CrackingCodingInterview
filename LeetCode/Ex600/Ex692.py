class Solution:
    def topKFrequent2(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]

    def topKFrequent_heap(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in xrange(k)]

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
