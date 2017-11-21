class Ex405(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """   
        if num >= 0:
            res = self.toHexPos(num)  
            #print res
        else:
            num = -num
            a = (2**32-1) ^ (num - 1) # !! == ~(num - 1)
            #a = -num + 2**32
            
            res = self.toHexPos(a)
            print a, bin(a), res
        #print res
        return res
            
    def toHexPos(self, num):         
        dic = {}
        #print 'lib:', hex(num)
        # OR: num += 2**32 if num < 0
        for i in range(10):
            dic[i] = i
        for i in range(97, 103):
            dic[i-87] = chr(i)
        #print dic
        res = ''
        while num >= 16:
            (a, b) = divmod(num, 16)
            res += str(dic[b])
            num = a
        #print num
        if num > 0:
            res += str(dic[num])
        elif num == 0 and res == '':
            res += str(dic[num])
        return res[::-1]
        #print res, '0x' + res[::-1] 
        
ex405 = Ex405()
#print 405, ex405.toHex(6551231)
print 405, ex405.toHex(-1)
