class Ex59(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(n):
            res.append([0] * n)
        cand = range(1, n * n + 1)
        i = 0
        ce = n 
        idx = 0
        while idx <= n / 2:
            # Right
            for j in range(idx, n-idx):
                res[idx][j] = cand[i]
                i += 1
            #idx += 1
            print 71, res
            # Down
            for j in range(idx+1, n-idx):
                res[j][n-idx-1] = cand[i]
                i += 1
            print 76, res
            # Left
            for j in range(n-idx-2, idx, -1):
                res[n-idx-1][j] = cand[i]
                i += 1
            print 81, res
            # Left
            for j in range(n-idx-1, idx, -1):
                res[j][idx] = cand[i]
                i += 1
            print 86, res
            idx += 1
        return res
        
ex59 = Ex59()
n = 5
print 59, ex59.generateMatrix(n)

