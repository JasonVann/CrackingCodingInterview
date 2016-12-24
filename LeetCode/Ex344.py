# Ex344
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        # for i in range(len(s)-1, -1, -1):
            # res += s[i]
        # for i in range(len(s)):
            # res = s[i] + res
        # Fastest 
        res = [s[i] for i in range(len(s) -1, -1, -1)]
        res = ''.join(res)
        # j = len(s) - 1
        # for i in range(len(s)):
            # if i >= j:
                # return res
            # temp = s[j]
            # s[j] = s[i]
            # s[i] = temp
            # j -= 1
            
        return res
