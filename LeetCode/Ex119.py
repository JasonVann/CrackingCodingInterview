class Ex119(object):
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
        
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if rowIndex == 0:
            return [1]
        i = 1
        pre = [1]
        while i <= rowIndex:
            j = 0
            cur = []
            while j <= i:
                #print all_arr, cur, i, j
                if j == 0:
                    pl = 0
                else:
                    pl = pre[j-1]
                if j == i:
                    pr = 0
                else:
                    #print 1127, numRows, all_arr, cur, i, j
                    pr = pre[j]
                #print 1129, pl, pr, all_arr, cur, i, j
                cur.append(pl+pr)
                j += 1
            #print 1132, all_arr, cur
            pre = cur
            i+=1
        return cur
        
    def getRow2(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        all_arr = self.generate(rowIndex+1)
        #print all_arr
        return all_arr[-1]
    def getRow_Good(self, rowIndex):
        row = [1]
        for i in range(1, rowIndex+1):
            row = list(map(lambda x,y: x+y, [0]+row, row + [0]))
        return row
    '''
    # Based on fancy Math
    row k of Pascal's Triangle:

    [C(k,0), C(k,1), ..., C(k, k-1), C(k, k)]

    and

    C[k,i] = C[k,i-1]*(k-i+1)/i
    '''
    
ex119 = Ex119()
print 119, ex119.getRow(6)
