class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        res = bin(num)
        res = res[2:]
        #c = res.count('0')
        count = 0
        count_one = 0
        for c in range(len(res)-1, -1, -1):
            if res[c] == '0':
                count += 1
            else:
                count_one += 1
        #return res, count
        if count_one == 1 and count % 2 == 0:
            return True
        return False
