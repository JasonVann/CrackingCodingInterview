class Ex231(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        '''
        while n >= 2:
            if n % 2 == 1:
                return False
            n = n>>1
        return True
        '''
        return bin(n).count('1')==1
