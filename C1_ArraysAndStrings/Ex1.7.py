def rotate_matrix(matrix):
    # Assume rotate CCW 90 degree
    n = len(matrix)
    m2 = []
    for i in range(n):
        row = []
        for j in range(0, n):
            #matrix[i][j], matrix[n-j-1][i] = matrix[n-j-1][i], matrix[i][j]
            row.append(matrix[j][n-1-i])
        m2.append(row)
    return m2

def rotate_matrix2(matrix):
    # Assume rotate CCW 90 degree
    # In-place
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n/2):
        for j in range(n):
            matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]
    return matrix


matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
print rotate_matrix(matrix)
print rotate_matrix2(matrix)
