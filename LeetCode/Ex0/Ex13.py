class Ex13(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ref = {}
        ref['I'] = 1
        ref['V'] = 5
        ref['X'] = 10
        ref['L'] = 50
        ref['C'] = 100
        ref['D'] = 500
        ref['M'] = 1000
        
        res = 0
        #print ref
        for a in range(len(s) - 1):
            if ref[s[a]] < ref[s[a+1]]:
               res -= ref[s[a]]
            else:
                res += ref[s[a]]
        return res + ref[s[-1]]
ex13 = Ex13()
print ex13.romanToInt('MMDCCCLXXIX')
print ex13.romanToInt('MMCMLXXIX')
