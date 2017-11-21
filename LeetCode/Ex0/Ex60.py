class Ex60(object):
    def cal_perm(self, n):
        i = 1
        res = 1
        while i <= n:
            res = res * i
            i += 1
        return res
        
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        cand = range(1, n + 1)
        j = 0
        i = 1
                
        res = []
        
        while len(cand) > 0:
            t1 = self.cal_perm(len(cand)-1)
            #if t1 < k:
            if k % t1 == 0:
                temp = k / t1
            else:
                temp = k / t1 + 1
            print 81, temp, cand
            temp = cand[temp-1]
            res.append(str(temp))
            cand.remove(temp)
            k = k - k / t1 * t1
            print 90, res, cand, k, t1, temp
                    
        return ''.join(res)
        
ex60 = Ex60()
print 60, ex60.getPermutation(4, 3)

