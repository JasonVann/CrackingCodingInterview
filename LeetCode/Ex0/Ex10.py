class Ex10(object):  
    def isMatch1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) > len(p) and ('*' not in p): 
            return False
        if s == p:
            return True
        if p == '.*':
            return True
            
        s2 = set(s)
        p2 = set(p)
        if len(s2) == len(p2) == 1 and '*' in p2:
            return True
            
        dic = {}
        i = 0
        j = 0
        while j < len(p) and i < len(s):
            if s[i] == p[j] or p[j] == '.':
                if j < len(p) - 1 and p[j+1] != '*':
                    i += 1
                    j += 1
                elif j < len(p) - 1 and p[j+1] == '*':
                    pass
                    
            elif s[i] != p[j] and p[j] != '.':
                if j < len(p) - 1 and p[j+1] == '*':
                    j+=2;
       
       
ex10 = Ex10()
s = 'aab'
p = 'c*a*b'
#print 10. ex10.isMatch(s, p)

