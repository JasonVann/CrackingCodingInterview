class Ex263(object):
    def isUgly(self, num):
        if num == 1:
            return True
        elif num <= 0:
            return False
        else:
            return self.iter(num)
    def iter(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #print num
        if num % 2 == 0:
            temp = num /2
            return self.isUgly(temp)
        elif num % 3 == 0:
            temp = num /3
            return self.isUgly(temp)
        elif num % 5 == 0:
            temp = num /5
            return self.isUgly(temp)
        elif num % 2 == 1:
            return False   

ex263 = Ex263()
print ex263.isUgly(63)
