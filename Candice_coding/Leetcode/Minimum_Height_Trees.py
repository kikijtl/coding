# For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.
# 
# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).
# 
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
# 
# Example 1:
# 
# Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]
# 
#         0
#         |
#         1
#        / \
#       2   3
# return [1]
# 
# Example 2:
# 
# Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
# 
#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
# return [3, 4]
# 
# Hint:
# 
# How many MHTs can a graph have at most?
# Note:
# 
# (1) According to the definition of tree on Wikipedia: "a tree is an undirected graph in which any two vertices are connected by exactly one path.
# In other words, any connected graph without simple cycles is a tree."
# 
# (2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # if a node has only one neighbor, then it can be treated as a leaf.
        # The basic idea is "keep deleting leaves layer-by-layer, until reach the root."
        if n == 1: return [0]
        graph = {}
        for node1, node2 in edges:
            if node1 not in graph:
                graph[node1] = set([])
            if node2 not in graph:
                graph[node2] = set([])
            graph[node1].add(node2)
            graph[node2].add(node1)
        vertices = set(graph.keys())
        while len(graph) > 2:
            leaves = []
            for node in graph:
                if len(graph[node]) == 1:
                    leaves.append(node)
            for leaf in leaves:
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                graph.pop(leaf)
                vertices.remove(leaf)
        return list(vertices)


if __name__ == '__main__':
    n = 6
    edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]  
    print Solution().findMinHeightTrees(n, edges)              