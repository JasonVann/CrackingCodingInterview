class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        carry = 0
        for i in range(-1, -len(num1) - 1, -1):
            s1 = num1[i]
            if i < -len(num2):
                s2 = "0"
            else:
                s2 = num2[i]
            s1 = ord(s1) - 48
            s2 = ord(s2) - 48
            cur = s1 + s2 + carry
            if cur >= 10:
                carry = 1
                cur = cur - 10
            else:
                carry = 0
            res = res + cur * 10 ** (abs(i) - 1)
        if carry == 1:
            res = res + carry * 10 ** abs(i)
        return str(res)
