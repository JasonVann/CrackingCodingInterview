class Ex67(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        carry = '0'
        a0 = a[:]
        res = []
        for i in range(1, len(a)):
            s1 = a[-i]
            if i <= len(b):
                s2 = b[-i]
            else:
                s2 = '0'
            cur = []
            cur += [s1, s2, carry]
            if cur.count('1') == 2:
                carry = '1'
                res.append('0')
            elif cur.count('1') > 2:
                res.append('1')
                carry = '1'
            elif cur.count('1') == 1:
                carry = '0'
                res.append('1')
            else:
                carry = '0'
                res.append('0')
        cur = []
        if len(b) < len(a):
            cur = [carry, a[0]]
        else:
            cur = [carry, a[0], b[0]]
        if cur.count('1') == 2:
            res.append('0')
            res.append('1')
        elif cur.count('1') == 3:
            res.append('1')
            res.append('1')
        elif cur.count('1') == 1:
            res.append('1')
            
        #print 96, res
        return ''.join(res[::-1]) if len(res) !=0 else '0'
        '''
        int curIntA = i>-1?Character.getNumericValue(a.charAt(i)):0;
            int curIntB = j>-1?Character.getNumericValue(b.charAt(j)):0;
            res=(curIntA ^ curIntB ^ c)+res;
            c = (curIntA+curIntB+c) >= 2 ? 1 : 0;
        '''
        
ex67 = Ex67()
a = '11'
b = '1'
a = '0'
b = '0'
print 67, ex67.addBinary(a, b)

