class Ex7(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pre = ''
        if x < 0:
            pre = '-'
            x = -x
        #print x, str(10)
        all = str(x)
        res = ''
        for i in all:
            res = i + res
        res = int(pre + res)
        return 0 if abs(res) > (2**31 - 1) else res
        
ex7 = Ex7()
print 7, ex7.reverse(123)
print 7, ex7.reverse(-123)
