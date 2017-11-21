class Ex8(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = 0
        pre = 1
        seen_sign = False
        seen_num = False
        for i in range(len(str)):
            if str[i] == ' ' and not (seen_num or seen_sign):
                continue
            if str[i] == ' ' and (seen_num or seen_sign):
                break
            if ord(str[i]) >= 48 and ord(str[i]) <= 57:
                temp = int(str[i])
                res = res * 10 + temp
                seen_num = True
            elif str[i] == '-' and res == 0 and not seen_sign:
                pre = -1
                seen_sign = True
            elif str[i] == '+' and res == 0 and not seen_sign:
                pre = 1
                seen_sign = True
            else:
                break
        res = res * pre
        if res < 0 and res < -2**31:
            return -2**31
        if res > 0 and res > 2**31 - 1:
            return 2**31-1
        return res
    '''
    public String longestPalindrome(String s) {
        if (s.isEmpty()) return "";
        if (s.length() == 1) return s;
        int min_start = 0, max_len = 1;
        for (int i = 0; i < s.length(); ) {
            if (s.length() - i <= max_len / 2) break;
            int j = i, k = i;
            while (k < s.length() - 1 && s.charAt(k + 1) == s.charAt(k)) ++k; // Skip duplicate characters.
            i = k + 1;
            while (k < s.length() - 1 && j > 0 && s.charAt(k + 1) == s.charAt(j - 1)) {
                ++k;
                --j;
            } // Expand.
            int new_len = k - j + 1;
            if (new_len > max_len) {
                min_start = j;
                max_len = new_len;
            }
        }
        return s.substring(min_start, min_start + max_len);
    }
    '''
        
ex8 = Ex8()
print 8, ex8.myAtoi('  -8')
print 8, ex8.myAtoi('8')
print 8, ex8.myAtoi('  ')
print 8, ex8.myAtoi(' -8a')
print 8, ex8.myAtoi("2147483648")
