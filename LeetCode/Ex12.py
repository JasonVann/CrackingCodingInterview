class Ex12(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ref = {}
        ref[1] = 'I'
        ref[5] = 'V'
        ref[10] = 'X'
        ref[50] = 'L'
        ref[100] = 'C'
        ref[500] = 'D'
        ref[1000] = 'M'
        ref[900] = 'CM'
        ref[400] = 'CD'
        ref[90] = 'XC'
        ref[40] = 'XL'
        ref[9] = 'IX'
        ref[4] = 'IV'
        
        res = ''
        all = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        while num > 0:
            #print num, all
            if num >= all[0]:
                res += ref[all[0]]
                num -= all[0]
                #all = all[1:]
            '''
            elif num > all[0] * 0.8: #92
                temp = all[0] - num / 10 * 10
                print 'b', temp, num, all
                res += ref[temp]
                num += temp
                num -= all[0]
                res += ref[all[0]]
                #all = all[1:]
            '''
            if len(all) > 1 and num < all[0]:
                all = all[1:]
        return res
        
ex12 = Ex12()
print ex12.intToRoman(2457)
