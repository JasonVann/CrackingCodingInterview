class Ex74(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """        
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        r1 = 0
        r2 = m - 1
        c1 = 0
        c2 = n - 1
        while True:            
            r = (r1+r2)/2
            c = (c1+c2)/2
            print 75, r, c, matrix[r][c], r1, r2, c1, c2
            if r1 > r2 or c1 > c2 or c1 >= n or r1 >= m or r < 0 or c < 0:
                return False
            
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                if c1 >= c2 or c == n - 1:
                    r1 = r + 1
                    c1 = 0
                    c2 = n - 1
                else:
                    c1 = c + 1
            else:
                if c1 >= c2 or c == 0:
                    r2 = r - 1
                    c1 = 0
                    c2 = n - 1
                else:
                    c2 = c - 1
        return False
    '''
    class Solution {
    public:
        bool searchMatrix(vector<vector<int> > &matrix, int target) {
            int n = matrix.size();
            int m = matrix[0].size();
            int l = 0, r = m * n - 1;
            while (l != r){
                int mid = (l + r - 1) >> 1;
                if (matrix[mid / m][mid % m] < target)
                    l = mid + 1;
                else 
                    r = mid;
            }
            return matrix[r / m][r % m] == target;
        }
    };
    '''
    
ex74 = Ex74()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
t = 4
matrix = [[1],[3]]
t = 1
matrix = [[1]]
t = 0
matrix = [[1],[3]]
t = 3
matrix = [[1,3]]
t = 3
matrix = [[-10,-10],[-9,-9],[-8,-6],[-4,-2],[0,1],[3,3],[5,5],[6,8]]
t = 0
print 74, ex74.searchMatrix(matrix, t)
