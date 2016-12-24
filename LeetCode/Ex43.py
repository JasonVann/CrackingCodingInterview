class Ex43(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #from collections import deque
        if num1 == '0' or num2 == '0':
            return '0'
        res = []
        m = len(num1)
        n = len(num2)
        if m < n:
            num1, num2 = num2, num1
            m, n = n, m
        carry = 0
        row = []
        last_row = '0' * m
        for b1 in range(len(num2)-1, -1, -1):
            row = []
            carry = 0
            print 72, num1, last_row
            for a1 in range(len(num1) - 1, -1, -1):
                #print 71, b1, a1, '9'
                b = num2[b1]
                a = num1[a1]
                idx_c = a1 - len(num1)
                if idx_c >= -len(last_row):
                    c = last_row[idx_c]
                else:
                    c = '0'
                print 76, a, b, c, a1, last_row
                j = ord(b) - ord('0')
                i = ord(a) - ord('0')
                k = ord(c) - ord('0')
                temp = j * i + k + carry
                print 83, i, j, k, carry, temp
                temp, carry = temp % 10, temp / 10
                
                row.append(str(temp))
            if carry >= 1:
                row.append(str(carry))
            row = row[::-1]
            print 88, res, row, last_row
            res.append(row[-1])
            last_row = row[:-1]
            print 90, res, row, last_row
            
            
        res = row[:-1] + res[::-1]
        
        return ''.join(res)
    '''
    !!! `num1[i] * num2[j]` will be placed at indices `[i + j`, `i + j + 1]` 
    Multiplication

    public String multiply(String num1, String num2) {
        int m = num1.length(), n = num2.length();
        int[] pos = new int[m + n];
       
        for(int i = m - 1; i >= 0; i--) {
            for(int j = n - 1; j >= 0; j--) {
                int mul = (num1.charAt(i) - '0') * (num2.charAt(j) - '0'); 
                int p1 = i + j, p2 = i + j + 1;
                int sum = mul + pos[p2];

                pos[p1] += sum / 10;
                pos[p2] = (sum) % 10;
            }
        }  
        
        StringBuilder sb = new StringBuilder();
        for(int p : pos) if(!(sb.length() == 0 && p == 0)) sb.append(p);
        return sb.length() == 0 ? "0" : sb.toString();
    }
    '''
    
ex43 = Ex43()
n1 = '999'
n2 = '9876'
print 43, ex43.multiply(n1, n2)

