class Ex326(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n <= 0:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            else:
                n = n/3
        return True
    '''
    public boolean isPowerOfThree(int n) {
        // 1162261467 is 3^19,  3^20 is bigger than int  
        return ( n>0 &&  1162261467%n==0);
    }
    '''

