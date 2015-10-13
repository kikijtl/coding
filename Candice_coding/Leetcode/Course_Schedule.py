'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.

click to show more hints.

Hints:
This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.
'''


import collections

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        in_edges = {}
        out_edges = {}
        tmp_ls = collections.deque([])
        graph_sort = []
        for i in xrange(numCourses):
            in_edges[i] = []
            out_edges[i] = []
        for i, j in prerequisites:
            in_edges[i].append(j)
            out_edges[j].append(i)
        for course in in_edges:
            if not in_edges[course]:
                tmp_ls.append(course)
        while tmp_ls:
            tmp = tmp_ls.popleft()
            graph_sort.append(tmp)
            for out_v in out_edges[tmp]:
                idx = in_edges[out_v].index(tmp)
                in_edges[out_v].pop(idx)
                if not in_edges[out_v]:
                    tmp_ls.append(out_v)
            out_edges.pop(tmp)
            in_edges.pop(tmp)
        if in_edges or out_edges:
            # There is a cycle in the graph
            # Impossible to finish all courses
            return []
        return graph_sort


if __name__ == '__main__':
    numCourses = 1
    prerequisites = []
    print Solution().findOrder(numCourses, prerequisites)        