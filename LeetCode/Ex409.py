# Ex 409
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0) + 1
        res = 0
        count_odd = False
        for k,v in dic.items():
            if v % 2 == 1:
                count_odd += 1
            res += 2* (v//2)
        return res + 1 if count_odd > 0 else res

#print longestPalindrome('abccccdd')
#print longestPalindrome('cccddaaa')
