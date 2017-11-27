class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
        if p == '*' or p[-1] == '*':
            return True
        if '*' not in p and len(s) > len(p):
            return False
        if s == p:
            return True
        i = 0
        return self.match(s, p, 0, 0, len(p), None)

    def match(self, s, p, i, j, lp, last):
        while j < lp and i < len(s):
            c = p[j]
            if i >= len(s):
                return False
            '''
            if last == '*':
                res = self.match(s, p, i + 1, j, lp, last)
                if res:
                    return True
            '''
            if s[i] != c:
                res = True
                if c == '*':
                    if not res:
                        res = self.match(s, p, i, j+1, lp, None) # Don't use '*'
                    if not res:
                        res = self.match(s, p, i + 1, j+1, lp, None) # Use '*' once
                    res = self.match(s, p, i + 1, j, lp, c)
                elif c == '?':
                    res = self.match(s, p, i+1, j+1, lp, last)

                else:
                    return False
                if res:
                    return True
            else:
                i += 1
                j += 1
        #return True
        return i == len(s) and j == len(p)

Ex44 = Solution()
print(Ex44.isMatch("abefcdgiescdfimde","ab*cd?i*de"))
print(Ex44.isMatch("a", "aa"))


print(Ex44.isMatch("aa","a")) #→ false
print(Ex44.isMatch("aa","aa")) #→ true
print(Ex44.isMatch("aaa","aa")) #→ false
print(Ex44.isMatch("aa", "*")) #→ true
print(Ex44.isMatch("aa", "a*")) #→ true
print(Ex44.isMatch("ab", "?*")) #→ true
print(Ex44.isMatch("aab", "c*a*b")) #→ false
