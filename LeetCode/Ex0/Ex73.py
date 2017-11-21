class Ex73(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                if matrix[i][j] == 0:
                    #print 64, matrix, i, j
                    for k in range(len(row)):
                        if matrix[i][k] != 0:
                            matrix[i][k] = None
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = None
                    #print 67, matrix
        #print matrix
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
        return
    '''
    void setZeroes(vector<vector<int> > &matrix) {
        int col0 = 1, rows = matrix.size(), cols = matrix[0].size();

        for (int i = 0; i < rows; i++) {
            if (matrix[i][0] == 0) col0 = 0;
            for (int j = 1; j < cols; j++)
                if (matrix[i][j] == 0)
                    matrix[i][0] = matrix[0][j] = 0;
        }

        for (int i = rows - 1; i >= 0; i--) {
            for (int j = cols - 1; j >= 1; j--)
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            if (col0 == 0) matrix[i][0] = 0;
        }
    }
    '''
    
ex73 = Ex73()
matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]

print 73, ex73.setZeroes(matrix)

