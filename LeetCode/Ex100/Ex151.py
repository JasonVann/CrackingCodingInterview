class Ex151(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s = s.replace('  ', ' ')
        a = s.split(' ')
        #print a
        a.reverse()
        a = ' '.join(a)
        a = a.replace('  ', ' ')
        #print len(a)
        return a
       
ex151 = Ex151()
print 151, ex151.reverseWords("   a   b ")
