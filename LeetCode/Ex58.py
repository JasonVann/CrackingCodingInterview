class Ex58(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """        
        s = s.rstrip()
        if len(s) == 0:
            return 0
        j = len(s) - 1
        found = False
        while j >= 0 :
            if s[j] == ' ':
                found = True
                break
            j -= 1
        print found
        return len(s) - j - 1 if found else len(nums)

ex58 = Ex58()
s = 'Hello World'
s = 'a '
print 58, ex58.lengthOfLastWord(s)
