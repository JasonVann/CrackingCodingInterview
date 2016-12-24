class Ex50(object):
    def myPow2(self, x, n):
        if(n==0): 
            return 1
        if(n<0):
            n = -n
            x = 1/x        
        ans = 1
        while(n>0):
            if(n&1):
                ans *= x
            x *= x
            n >>= 1        
        return ans;

    def myPow(self, x, n):
        return self.myPow_helper(1, x, n)
        
    def myPow_helper(self, a, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """        
        if n == 0:
            return 1
        if n == 1:
            return a*x
        if n < 0:
            return 1*1.0/self.myPow_helper(1, x, -n)
        else:
            if n % 2 == 0:
                return self.myPow_helper(a, x*x, n/2)
            else:
                return self.myPow_helper(a*x, x, n-1)                
            
    def myPow0(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = x
        a = 1
        while n > 1:
            if n % 2 == 0:
                res = res*res
                n = n/2
            else:
                a = a*x
                n = n - 1
        return a * res
    '''
    double pow(double x, int n) {
        if(n<0){
            x = 1.0/x;
            n = -n;
        }
        int unsigned m = n;
        double tbl[32] = {0};
        double result = 1;
        tbl[0] = x;
        for(int i=1;i<32;i++){
            tbl[i] = tbl[i-1]*tbl[i-1];
        }
        for(int i=0;i<32;i++){
            if( m & (0x1<<i) )
            result *= tbl[i];
        }
        return result;
    }
    '''
ex50 = Ex50()
#print 50, ex50.myPow(5, 13)
#print 50, ex50.myPow(34.005, -3)
print 50, ex50.myPow2(3, 6)
