class Ex342(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = 1
        if num < 0:
            return False
        while n < num:
            n = n << 2
        return n == num
    '''
    bool isPowerOfFour(int n) {
        return n>0 && (n&(n-1))==0 && (n&0x55555555);
    }
    '''
            
ex342 = Ex342()
print 342, ex342.isPowerOfFour(1)

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

'''
First,greater than 0.Second,only have one '1' bit in their binary notation,so we use x&(x-1) 
to delete the lowest '1',and if then it becomes 0,it prove that there is only one '1' bit.
Third,the only '1' bit should be locate at the odd location,for example,16.It's binary is 00010000.
So we can use '0x55555555' to check if the '1' bit is in the right place.

public boolean isPowerOfFour(int num) {
        return num > 0 && (num&(num-1)) == 0 && (num & 0x55555555) != 0;
        //0x55555555 is to get rid of those power of 2 but not power of 4
        //so that the single 1 bit always appears at the odd position 
    }
'''
'''
bool isPowerOfFour(int num) {
    return num > 0 && (num & (num - 1)) == 0 && (num - 1) % 3 == 0;
}
'''
