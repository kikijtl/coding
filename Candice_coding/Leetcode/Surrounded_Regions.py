# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# 
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
# 
# X X X X
# X X X X
# X X X X
# X O X X


import collections

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        visited = {}
        for i in xrange(m):
            if board[i][0] == 'O' and (i, 0) not in visited:
                self._markVisited(i, 0, board, visited)
            if board[i][n-1] == 'O' and (i, n-1) not in visited:
                self._markVisited(i, n-1, board, visited)
        for j in xrange(n):
            if board[0][j] == 'O' and (0, j) not in visited:
                self._markVisited(0, j, board, visited)
            if board[m-1][j] == 'O' and (m-1, j) not in visited:
                self._markVisited(m-1, j, board, visited)
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
        
    def _markVisited(self, x, y, board, visited):
        visited[(x, y)] = True
        q = collections.deque([(x, y)])
        while q:
            i, j = q.popleft()
            if i > 0 and board[i-1][j] == 'O' and (i-1, j) not in visited:
                visited[(i-1, j)] = True
                q.append((i-1, j))
            if i < len(board)-1 and board[i+1][j] == 'O' and (i+1, j) not in visited:
                visited[(i+1, j)] = True
                q.append((i+1, j))
            if j > 0 and board[i][j-1] == 'O' and (i, j-1) not in visited:
                visited[(i, j-1)] = True
                q.append((i, j-1))
            if j < len(board[0])-1 and board[i][j+1] == 'O' and (i, j+1) not in visited:
                visited[(i, j+1)] = True
                q.append((i, j+1))


if __name__ == '__main__':
    board = ["XOOOOOOOOOOOOOOOOOOO",
             "OXOOOOXOOOOOOOOOOOXX",
             "OOOOOOOOXOOOOOOOOOOX",
             "OOXOOOOOOOOOOOOOOOXO",
             "OOOOOXOOOOXOOOOOXOOX",
             "XOOOXOOOOOXOXOXOXOXO",
             "OOOOXOOXOOOOOXOOXOOO",
             "XOOOXXXOXOOOOXXOXOOO",
             "OOOOOXXXXOOOOXOOXOOO",
             "XOOOOXOOOOOOXXOOXOOX",
             "OOOOOOOOOOXOOXOOOXOX",
             "OOOOXOXOOXXOOOOOXOOO",
             "XXOOOOOXOOOOOOOOOOOO",
             "OXOXOOOXOXOOOXOXOXOO",
             "OOXOOOOOOOXOOOOOXOXO",
             "XXOOOOOOOOXOXXOOOXOO",
             "OOXOOOOOOOXOOXOXOXOO",
             "OOOXOOOOOXXXOOXOOOXO",
             "OOOOOOOOOOOOOOOOOOOO",
             "XOOOOXOOOXXOOXOXOXOO"]
    for i in xrange(len(board)):
        board[i] = list(board[i])
    Solution().solve(board)
    print board