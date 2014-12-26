'''Given a triangle, find the minimum path sum from top to bottom. 
    Each step you may move to adjacent numbers on the row below.'''
def minimumTotal(triangle):
    n = len(triangle)
    sum = [[0 for j in range(n)] for i in range(n)]
    '''
    Must use dynamic programming.
    Greedy method will return wrong answer.
    The recursive equation is:
    sum[i][j] = triangle[i][j] + min(sum[i+1][j],sum[i+1][j+1])
    '''
    for j in range(n):
        sum[n-1][j] = triangle[n-1][j]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            if sum[i+1][j] <= sum[i+1][j+1]:
                sum[i][j] = sum[i+1][j] + triangle[i][j]
            else:
                sum[i][j] = sum[i+1][j+1] + triangle[i][j]
    return sum[0][0]

def minimumTotal_lessSpace(triangle):
    n = len(triangle)
    sum = triangle[n-1]
    '''
    This method only use O(n) extra space
    '''
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            if sum[j] <= sum[j+1]:
                sum[j] += triangle[i][j]
            else:
                sum[j] = sum[j+1] + triangle[i][j]
    return sum[0]


if __name__ == '__main__':
    triangle = [[-1],[2,3],[1,-1,-3]]
    print minimumTotal(triangle)
    print minimumTotal_lessSpace(triangle)