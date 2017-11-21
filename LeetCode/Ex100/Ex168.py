class Ex168(object):
    def find_len(self, n):
        j = 0
        t = 0
        dic = {}
        arr = []
        while True:
            if 26**j < n:
                j += 1
                t += 26**j
                if j > 1:
                    dic['z'*j] = (dic['z'*(j-1)])+ 26**j
                else:
                    dic['z'*j] = 26**j 
                arr.append(dic['z'*j])
            else:
                break
        #print dic
        #print arr
        return arr
        
    def convertToTitle(self, n):
        arr = self.find_len(n)
        res = ''
        while n > 26:
            for i in range(1, len(arr)):
                if arr[i-1] < n and arr[i] >= n:
                    if (n-arr[i-1]) % arr[i-1] == 0:
                        temp = (n - arr[i-1])/(arr[i-1])
                    else:
                        #temp = (n - arr[i-1])/(arr[i-1]) + 1
                        temp = (n - arr[i-1])/(26**i) + 1
                    #temp = n/26
                    #print 816, 'n=',n, 'i=', i, 'temp=',temp, 'res=', res, arr    
                                      
                    res += chr(temp+64)
                    n -= 26 ** i * temp
                    break
            
        #print n, res
        if n > 0 and n <= 26: 
            res += chr(n+64)
        return res      
            
ex168 = Ex168()
#print 168, ex168.find_len(28)
#print 168, ex168.convertToTitle(6992)
#print 168, ex168.convertToTitle(24568)
