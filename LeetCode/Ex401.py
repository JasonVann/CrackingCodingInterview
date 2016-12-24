class Ex401(object):
    def printTime(self, num):
        minute = num % 64
        hour = num / 64
        if hour == 0:
            hour = '0'
        if minute < 10:
            minute = '0'+str(minute)
        if hour > 12:
            return
        if minute > 60:
            return
        return str(hour) + ':' + str(minute)
        
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        self.readBinary(9, 0, num, res)
        res2 = []
        for i in res:
            temp = self.printTime(i)
            if temp != None:
                res2.append(temp)
        return res2
        
    def readBinary(self, left, right, num, res):
        if num == 0:
            return res
        if num == 1:
            for i in range(left, right-1, -1):      
                i = 1<<i
                res.append(i)
            return res
        else:
            i = left
            res2 = 0
            raw = self.readBinary(i, num-1, res)
            for j in temp:
                j2 = list(bin(j)[2:])
                j2.reverse()
                last1 = j2.index('1')

            '''
            while i > num:
                temp = self.readBinary(i, num-1, res)
                i -= 1
                res2 += temp
            '''
            return res2
            
ex401 = Ex401()
num = 2
#print 401, ex401.readBinaryWatch(num)
#print ex401.printTime(1<<10)
            

