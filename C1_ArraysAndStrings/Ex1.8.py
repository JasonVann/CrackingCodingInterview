import copy

def zero_matrix(matrix):
    # O(n^2) space
    #m2 = matrix[:][:]
    m2 = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                m2[i] = [0] * len(matrix[i])
                for k in range(len(matrix)):
                    m2[k][j] = 0
                break
    return m2

def zero_matrix2(matrix):
    # O(n) space
    #Avoid extra O(mn) space
    row = {}
    col = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if i not in row:
                    row[i] = 1
                if j not in col:
                    col[j] = 1
                break
    for i in row.keys():
        matrix[i] = [0] * len(matrix[i])
    for j in col.keys():
        for k in range(len(matrix)):
            matrix[k][j] = 0
    return matrix

# III. set 0's row & coln to -1, then 2nd pass to set to 0. O(1) space, O(n^2) time
def zero_matrix3(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                for m in range(len(matrix[i])):
                    if matrix[i][m] != 0:
                        matrix[i][m] = -1
                for n in range(len(matrix)):
                    if matrix[n][j] != 0:
                        matrix[n][j] = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix

matrix = [[1,0,2,3], [0,1,2,3], [1,2,3,4], [1,2,3,4]]
print(zero_matrix(matrix))
print(zero_matrix2(matrix))
print(zero_matrix3(matrix))
