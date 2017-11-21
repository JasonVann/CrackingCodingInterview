# Ex292
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        else:
            return True
        fail = [1,2,3]
        my_fail = [4, 8,]
        al_fail = [1,2,3, 5, 6, 7,]
