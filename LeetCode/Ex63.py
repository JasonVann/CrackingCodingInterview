class Ex63(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        A = []
        for i in range(m):
            cur = []
            found = False
            for j in range(n):
                if obstacleGrid[i][j] == 1 or (i == 0 and found):
                    cur.append(None)
                    found = True
                else:
                    if i == 0:
                        cur.append(1)
                    else:
                        cur.append(0)
            A.append(cur)
        
        found = False
        for i in range(m):
            if obstacleGrid[i][0] == 1 or found:
                found = True
                A[i][0] = None
            else:
                A[i][0] = 1
        #print 300, A
        for i in range(1, m):
            for j in range(1, n):
                if A[i][j] == None:
                    continue
                if A[i][j-1] == None:
                    A[i][j] = A[i-1][j]
                elif A[i-1][j] == None:
                    A[i][j] = A[i][j-1]
                else:
                    A[i][j] = A[i][j-1] + A[i-1][j]
        return 0 if A[-1][-1] == None else A[-1][-1]
    '''
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int width = obstacleGrid[0].length;
        int[] dp = new int[width];
        dp[0] = 1;
        for (int[] row : obstacleGrid) {
            for (int j = 0; j < width; j++) {
                if (row[j] == 1)
                    dp[j] = 0;
                else if (j > 0)
                    dp[j] += dp[j - 1];
            }
        }
        return dp[width - 1];
    }
    '''
    '''    
    class Solution {
    public:
        int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
            int m = obstacleGrid.size();
            int n = obstacleGrid[0].size();
            vector<int> cur(m, 0);
            for (int i = 0; i < m; i++) {
                if (!obstacleGrid[i][0])
                    cur[i] = 1;
                else break;
            }
            for (int j = 1; j < n; j++) {
                bool flag = false;
                if (obstacleGrid[0][j])
                    cur[0] = 0;
                else flag = true;
                for (int i = 1; i < m; i++) {
                    if (!obstacleGrid[i][j]) {
                        cur[i] += cur[i - 1]; 
                        if (cur[i]) flag = true;
                    }
                    else cur[i] = 0; 
                }
                if (!flag) return 0;
            }
            return cur[m - 1];
        }
    };
    '''

