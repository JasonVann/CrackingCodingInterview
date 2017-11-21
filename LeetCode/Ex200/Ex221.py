class Ex221(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        A = []
        max_a = 0
        dic = {}
        if int(matrix[0][0]) == 0:
            dic[(0, 0)] = 0
        else:
            dic[(0, 0)] = 1
            max_a = 1
        # 1st row
        for j in range(1, n):
            w = dic[(0, j-1)]   
            if int(matrix[0][j]):
                #w = w + int(matrix[0][j])                
                w = 1
                max_a = 1
            else:
                w = 0
            dic[(0, j)] = w
        # 1st column
        for j in range(1, m):
            w = dic[(j-1, 0)]
            if int(matrix[j][0]):
                #h += int(matrix[j][0])
                h = 1
                max_a = 1
            else:
                h = 0
                w = 0
            dic[(j, 0)] = h
            
        for i in range(1, m):
            for j in range(1, n):
                if int(matrix[i][j]) == 0:
                    dic[(i, j)] = 0
                    continue
                w0 = dic[(i-1, j-1)]
                wa = dic[(i-1, j)] # above
                wl = dic[(i, j-1)] # left
                dic[(i, j)] = min(dic[(i-1, j)], dic[(i, j-1)], dic[(i-1, j-1)]) + 1
                if dic[(i,j)] > max_a:
                    max_a = dic[(i, j)] 
        return max_a ** 2
        
    def maximalSquare0(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
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
            max_a = 1
        # 1st row
        for j in range(1, n):
            (w, h) = dic[(0, j-1)]   
            if int(matrix[0][j]):
                w = w + int(matrix[0][j])
                h = 1
                max_a = 1
            else:
                w = 0
                h = 0
            dic[(0, j)] = (w, h)
            res[0][j] = w * h
        # 1st column
        for j in range(1, m):
            (w, h) = dic[(j-1, 0)]
            if int(matrix[j][0]):
                h += int(matrix[j][0])
                w = 1
                max_a = 1
            else:
                h = 0
                w = 0
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
                if int(matrix[i-1][j-1]) == 0 or int(matrix[i-1][j]) == 0 or int(matrix[i][j-1]) == 0:
                    res[i][j] = 1
                    dic[(i, j)] = (1,1)
                else:
                    if ha >= h0 and wl >= w0:
                        (w, h) = (w0 + 1, h0 + 1)
                        l = min(w, h)
                        res[i][j] = l * l
                        dic[(i, j)] = (l, l)
                    else:
                        w = min(wl, w0) + 1
                        h = min(ha, h0) + 1
                        l = min(w, h)
                        res[i][j] = l * l
                        dic[(i, j)] = (l, l)
                if res[i][j] > max_a:
                    max_a = res[i][j]
        return max_a
    '''
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size();
        if (!m) return 0;
        int n = matrix[0].size();
        vector<int> pre(m, 0);
        vector<int> cur(m, 0);
        int maxsize = 0;
        for (int i = 0; i < m; i++) {
            pre[i] = matrix[i][0] - '0';
            maxsize = max(maxsize, pre[i]);
        }
        for (int j = 1; j < n; j++) {
            cur[0] = matrix[0][j] - '0';
            maxsize = max(maxsize, cur[0]);
            for (int i = 1; i < m; i++) {
                if (matrix[i][j] == '1') {
                    cur[i] = min(cur[i - 1], min(pre[i - 1], pre[i])) + 1;
                    maxsize = max(maxsize, cur[i]);
                }
            }
            swap(pre, cur);
            fill(cur.begin(), cur.end(), 0);
        }
        return maxsize * maxsize;
    }
    '''
    '''
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        int m = matrix.size(), n = matrix[0].size();
        vector<int> dp(m + 1, 0);
        int maxsize = 0, pre = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 1; i <= m; i++) {
                int temp = dp[i];
                if (matrix[i - 1][j] == '1') {
                    dp[i] = min(dp[i], min(dp[i - 1], pre)) + 1;
                    maxsize = max(maxsize, dp[i]);
                }
                else dp[i] = 0; 
                pre = temp;
            }
        }
        return maxsize * maxsize;
    }
    '''

