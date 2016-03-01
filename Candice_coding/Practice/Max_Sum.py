# Given an array of integers, write a function to return the maximum sum with following constraints: 
# you cannot add two adjacent integers together. 
# Explain the running time too.
# Google engineering residency program

def maxSum(A):
    n = len(A)
    if n <= 2:
        return max(A)
    dp = [-float('inf')] * n
    dp[0] = A[0]
    dp[1] = max(A[1], A[0])
    for i in xrange(2, n):
        dp[i] = max(dp[i-2]+A[i], dp[i-1])
    return max(dp)


if __name__ == '__main__':
    tests = [[0], [1,2], [-1,0,1,2], [1,-1,0,2,-1,-1,3,2], [1,-1,-1,0,-1], [2,1,1,-1,-2]]
    for A in tests:
        print A, maxSum(A)