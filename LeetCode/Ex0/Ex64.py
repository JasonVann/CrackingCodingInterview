class Ex64(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        #pre = [0] * n # pad one line above
        pre = grid[0][:]
        for j in range(1, n):
            pre[i] = pre[i] + pre[i-1]
            
        pre[0] = grid[0][0]
        cur = pre[:]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    cur[0] = pre[0] + grid[i][j]
                else:
                    a = cur[j-1] + grid[i][j]
                    b = pre[j-1] + grid[i][j]
                    cur[j] = min(a, b)
                    print 300, a, b, cur[j-1], pre[j], grid[i][j]
            pre, cur = cur, pre
        return pre[-1]
    '''
    class Solution {
    public:
        int minPathSum(vector<vector<int>>& grid) {
            int m = grid.size();
            int n = grid[0].size();
            vector<int> cur(m, grid[0][0]);
            for (int i = 1; i < m; i++)
                cur[i] = cur[i - 1] + grid[i][0]; 
            for (int j = 1; j < n; j++) {
                cur[0] += grid[0][j]; 
                for (int i = 1; i < m; i++)
                    cur[i] = min(cur[i - 1], cur[i]) + grid[i][j];
            }
            return cur[m - 1];
        }
    };
    '''

