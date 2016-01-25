# Given an integer matrix, find the length of the longest increasing path.
# 
# From each cell, you can either move to four directions: left, right, up or down.
# You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
# 
# Example 1:
# 
# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Return 4
# The longest increasing path is [1, 2, 6, 9].
# 
# Example 2:
# 
# nums = [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Return 4
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

# DFS with memorization

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        memorize = [[0 for i in xrange(n)] for j in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                self.longestIncreasingPathDfs(matrix, i, j, memorize)
        return max([max(row) for row in memorize])
    
    def longestIncreasingPathDfs(self, matrix, i, j, memorize):
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) \
                or matrix[x][y] <= matrix[i][j]:
                continue
            if not memorize[x][y]:
                self.longestIncreasingPathDfs(matrix, x, y, memorize)
            memorize[i][j] = max(memorize[x][y] + 1, memorize[i][j])
        memorize[i][j] = max(memorize[i][j], 1)
        
            
if __name__ == '__main__':
    matrix = [[7,7,5],[2,4,6],[8,2,0]]
    print Solution().longestIncreasingPath(matrix)