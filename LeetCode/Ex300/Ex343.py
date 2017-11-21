class Ex343(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        res = []
        while n > 4:
            res.append(3)
            n = n - 3
        res.append(n)
        return reduce(lambda x, y: x * y, res, 1)
        
    def integerBreak0(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Too slow
        res = {}
        res[2] = [[1,1]]
        i = 2
        while i < n:
            i += 1
            temp = []
            for cell in res[i-1]:
                for j in range(len(cell)):
                    cell2 = cell[:]
                    cell2[j] += 1
                    temp.append(cell2)
                    temp.append(cell[:] + [1])
            temp.append([1, i-1])
            #newlist=[ii for n,ii in enumerate(temp) if ii not in temp[:n]]
            newlist = []

            #temp.sort()
            for a in temp:
                a.sort()
                if a not in newlist:
                    newlist.append(a)
            res[i] = newlist 
        #print res, len(res)
        max_res = 1
        max_cell = []
        for j in res[n]:
            temp = reduce(lambda x, y: x * y, j, 1)
            if temp > max_res:
                max_res = temp
                max_cell = j
        print 135, max_cell
        return max_res
        
    '''
    public int integerBreak(int n) {
       int[] dp = new int[n + 1];
       dp[1] = 1;
       for(int i = 2; i <= n; i ++) {
           for(int j = 1; j < i; j ++) {
               dp[i] = Math.max(dp[i], (Math.max(j,dp[j])) * (Math.max(i - j, dp[i - j])));
           }
       }
       return dp[n];
    }
    '''
        
ex343 = Ex343()
n = 20
print 343, ex343.integerBreak(n)

