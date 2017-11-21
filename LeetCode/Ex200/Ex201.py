class Ex201(object):
    def find_n(self, m, start):
        while start <= m:
            start *= 2
        return start
        
    def rangeBitwiseAnd(self, m, n):
        res = m
        i = m+1
        if m == 0:
            return 0
        a = self.find_n(m, 1)
        b = self.find_n(n, a)
        if b - a >= 2:
            return 0
        while i < n+1:
            res = res & i
            i += 1
        return res
        
    def rangeBitwiseAnd0(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = m
        # Memory limit
        for i in range(m+1, n+1):
            res = res & i
        return res
    '''
    public class Solution {
        public int rangeBitwiseAnd(int m, int n) {
            if(m == 0){
                return 0;
            }
            int moveFactor = 1;
            while(m != n){
                m >>= 1;
                n >>= 1;
                moveFactor <<= 1;
            }
            return m * moveFactor;
        }
    }
    '''
    '''
    int rangeBitwiseAnd(int m, int n) {
        return (n > m) ? (rangeBitwiseAnd(m/2, n/2) << 1) : m;
    }
    '''
    ''' #??
    public int rangeBitwiseAnd(int m, int n) {
        while(m<n) n = n & (n-1);
        return n;
    }
    '''
    
ex201 = Ex201()
m = 0
n = 2147483647
print 201, ex201.rangeBitwiseAnd(m, n)

