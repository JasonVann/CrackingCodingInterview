class Ex6(object):        
    def fill_zero(self, arr, k, col):
        for i in range(len(arr)):
            if i != k:
                arr[i].append(0)                
                
    def convert2(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        row = []
        arr = []
        for i in range(numRows):
            arr.append([])
        row = 0
        col = 0
        down = True
        for i in s:
            #arr[row][col] = i
            #print 75, arr, row, col, down
            arr[row].append(i)
            if row == 0 and (not down):
                down = not down 
                if row < numRows - 1:
                    row += 1
            elif row < numRows - 1 and down:
                row += 1
            elif row == numRows - 1 and down:
                down = not down
                if (row > 0):
                    row -= 1
                col += 1
            else:
                # up
                #self.fill_zero(arr, row, col)
                if row > 0:
                    row -= 1
                col += 1
        '''
        for row in arr:
            for col in row:
                if col == '0':
                    #print ' '
                else:
                    #print col
        '''
        res = ''
        for i in arr:
            for j in i:
                if j != 0:
                    res += j
        print len(arr[0])
        return res
        
                
ex6 = Ex6()
s = 'ABC'
numRows = 1
s = "abcdefghijklmn"
numRows = 5
print 6, ex6.convert(s, numRows)

