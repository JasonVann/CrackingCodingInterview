class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.ans = []
        self.l = len(s)
        self.dfs(s, 0, [])
        return self.ans

    def dfs(self, s, start, path):
        for i in range(start+1, self.l+1):
            temp = s[start:i]
            if self.is_palindrome(s, start, i):
                res = self.dfs(s, i, path + [temp])
        temp = ''.join(path)
        if len(temp) == self.l:
            self.ans.extend([path])
            return True
        return False

    def is_palindrome(self, s, i, j):
        return s[i:j] == s[i:j][::-1]

Ex131 = Solution()
print(Ex131.is_palindrome('aba', 0, 2))
s = "aab"
print(Ex131.partition(s))
