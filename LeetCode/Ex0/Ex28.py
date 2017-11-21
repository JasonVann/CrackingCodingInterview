class Ex28(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if haystack == "":
            return -1        
        i = 0
        cur = -1
        j = 0
        while i < len(needle):
            while j < len(haystack):
                if haystack[j] == needle[i]:                    
                    if i == 0:
                        cur = j
                    if i == len(needle) - 1 or j == len(haystack) - 1:
                        if len(haystack) - cur < len(needle):
                            return -1
                        return cur
                    j += 1
                    i += 1
                else:
                    #j = cur
                    j = j - i + 1
                    i = 0
                    cur = -1
                    '''
                    if needle[0] != haystack[j]:
                        j += 1
                    '''
            i+=1
        return cur
    '''
    public int strStr(String haystack, String needle) {
      for (int i = 0; ; i++) {
        for (int j = 0; ; j++) {
          if (j == needle.length()) return i;
          if (i + j == haystack.length()) return -1;
          if (needle.charAt(j) != haystack.charAt(i + j)) break;
        }
      }
    }
    '''
ex28 = Ex28()
h = 'happysusundays'
n = 'sunday'
h = ""
n = "a"
h = "mississippi"
n = "a"
h = "mississippi"
n = "issip"

print 28, ex28.strStr(h, n)
