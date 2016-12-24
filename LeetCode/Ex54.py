class Ex54(object):
    def iter(self, matrix, i, res):
        if i >= len(matrix) - i or i >= len(matrix[0]) - i:
            return
            
        row1, row2, row3, row4 = [], [], [], []
        row = matrix[0]
        row1 += matrix[i][i:len(matrix[0]) - i]
        print 61, 'row1', row1
        for j in range(i+1, len(matrix) - i - 1):
            row = matrix[j]
            print 64, row, i, len(row) - i - 1
            if len(row) - i - 1 >= 0:
                row2.append(row[len(row) - i - 1])
            if i < len(row) - i - 1:
                row4.append(row[i])
        print 68, 'row2', row2
        if i != len(matrix) - i - 1:
            row3 += matrix[len(matrix) - i - 1][i:len(row) - i][::-1]
        row4 = row4[::-1]
        print 72, 'row3', row3
        print 73, 'row4', row4
        res += row1 + row2 + row3 + row4
        print 68, res, i, row1, row2, row3, row4
        return self.iter(matrix, i+1, res)
                
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        print 82, len(matrix)
        self.iter(matrix, 0, res)
        return res
    '''    
    public class Solution {
        public List<Integer> spiralOrder(int[][] matrix) {
            
            List<Integer> res = new ArrayList<Integer>();
            
            if (matrix.length == 0) {
                return res;
            }
            
            int rowBegin = 0;
            int rowEnd = matrix.length-1;
            int colBegin = 0;
            int colEnd = matrix[0].length - 1;
            
            while (rowBegin <= rowEnd && colBegin <= colEnd) {
                // Traverse Right
                for (int j = colBegin; j <= colEnd; j ++) {
                    res.add(matrix[rowBegin][j]);
                }
                rowBegin++;
                
                // Traverse Down
                for (int j = rowBegin; j <= rowEnd; j ++) {
                    res.add(matrix[j][colEnd]);
                }
                colEnd--;
                
                if (rowBegin <= rowEnd) {
                    // Traverse Left
                    for (int j = colEnd; j >= colBegin; j --) {
                        res.add(matrix[rowEnd][j]);
                    }
                }
                rowEnd--;
                
                if (colBegin <= colEnd) {
                    // Traver Up
                    for (int j = rowEnd; j >= rowBegin; j --) {
                        res.add(matrix[j][colBegin]);
                    }
                }
                colBegin ++;
            }
            
            return res;
        }
    }
    '''
    '''
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<vector<int> > dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        vector<int> res;
        int nr = matrix.size();     if (nr == 0) return res;
        int nc = matrix[0].size();  if (nc == 0) return res;
        
        vector<int> nSteps{nc, nr-1};
        
        int iDir = 0;   // index of direction.
        int ir = 0, ic = -1;    // initial position
        while (nSteps[iDir%2]) {
            for (int i = 0; i < nSteps[iDir%2]; ++i) {
                ir += dirs[iDir][0]; ic += dirs[iDir][1];
                res.push_back(matrix[ir][ic]);
            }
            nSteps[iDir%2]--;
            iDir = (iDir + 1) % 4;
        }
        return res;
    }
    '''
    
ex54 = Ex54()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

matrix = [[7],[9],[6]]
matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
matrix = [[7,9,6]]
matrix = [[2,5,8],[4,0,-1]]
print 54, ex54.spiralOrder(matrix)

