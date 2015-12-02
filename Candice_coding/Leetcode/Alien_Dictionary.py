# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
# 
# For example,
# Given the following words in dictionary,
# 
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".
# 
# Note:
# You may assume all letters are in lowercase.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.


class GraphNode(object):
    def __init__(self, val):
        self.val = val
        self.out_edges = []
        self.in_edges_num = 0

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        node_tb = {}
        for word in words:
            for ch in word:
                if ch not in node_tb:
                    node_tb[ch] = GraphNode(ch)
        # Set up graph
        for i in xrange(1, len(words)):
            for j in xrange(min(len(words[i]), len(words[i-1]))):
                if words[i][j] != words[i-1][j]:
                    node_tb[words[i-1][j]].out_edges.append(words[i][j])
                    node_tb[words[i][j]].in_edges_num += 1
                    break
        # Do topological sort
        result = []
        q = collections.deque([])
        for word in node_tb:
            if node_tb[word].in_edges_num == 0:
                q.append(node_tb[word])
        while q:
            node = q.popleft()
            node_tb.pop(node.val)
            result.append(node.val)
            for vertex_val in node.out_edges:
                vertex = node_tb[vertex_val]
                vertex.in_edges_num -= 1
                if vertex.in_edges_num == 0:
                    q.append(vertex)
        for key in node_tb:
            if node_tb[key].in_edges_num != 0:
                return ''
            else:
                result.append(key)
        return ''.join(result)
            
