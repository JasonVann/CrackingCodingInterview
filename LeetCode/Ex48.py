class Ex48(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        n = len(matrix[0])
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            for j in range(0, n/2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
        return
    '''???
    def rotate(self, A):
        A[:] = zip(*A[::-1])
        // A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]
    '''

