'''Write an algorithm such that if an element in an m*n matrix is 0,
its entire row and column are set to 0.'''

def setZero(matrix):
    m = len(matrix)
    if m == 0:
        return matrix
    n = len(matrix[0])
    if n == 0:
        return matrix
    r = [1] * m
    c = [1] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                r[i] = 0
                c[j] = 0
    for p in range(len(r)):
        if r[p] == 0:
            for j in range(n):
                matrix[p][j] = 0
    for q in range(len(c)):
        if c[q] == 0:
            for i in range(m):
                matrix[i][q] = 0
    return matrix

if __name__ == '__main__':
    matrix = [[1,1,1,1,0],[1,1,1,2,3],[0,1,2,3,4],[1,2,3,0,4],[1,0,2,3,4],[1,2,3,4,5]]
    setZero(matrix)
    for row in matrix:
        print row            