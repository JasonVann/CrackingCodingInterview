class Ex85(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # UL, UR, LL, LR
        dic_l = {} # left
        dic_a = {} # above
        print 61, len(matrix), len(matrix[0])
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        A = []
        res = []
        max_a = 0
        dic = {}
        for i in range(m):
            res.append([0]*n)
        res[0][0] = int(matrix[0][0])
        if int(matrix[0][0]) == 0:
            dic[(0, 0)] = (0, 0)
        else:
            dic[(0, 0)] = (1, 1)
        # 1st row
        for j in range(1, n):
            (w, h) = dic[(0, j-1)]   
            if int(matrix[0][j]):
                w = w + int(matrix[0][j])
            else:
                w = 0
            dic[(0, j)] = (w, h)
            res[0][j] = w * h
        # 1st column
        for j in range(1, m):
            (w, h) = dic[(j-1, 0)]
            if int(matrix[j][0]):
                h += int(matrix[j][0])
            else:
                h = 0
            dic[(j, 0)] = (w, h)
            res[j][0] = w * h
            
        for i in range(1, m):
            for j in range(1, n):
                if int(matrix[i][j]) == 0:
                    res[i][j] = 0
                    dic[(i, j)] = (0,0) #w, h
                    continue
                (w0, h0) = dic[(i-1, j-1)]
                (wa, ha) = dic[(i-1, j)] # above
                (wl, hl) = dic[(i, j-1)] # left
                
                if int(matrix[i-1][j]) == 0:
                    (w, h) = dic[(i, j-1)] # Then look left
                    h = 1
                    dic[(i, j)] = (w+1, h)
                    res[i][j] = (w+1) * h
                elif int(matrix[i][j-1]) == 0:
                    (w, h) = dic[(i-1, j)] # Then look up
                    w = 1
                    dic[(i, j)] = (w, h+1)
                    res[i][j] = w * (h+1)
                elif int(matrix[i-1][j-1]) == 0:
                    if res[i][j-1] >= res[i-1][j]:
                        pass
                else:                 
                    if h0 <= ha:
                        h1 = (h0+1)
                    else:
                        h1 = ha+1
                    if w0 <= wa:
                        w1 = w0+1
                    else:
                        w1 = wa+1
                    a1 = w1*h1
                    if wa <= wl + 1:
                        w2 = wa
                        h2 = (ha+1)
                    else:
                        w2 = (wl+1)
                        h2 = (ha+1)
                    a2 = w2*h2
                    if hl <= ha + 1:
                        w3 = (wa+1)
                        h3 = hl
                    else:
                        w3 = (wa+1)
                        h3 = (ha+1)
                    a3 = w3 * h3
                    if a1 > a2 and a1 > a3:
                        res[i][j] = a1
                        dic[(i, j)] = (w1, h1)
                    elif a2 > a1 and a2 > a3:
                        res[i][j] = a2
                        dic[(i, j)] = (wa, ha)
                    else:
                        res[i][j] = a3
                        dic[(i, j)] = (wl, hl)
                    print 151, (i, j), a1, a2, a3, (w1, h1), (w2, h2), (w3, h3)
                if res[i][j] > max_a:
                    max_a = res[i][j]
        print 156, res, dic, max_a
        return max_a
        
    def maximalRectangle0(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # UL, UR, LL, LR
        dic = {}
        print 61, len(matrix), len(matrix[0])
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        A = []
        res = []
        max_a = 0
        dic = {}
        for i in range(m):
            res.append([0]*n)
        res[0][0] = int(matrix[0][0])
        if int(matrix[0][0]) == 0:
            dic[(0, 0)] = (0, 0)
        else:
            dic[(0, 0)] = (1, 1)
        # 1st row
        for j in range(1, n):
            (w, h) = dic[(0, j-1)]   
            if int(matrix[0][j]):
                w = w + int(matrix[0][j])
            else:
                w = 0
            dic[(0, j)] = (w, h)
            res[0][j] = w * h
        # 1st column
        for j in range(1, m):
            (w, h) = dic[(j-1, 0)]
            if int(matrix[j][0]):
                h += int(matrix[j][0])
            else:
                h = 0
            dic[(j, 0)] = (w, h)
            res[j][0] = w * h
            
        for i in range(1, m):
            for j in range(1, n):
                if int(matrix[i][j]) == 0:
                    res[i][j] = 0
                    dic[(i, j)] = (0,0) #w, h
                    continue
                (w0, h0) = dic[(i-1, j-1)]
                (wa, ha) = dic[(i-1, j)] # above
                (wl, hl) = dic[(i, j-1)] # left
                
                if int(matrix[i-1][j]) == 0:
                    (w, h) = dic[(i, j-1)] # Then look left
                    h = 1
                    dic[(i, j)] = (w+1, h)
                    res[i][j] = (w+1) * h
                elif int(matrix[i][j-1]) == 0:
                    (w, h) = dic[(i-1, j)] # Then look up
                    w = 1
                    dic[(i, j)] = (w, h+1)
                    res[i][j] = w * (h+1)
                elif int(matrix[i-1][j-1]) == 0:
                    if res[i][j-1] >= res[i-1][j]:
                        pass
                else:
                #if 1:                    
                    if h0 <= ha:
                        h1 = (h0+1)
                    else:
                        h1 = ha+1
                    if w0 <= wa:
                        w1 = w0+1
                    else:
                        w1 = wa+1
                    a1 = w1*h1
                    if wa <= wl + 1:
                        w2 = wa
                        h2 = (ha+1)
                    else:
                        w2 = (wl+1)
                        h2 = (ha+1)
                    a2 = w2*h2
                    if hl <= ha + 1:
                        w3 = (wa+1)
                        h3 = hl
                    else:
                        w3 = (wa+1)
                        h3 = (ha+1)
                    a3 = w3 * h3
                    if a1 > a2 and a1 > a3:
                        res[i][j] = a1
                        dic[(i, j)] = (w1, h1)
                    elif a2 > a1 and a2 > a3:
                        res[i][j] = a2
                        dic[(i, j)] = (wa, ha)
                    else:
                        res[i][j] = a3
                        dic[(i, j)] = (wl, hl)
                    print 151, (i, j), a1, a2, a3, (w1, h1), (w2, h2), (w3, h3)
                if res[i][j] > max_a:
                    max_a = res[i][j]
        print 156, res, dic, max_a
        return max_a
        
ex85 = Ex85()
#matirx = [[1, 0, 1, 0, 0],[1, 0, 1, 1, 1],[1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
matrix = ["10100","10111","11111","10010"]
print ex85.maximalRectangle(matrix)

