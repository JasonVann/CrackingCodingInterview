class Ex89(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l = 2 ** n
        res = []
        i = 0
        start = ['0'] * n
        while i < l:
        
            i += 1
        res = ['000', '001', '011', '010']
        res2 = []
        for r in res:
            r = '0b' + r
            r = ''.join(r)
            r = int(r, 2)
            res2.append(r)
        return res2
        
ex89 = Ex89()
n = 3
print 89, ex89.grayCode(n)

