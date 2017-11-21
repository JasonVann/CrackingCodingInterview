class Ex387(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] = -1
            else:
                dic[s[i]] = i
        has_found = False
        #print dic
        for (k, v) in dic.items():
            if v <> -1:
                if not has_found or v < min_i:
                    min_i = v
                    has_found = True
        #print has_found, min_i
        return -1 if (not has_found) else min_i
      
ex387 = Ex387()
print 387, ex387.firstUniqChar('leetcode')
