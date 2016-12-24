class Ex205(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 8 times faster
        dic_s = {}
        for i in range(len(s)):
            if s[i] not in dic_s:
                dic_s[s[i]] = [i]
            else:
                dic_s[s[i]].append(i)
        t = list(t)
        for k, v in dic_s.items():
            cur = t[v[0]]
            for j in v:
                if t[j] != cur:
                    return False
            if j < len(t) - 1 and cur in t[j+1:]:
                return False
        #print t
        return '0' not in t
                    
        '''# slow
        dic_s = {}
        for i in range(len(s)):
            if s[i] not in dic_s:
                dic_s[s[i]] = [i]
            else:
                dic_s[s[i]].append(i)
        dic_t = {}
        for i in range(len(s)):
            if t[i] not in dic_t:
                dic_t[t[i]] = [i]
            else:
                dic_t[t[i]].append(i)
        dic_s2 = dic_s.copy()
        t_v = dic_t.values()
        print dic_s, dic_t
        for k,v in dic_s.items():
            if v in t_v:
                dic_s2.pop(k)
            else:
                return False
        return len(dic_s2.keys()) == 0
        '''
        
ex205 = Ex205()
print 205, ex205.isIsomorphic('egg', 'add')
print 205, ex205.isIsomorphic('foo', 'bar')
print 205, ex205.isIsomorphic('paper', 'title')
print 205, ex205.isIsomorphic('aab', 'aaa')
