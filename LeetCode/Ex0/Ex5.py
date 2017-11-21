class Ex5(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        i = 0
        j = len(s) - 1
        count = 0
        res = ''
        temp = 0
        while i < len(s):
            cur = s[i:i+temp+1]
            #if cur[::-1] == s[i+temp+1:i+temp+1+len(cur)]:
            if cur[::-1] in s[i+1:]:
                temp += 1
            else:
                if temp > count:   
                    #temp += 1
                    #if cur[::-1] == s[i+temp+1:i+temp+1+len(cur)]:
                    if cur == cur[::-1]:
                        res = cur
                        count = temp
                    temp = 0
                i+=1
        return res if res != '' else s[0]
        
        
ex5 = Ex5()
s = 'abcefecbagba'
s = 'aa'
s = ''
print 5, ex5.longestPalindrome(s)
