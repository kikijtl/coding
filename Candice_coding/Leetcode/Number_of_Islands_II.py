# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# 
# Example:
# 
# Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
# 
# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
# 
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
# 
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
# 
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
# 
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# We return the result as an array: [1, 1, 2, 3]
# 
# Challenge:
# 
# Can you do it in time complexity O(k log mn), where k is the length of the positions?


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # Use Union-Find
        islands = []
        count = 0
        rootMap = {}
        grid = [[0 for j in xrange(n)] for i in xrange(m)]
        for position in positions:
            count += 1
            grid[position[0]][position[1]] = 1
            node = (position[0], position[1])
            rootMap[node] = node
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for x, y in directions:
                neighbor = (position[0]+x, position[1]+y)
                if 0 <= neighbor[0] < m and 0 <= neighbor[1] < n and neighbor in rootMap:
                    neighborRoot = self._findRoot(neighbor, rootMap)
                    nodeRoot = self._findRoot((position[0], position[1]), rootMap)
                    if neighborRoot != nodeRoot:
                        count -= 1
                        self._unionIslands(nodeRoot, neighborRoot, rootMap)
            islands.append(count)
        return islands
    
    def _findRoot(self, node, rootMap):
        while rootMap[node] != node:
            rootMap[node] = rootMap[rootMap[node]]  # path compression
            node = rootMap[node]
        return node
    
    def _unionIslands(self, root1, root2, rootMap):
        rootMap[root2] = root1