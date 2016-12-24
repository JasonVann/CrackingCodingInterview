class Ex118(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        i = 1
        cur = [1]
        all_arr = []
        all_arr.append(cur)
        while i < numRows:
            j = 0
            cur = []
            while j <= i:
                #print all_arr, cur, i, j
                if j == 0:
                    pl = 0
                else:
                    pl = all_arr[i-1][j-1]
                if j == i:
                    pr = 0
                else:
                    #print 1127, numRows, all_arr, cur, i, j
                    pr = all_arr[i-1][j]
                #print 1129, pl, pr, all_arr, cur, i, j
                cur.append(pl+pr)
                j += 1
            #print 1132, all_arr, cur
            all_arr.append(cur)
            i+=1
        return all_arr
        
    def generate2(self, numRows):
        if numRows==0:
            return []
        res=[[1],]
        for i in range(0,numRows-1):
            a = zip(res[i],res[i][1:])
            print a, res[i][1:]
            l=[sum(p) for p in list(zip(res[i],res[i][1:]))]
            l.insert(0,1)
            l.append(1)
            res.append(l)
        return res
    
ex118 = Ex118()
print 118, ex118.generate(5)
