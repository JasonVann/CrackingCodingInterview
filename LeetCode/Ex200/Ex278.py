class Ex278(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        
        while l < r - 1:
            mid = (l+r)/2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
        return l if isBadVersion(l) else (l + 1)
