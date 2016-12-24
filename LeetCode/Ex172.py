def fact(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res

class Ex172(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        count = 0
        while n > 0:
            res *= n
            n -= 1
        #print res
        while res > 0:
            if res % 10 == 0:
                count += 1
            else:
                break
            res = res / 10
        #print count
        return count
        
ex172 = Ex172()
print 172, ex172.trailingZeroes(2599)
