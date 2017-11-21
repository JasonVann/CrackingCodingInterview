# Ex374
target = 10
def guess(n, target):
    if n > target:
        return -1
    elif n < target:
        return 1
    else:
        return 0

class Ex374(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        while l < h - 1:            
            mid = l + (h-l)/2 
            res = guess(mid) 
            if res == -1:
                h = mid
            elif res == 0:
                return mid
            else:
                l = mid
        return l if guess(l) == 0 else l + 1i

def guessNumber(n):
    """
    :type n: int
    :rtype: int
    """ 
    lo = 1
    high = n
    while(lo <= high):
        new = (lo + high)/2
        res = guess(new)
        if(res == 1):
            lo = new + 1
        elif res == -1:
            high = new -1
        else:
            return new
