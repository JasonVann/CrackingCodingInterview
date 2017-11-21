class Ex125(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            #print i, j, s[i], s[j], ord(s[i]), ord(s[j])
            
            if not ((ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122) or (ord(s[i]) >= 48 and ord(s[i]) <= 57)):
            #if s[i] == ' ':
                i += 1
                print 'a'
                continue
            if not ((ord(s[j]) >= 65 and ord(s[j]) <= 90) or (ord(s[j]) >= 97 and ord(s[j]) <= 122) or (ord(s[j]) >= 48 and ord(s[j]) <= 57)):
            #if s[j] == ' ':
                j -= 1
                continue
            #print 'b', s[i], s[j]
            if str.lower(str(s[i])) != str.lower(str(s[j])):
                return False
            i += 1
            j -= 1
        return True
        
    '''
    def isPalindrome(self, s):
        s=''.join([i.lower() for i in s if i.isalnum()])
        return s==s[::-1]
    '''
    
ex125 = Ex125()
test = "A man, a plan, a canal: Panama"
test = "race a car"
test = "0P"

print 125, ex125.isPalindrome(test)
