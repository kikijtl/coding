# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
# 
# For example:
# 
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# 
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
# 
# Hint:
# 
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?
# According to the definition of tree on Wikipedia: ¡°a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.¡±
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.


class GraphNode(object):
    def __init__(self, val):
        self.val = val
        self.neighbors = sets.Set([])

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # The question actually is to check if there is a loop in the graph
        node_tb = {}
        for i in xrange(n):
            node_tb[i] = GraphNode(i)
        for edge in edges:
            node_tb[edge[0]].neighbors.add(edge[1])
            node_tb[edge[1]].neighbors.add(edge[0])
        visited = sets.Set([0])
        loop = self._validTreeHelper(0, node_tb, visited)
        if loop: return False
        else: return len(visited) == n
    
    def _validTreeHelper(self, start, node_tb, visited):
        ''' Used to check if there is a loop in the graph'''
        visited.add(start)
        node = node_tb[start]
        for neighbor in node.neighbors:
            if neighbor in visited:
                return True
            else:
                node_tb[neighbor].neighbors.remove(start)
                loop = self._validTreeHelper(neighbor, node_tb, visited)
                if loop: return True
        return False
        