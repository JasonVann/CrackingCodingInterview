class Ex62(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        A = []
        for i in range(m):
            A.append([0] * n)
            A[i][0] = 1
        A[0] = [1] * n                
        for i in range(1, m):
            for j in range(1, n):
                A[i][j] = A[i][j-1] + A[i-1][j]
        return A[-1][-1]
    '''
    class Solution {
        int uniquePaths(int m, int n) {
            if (m > n) return uniquePaths(n, m);
            vector<int> cur(m, 1);
            for (int j = 1; j < n; j++)
                for (int i = 1; i < m; i++)
                    cur[i] += cur[i - 1]; 
            return cur[m - 1];
        }
    }; 
    '''
    '''
    Binomial coefficient:
    # (n - 1) movements from (m + n-2).
    class Solution {
        public:
            int uniquePaths(int m, int n) {
                int N = n + m - 2;// how much steps we need to do
                int k = m - 1; // number of steps that need to go down
                double res = 1;
                // here we calculate the total possible path number 
                // Combination(N, k) = n! / (k!(n - k)!)
                // reduce the numerator and denominator and get
                // C = ( (n - k + 1) * (n - k + 2) * ... * n ) / k!
                for (int i = 1; i <= k; i++)
                    res = res * (N - k + i) / i;
                return (int)res;
            }
        };
    '''
    '''
    def uniquePaths(self, m, n):
        return reduce(lambda res, i: res * (n - 1 + i) / i, range(1, m), 1)
    '''    

