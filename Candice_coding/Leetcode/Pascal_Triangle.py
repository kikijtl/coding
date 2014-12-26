def generate(numRows):
    T = []
    for i in range(numRows):
        T.append([1]*(i+1))
    for i in range(1, numRows):
        for j in range(1, i):
            T[i][j] = T[i-1][j] + T[i-1][j-1]    
    return T

def getRow(rowIndex):
    T = []
    for i in range(rowIndex+1):
        T.append([1]*(i+1))
    for i in range(1, rowIndex+1):
        for j in range(1, i):
            T[i][j] = T[i-1][j-1] + T[i-1][j]
    return T[rowIndex]


if __name__ == '__main__':
    numRows = 5
    print generate(numRows)
    rowIndex = 3
    print getRow(rowIndex)