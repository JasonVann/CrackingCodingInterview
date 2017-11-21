class Ex459(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        if len(str) <= 1:
            return False
        A0 = []
        for i in range(len(str)):
            if str[i] == str[0]:
                A0.append(i)
        
        for i in range(1, len(A0)):
            start = 0
            end = A0[i]
            if len(str) % (end - start) == 0:
                k = len(str) / (end - start)
                if str == str[start: end] * k:
                    return True
        return False

