# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], 
# reconstruct the itinerary in order. 
# All of the tickets belong to a man who departs from JFK. 
# Thus, the itinerary must begin with JFK.
# 
# Note:
# If there are multiple valid itineraries, 
# you should return the itinerary that has the smallest lexical order 
# when read as a single string. 
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets may form at least one valid itinerary.
# Example 1:
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
# Example 2:
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
# Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. 
# But it is larger in lexical order.


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # http://bookshadow.com/weblog/2016/02/05/leetcode-reconstruct-itinerary/
        # DFS
        table = {}
        for start, end in tickets:
            if start not in table:
                table[start] = [end]
            else:
                table[start].append(end)
            if end not in table:
                table[end] = []
        return self.findItineraryDfs('JFK', tickets, table)
    
    def findItineraryDfs(self, start, tickets, table):
        left = []   # record subroutines that contains the start
        right = []  # record subroutines that doesn't contain the start
        # The left should come before the right,
        # otherwise, tickets forming a travel circle are not traversed/used.
        for end in sorted(table[start]):
            if end not in table[start]:
                # which means this ticket is already used in previous dfs
                continue
            table[start].remove(end)
            subroutine = self.findItineraryDfs(end, tickets, table)
            if start in subroutine:
                left.extend(subroutine)
            else:
                right.extend(subroutine)
        return [start] + left + right
    

if __name__ == '__main__':
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print Solution().findItinerary(tickets)