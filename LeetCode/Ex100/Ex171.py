class Ex171(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            temp = ord(s[i]) - 64
            res += temp * 26 ** (len(s) - i - 1)
        return res
        
ex171 = Ex171()
print 171, ex171.titleToNumber('IZZ')
