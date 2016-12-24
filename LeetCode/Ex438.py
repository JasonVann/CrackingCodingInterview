class Ex438(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # n
        res = []
        l = len(s)
        n = len(p)   
        if l < n:
            return []
           
        dic = {}
        for i in p:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        start = 0
        count = 0
        for i in range(len(s)):
            cur = s[i]
            failed = False
            failed2 = False
            if cur not in dic:
                failed2 = True
            elif dic[cur] >= 1:
                dic[cur] -= 1
                count += 1
            else:
                failed = True
            if count == len(p):
                res.append(start)
                dic[s[start]] += 1
                count -= 1
                start += 1
                continue
            if i - start == n-1 or failed or failed2:
                if failed2:
                    for j in s[start:i]:
                        dic[j] += 1
                    start = i + 1
                    count = 0
                    continue
                if s[start] in dic and s[start] != s[i]:
                    dic[s[start]] += 1
                    count -= 1                    
                
                start += 1
        return res
        
    def findAnagrams0(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # n*nlog(n)
        res = []
        l = len(s)
        n = len(p)   
        if l < n:
            return []
           
        p1 = list(p)
        p1.sort()
        for i in range(l-n+1):
            cur = list(s[i:i+n])
            cur.sort()
            if cur == p1:
                res.append(i)
        return res
        
ex438 = Ex438()
s = 'cbaebabacd'
p = 'abc'
s = "cbaebabacd"
p = "abc"
print 438, ex438.findAnagrams(s, p)

