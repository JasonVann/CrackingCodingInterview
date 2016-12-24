class Ex38(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        if n > 1:
            res = self.countAndSay_helper(res, n-1)
        return res
        
    def countAndSay_helper(self, res, n):
        """
        :type n: int
        :rtype: str
        """
        #res = '1'
        last = res           
        if n >= 1:
            res = res.split(' ')
            res = ''
            strike = 1
            i = 0
            while i < len(last)-1:
                if last[i] == last[i+1]:                
                    strike += 1
                    i+=1
                else:      
                    res += str(strike)
                    res += str(last[i])
                    
                    strike = 1
                    i+=1
            # Then describe the last digit
            if strike == 1:
                res += '1' + last[-1]
            elif strike > 1:
                res += str(strike)+ last[-1]
            return self.countAndSay_helper(res, n - 1)
            
        return res
    '''
    public String countAndSay(int n) {
        StringBuilder prev = new StringBuilder("1");
        StringBuilder curr = new StringBuilder("");
        int i = 0;
        while (--n > 0) {
            for (int j = 1; j <= prev.length(); j++) {
                if (j == prev.length() || prev.charAt(j) != prev.charAt(i)) {
                    curr.append(j-i);
                    curr.append(prev.charAt(i));
                    i = j;
                }
            }
            prev = curr; i = 0;
            curr = new StringBuilder("");
        }
        return prev.toString();
    }
    '''
    
ex38 = Ex38()
n = 3
print 38, ex38.countAndSay(n)


