class Ex240(object):       
    def search(self, row, target):
        lo = 0
        hi = len(row) - 1
        while lo <= hi:
            mid = (lo+hi)/2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
        
    def searchMatrix0(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """   
        # O(nlogn)
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if matrix[0][0] > target or matrix[m-1][n-1] < target:
            return False
        for i in range(m):
            row = matrix[i]
            res = self.search(row, target)
            if res:
                return True
        return False
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """   
        # Minor Optimization
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if matrix[0][0] > target or matrix[m-1][n-1] < target:
            return False
        lo = 0
        hi = m - 1
        while lo < hi:
            last_lo = lo
            last_hi = hi
            mid = (lo+hi)/2
            if matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] < target:
                lo = mid + 1
            if matrix[mid][0] > target:
                hi = mid - 1
            if last_lo == lo and last_hi == hi:
                break
        for i in range(lo, hi+1):
            row = matrix[i]
            res = self.search(row, target)
            if res:
                return True 
        return False
    '''
    public class Solution {
        public boolean searchMatrix(int[][] matrix, int target) {
            if(matrix == null || matrix.length < 1 || matrix[0].length <1) {
                return false;
            }
            int col = matrix[0].length-1;
            int row = 0;
            while(col >= 0 && row <= matrix.length-1) {
                if(target == matrix[row][col]) {
                    return true;
                } else if(target < matrix[row][col]) {
                    col--;
                } else if(target > matrix[row][col]) {
                    row++;
                }
            }
            return false;
        }
    }
    '''
    '''
    # T(nxn) = O(n^log3)
    # Each time get rid 1 block out of 4
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        if(m<1) return false;
        int n = matrix[0].length;
        
        return searchMatrix(matrix, new int[]{0,0}, new int[]{m-1, n-1}, target);
    }

    private boolean searchMatrix(int[][] matrix, int[] upperLeft, int[] lowerRight, int target) {
        if(upperLeft[0]>lowerRight[0] || upperLeft[1]>lowerRight[1]
                || lowerRight[0]>=matrix.length || lowerRight[1]>=matrix[0].length) 
            return false;
        if(lowerRight[0]-upperLeft[0]==0 && lowerRight[1]-upperLeft[1]==0)
            return matrix[upperLeft[0]][upperLeft[1]] == target;
        int rowMid = (upperLeft[0] + lowerRight[0]) >> 1;
        int colMid = (upperLeft[1] + lowerRight[1]) >> 1;
        int diff = matrix[rowMid][colMid] - target;
        if(diff > 0) {
            return searchMatrix(matrix, upperLeft, new int[]{rowMid, colMid}, target)
                    || searchMatrix(matrix, new int[]{upperLeft[0],colMid+1}, new int[]{rowMid, lowerRight[1]}, target)
                    || searchMatrix(matrix, new int[]{rowMid+1,upperLeft[1]}, new int[]{lowerRight[0], colMid}, target);
        }
        else if(diff < 0) {
            return searchMatrix(matrix, new int[]{upperLeft[0], colMid+1}, new int[]{rowMid, lowerRight[1]}, target)
                    || searchMatrix(matrix, new int[]{rowMid+1, upperLeft[1]}, new int[]{lowerRight[0], colMid}, target)
                    || searchMatrix(matrix, new int[]{rowMid+1, colMid+1}, lowerRight, target);
        }
        else return true;
    }
    '''

