# Ex258                                
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        '''
        while num >= 10:
            a = str(num)
            num = reduce(lambda x,y: int(x) + int(y), a)
            
        return num
        '''
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9 
