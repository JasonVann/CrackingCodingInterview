class Ex202(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        all = []
        temp = n
        while temp != 1:
            all.append(temp)
            t2 = 0
            for i in range(len(str(temp))):
                t2 += (temp % 10) ** 2
                temp = temp / 10
            temp = t2
            if temp in all:
                return False
        return True
    # Interesting idea
    '''
        int digitSquareSum(int n) {
        int sum = 0, tmp;
        while (n) {
            tmp = n % 10;
            sum += tmp * tmp;
            n /= 10;
        }
        return sum;
    }

    bool isHappy(int n) {
        int slow, fast;
        slow = fast = n;
        do {
            slow = digitSquareSum(slow);
            fast = digitSquareSum(fast);
            fast = digitSquareSum(fast);
        } while(slow != fast);
        if (slow == 1) return 1;
        else return 0;
    }
    '''
    
ex202 = Ex202()
print 202, ex202.isHappy(14)
