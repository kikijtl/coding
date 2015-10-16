from sets import Set
from collections import deque


class GraphAdjMatrix(object):
    def __init__(self, vertex_num, directed=False):
        self.vertex_num = vertex_num
        self.vertex_ls = []
        self.directed = directed
        self.adj_matrix = [[0 for i in xrange(vertex_num)] for j in xrange(vertex_num)]
    
    def add_vertex(self, value):
        if len(self.vertex_ls) == self.vertex_num:
            print 'Error in adding vertex'
            return
        self.vertex_ls.append(value)
        
    def add_edge(self, start, end, weight=1):
        try:
            self.adj_matrix[start][end] = weight
        except:
            print 'Error'
            return
        if not self.directed:
            self.adj_matrix[end][start] = weight
    
    def dfs(self, source):
        visited = Set([])
        self._dfsHelper(source, visited)
        
    
    def _dfsHelper(self, source, visited):
        if source in visited: return
        visited.add(source)
        print source
        for i in xrange(self.vertex_num):
            if self.adj_matrix[source][i]:
                self._dfsHelper(i, visited)
                
    
    def bfs(self, source):
        visited = Set([])
        q = deque([])
        q.append(source)
        while q:
            tmp = q.popleft()
            if tmp in visited:
                continue
            visited.add(tmp)
            print tmp
            for i in xrange(self.vertex_num):
                if self.adj_matrix[tmp][i]:
                    q.append(i)        


    def findShortestPath_bfs(self, start, end):
        distance = [float('inf')] * self.vertex_num
        path = [end]
        parent = [start] * self.vertex_num
        q = deque([])
        visited = Set([])
        distance[start] = 0
        q.append(start)
        while q:
            tmp = q.popleft()
            if tmp in visited: continue
            visited.add(tmp)
            for i in xrange(self.vertex_num):
                if self.adj_matrix[tmp][i]:
                    q.append(i)
                    if distance[i] > distance[tmp] + 1:
                        distance[i] = distance[tmp] + 1
                        parent[i] = tmp
                    if i == end: break
        find_path = end
        while find_path != start:
            path.append(parent[find_path])
            find_path = parent[find_path]
        path.reverse()
        return distance[end], path
    
    
    def findShortestPath_dfs(self, start, end):
#         if start == end: return 0, [start]
        current_path = [start]
        shortest_path = []
        self.findShortestPath_dfsHelper(start, end, current_path, shortest_path)
        return len(shortest_path), shortest_path[0]
    
    def findShortestPath_dfsHelper(self, start, end, current_path, shortest_path):
        if start == end:
            if not len(shortest_path): shortest_path.append(tuple(current_path))
            if len(current_path) < len(shortest_path[0]):
                shortest_path[0] = tuple(current_path)
            return
        for i in xrange(self.vertex_num):
            if self.adj_matrix[start][i] and i not in current_path:
                current_path.append(i)
                self.findShortestPath_dfsHelper(i, end, current_path, shortest_path)
                current_path.pop()

                


if __name__ == '__main__':
    vertex_num = 6
    mygraph = GraphAdjMatrix(7)
    for i in xrange(7):
        mygraph.add_vertex(i)
    edge_ls = [(0,4), (0,1), (0,5), #(0,6),
               (1,5), (1,2), (2,6), (2,3),
               (3,4), (3,6)]
    for edge in edge_ls:
        mygraph.add_edge(edge[0], edge[1])
#     mygraph.dfs(0)
#     mygraph.bfs(0)
    print mygraph.findShortestPath_dfs(3, 3)
    