class Ex70(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        all = [1,2]
        if n <= 2:
            return all[n - 1]
        while len(all) < n:
            s = len(all)
            new = all[s - 2] + all[s - 1]
            all.append(new)
        return all[-1]
        
ex70 = Ex70()
print 70, ex70.climbStairs(4)
