class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        while n > 0:
            i += 1
            n -= i
            
        if n == 0:
            return i
        return i - 1
