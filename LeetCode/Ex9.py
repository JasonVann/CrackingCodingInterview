class Ex9(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        n = 1
        while 10**n <= x:
            n += 1
        n -= 1
        i = 0
        j = n
        while j > i:
            l = (x / (10**j)) % 10
            r = x / (10**i) % 10
            if l != r:
                return False
            j -= 1
            i += 1            
        return True
    '''
    public class Solution {
        // 楼主的大概逻辑是，比如 1234321；
        每次通过除以10和对10取余来保存下前半部分x和后半部分v，比如 x = 123432, v=1;
        直到x=123，v=1234的时候，循环结束，再通过 v/10 == x，来判断数是不是回环的。

        static int v;
        public static boolean isPalindrome(int x) {
            //optimizations
            if(x<0) return false;
            if(x<10) return true;
            if(x%10==0) return false;
            if(x<100&&x%11==0) return true;
            if(x<1000&&((x/100)*10+x%10)%11==0) return true;

            //actual logic
            v=x%10;
            x=x/10;
            while(x-v>0)
            {
                    v=v*10+x%10;
                    x/=10;
            }
            if(v>x){v/=10;}
            return v==x?true:false;
        }
    }
    '''
    '''
    public boolean isPalindrome(int x) {
        if (x < 0) return false;

        int p = x; 
        int q = 0; 
        
        while (p >= 10){
            q *=10; 
            q += p%10; 
            p /=10; 
        }
        
        return q == x / 10 && p == x % 10;
    }
    '''
ex9 = Ex9()
x = -2147483648
x = -101
x = 10
x = 10101
x = 5
print 9, ex9.isPalindrome(x)

