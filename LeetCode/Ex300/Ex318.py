class Ex318(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic = {}
        # O(n)
        dic3 = {}
        if words == []:
            return 0
            
        for i in range(97, 123):
            bitmap = ''
            key = chr(i)
            val = []
            for j in range(len(words)):
                if key in words[j]:
                    val.append(j)
                    bitmap += '1'
                else:
                    bitmap += '0'
            #dic[key] = val
            dic3[key] = int(bitmap, 2)
        #print dic
        dic2 = {}
        temp = -1
        found = False
        dic = dic3
        max_l = 2**(len(words)) - 1
        for w in words:
            share = 0
            for l in w:
                share = share | dic[l]
            #non_share = ~share
            non_share = max_l - share
            #non_share = [i for i in range(len(words)) if i not in share]
            #print non_share, w
            dic2[w] = non_share
            if non_share > 0:
                found = True
        if not found:
            return 0
        #print dic2
        print 1753, dic2
        for w in words:
            non_share = dic2[w]
            bin_ns = bin(non_share)
            j = -1
            while True:
                if bin_ns[j] != '0':
                    cur = len(w) * len(words[j])
                    #print 1744, w, words[j], 'j=', j, bin_ns, cur
                    if temp == -1 or temp < cur:
                        temp = cur
                    
                j -= 1
                if bin_ns[j] == 'b':
                    break
                                
        #print 1763, len(dic2), temp
        return 0 if temp == -1 else temp
        
    '''
    int maxProduct(vector<string>& words) {
        vector<int> mask(words.size());
        vector<int> lens(words.size());
        for(int i = 0; i < words.size(); ++i) lens[i] = words[i].length();
        int result = 0;
        for (int i=0; i<words.size(); ++i) {
            for (char c : words[i])
                mask[i] |= 1 << (c - 'a');
            for (int j=0; j<i; ++j)
                if (!(mask[i] & mask[j]))
                    result = max(result, lens[i]*lens[j]);
        }
        return result;
    }
    '''
    def maxProduct2(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Slow: uses list as share
        dic = {}
        # O(n)
        for i in range(97, 123):
            key = chr(i)
            val = []
            for j in range(len(words)):
                if key in words[j]:
                    val.append(j)
            dic[key] = val
        #print dic
        dic2 = {}
        temp = -1
        found = False
        # O(n)
        print 1740, len(dic2)
        for w in words:
            share = []
            for l in w:
                share += dic[l]
            non_share = list(set([i for i in range(len(words))]) - set(share))
            #non_share = [i for i in range(len(words)) if i not in share]
            #print non_share, w
            dic2[w] = non_share
            if len(non_share) > 0:
                found = True
        if not found:
            return 0
        #print dic2
        print 1753, len(dic2)
        #return len(dic2)
        for w in words:
            non_share = dic2[w]
            
            for k in non_share:
                cur = len(w) * len(words[k])
                #print 1744, w, words[k], cur
                if temp == -1 or temp < cur:
                    temp = cur
        print 1763, len(dic2)
        return 0 if temp == -1 else temp
                
        
ex318 = Ex318()
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
words = ["ab", "ac", "ade", "ef"]
#words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
#words = ["a", "aa", "aaa", "aaaa"]
print 318, ex318.maxProduct(words)
