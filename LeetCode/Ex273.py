class Ex273(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {}
        dic[1] = 'one'
        dic[2] = 'two'
        dic[3] = 'three'
        dic[4] = 'four'
        dic[5] = 'five'
        dic[6] = 'six'
        dic[7] = 'seven'
        dic[8] = 'eight'
        dic[9] = 'nine'
        dic[10] = 'ten'
        dic[11] = 'eleven'
        dic[12] = 'twelve'
        dic[13] = 'thirteen'
        dic[14] = 'fourteen'
        dic[15] = 'fifteen'
        dic[16] = 'sixteen'
        dic[17] = 'seventeen'
        dic[18] = 'eighteen'
        dic[19] = 'nineteen'
        dic[20] = 'twenty'
        dic[30] = 'thirty'
        dic[40] = 'forty'
        dic[50] = 'fifty'
        dic[60] = 'sixty'
        dic[70] = 'seventy'
        dic[80] = 'eighty'
        dic[90] = 'ninety'
        dic[100] = 'hundred'
        dic[1000] = 'thousand'
        dic[1000000] = 'million'
        dic[1000000000] = 'billion'
        all = sorted(dic.keys(), reverse = True)
        #print all
        res = ''
        if num == 0:
            return 'Zero'
        while num > 0:
            #print num, all, res
            temp = ''
            if num >= all[0]:
                n = num / all[0]
                if str(all[0])[0] == '1' and all[0] >= 19: # and (n >= 100 or all[0] >= 100): # If > 10, need 'one' 
                    if n not in dic.keys():
                        temp = self.numberToWords(n)
                    else:
                        if all[0] >= 100 and n >= 100:
                            temp = 'one' + ' '
                        temp += dic[n]
                    res = res + temp + ' '
                #print 'b', num, all, res, n
                res = res + dic[all[0]] + ' '
                num -= n * all[0]
            all.pop(0)            
        res = res.title()
        return res.strip()
        
ex273 = Ex273()
print 273, ex273.numberToWords(12345)
print 273, ex273.numberToWords(100000)
print 273, ex273.numberToWords(123)
print 273, ex273.numberToWords(1234567891)
print 273, ex273.numberToWords(50868)
