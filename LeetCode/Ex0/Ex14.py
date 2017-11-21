class Ex14(object):
    def Compare2(self, str1, str2):
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        res = ''
        for i in range(len(str2)):
            if str1[i] == str2[i]:
                res += str1[i]
            else:
                break
        return res
        
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        res = strs[0]
        for i in range(1, len(strs)):
            res = self.Compare2(res, strs[i])
            if len(res) == 0:
                return ''
        return res

