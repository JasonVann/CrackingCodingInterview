class Ex91(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        if len(s) == 0:
            return 0
            
        A = [[[0]]] * len(s)
        A[0] = [[s[0]]]
        for i in range(1, len(s)):
            last = A[i-1]
            cur = []
            print 67, last, A
            for a in last:
                b = str(a[-1])
                if len(b) == 1 and int(b+s[i]) <= 26:
                    print 72, a, type(a)
                    c = a[:-1][:]
                    c.append(b+s[i])
                    cur.append(c)
                                 
                c = a[:]
                c.append(s)
                cur.append(c)
        print 80, A
        return len(A[-1])
        
    def numDecodings0(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
            
        A = [0] * len(s)
        if s[0] == '0':
            return 0
        else:
            A[0] = 1
        i = 1
        while i < len(s):
            if i < len(s) - 1 and s[i+1] == '0':
                A[i] = A[i-1]
                i += 1
                A[i] = A[i-1]
                continue  
            #print 71, i, s[i-1: i+1]
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 26 and s[i] != '0':
                A[i] = A[i-1] + 1
            else:
                '''
                if i >= 2 and s[i-1] == '0' and int(s[i-2:i]) > 26:
                    return 0
                '''
                if s[i-1] == '0' and s[i] == '0':
                    return 0
                if int(s[i-1:i+1]) > 26 and s[i] == '0':
                    return 0
                A[i] = A[i-1]
            i += 1
        return A[-1]
        
ex91 = Ex91()
s = "230"
print 91, ex91.numDecodings(s)

