# Ex383
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for m in magazine:
            dic[m] = dic.get(m, 0) + 1
        for m in ransomNote:
            if m not in dic:
                return False
            dic[m] = dic.get(m, 0) - 1
            if dic[m] < 0:
                return False
        return True
