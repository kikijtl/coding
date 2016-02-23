# Given a 2D board and a list of words from the dictionary, find all words in the board.
# 
# Each word must be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once in a word.
# 
# For example,
# Given words = ["oath","pea","eat","rain"] and board =
# 
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# 
# You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
# 
# If the current candidate does not exist in all words prefix, you could stop backtracking immediately. 
# What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? 
# How about a Trie?

class TrieNode(object):
    def __init__(self):
        self.leaves = {}


class PrefixTree(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        root = self.root
        for char in word:
            if char not in root.leaves:
                root.leaves[char] = TrieNode()
            root = root.leaves[char]
        root.leaves[''] = None


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board:
            return []
        tree = PrefixTree()
        for word in words:
            tree.insert(word)
        m = len(board)
        n = len(board[0])
        visited = [[False for j in xrange(n)] for i in xrange(m)]
        result = set([])     # Using a dictionary or set to avoid repeated results
        for i in xrange(m):
            for j in xrange(n):
                self.findWordsHelper(board, tree.root, i, j, [], result, visited)
        return list(result)
    
    def findWordsHelper(self, board, node, i, j, tmpResult, result, visited):
        if not node or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
            return
        if board[i][j] not in node.leaves:
            return
        nextNode = node.leaves[board[i][j]]
        tmpResult.append(board[i][j])
        if '' in nextNode.leaves:
            # This is not a base case because 'aaa' and 'aaab' might all exists in the dictionary.
            word = ''.join(tmpResult)
            if word not in result:
                result.add(word)
        visited[i][j] = True
        self.findWordsHelper(board, nextNode, i-1, j, tmpResult, result, visited)
        self.findWordsHelper(board, nextNode, i+1, j, tmpResult, result, visited)
        self.findWordsHelper(board, nextNode, i, j-1, tmpResult, result, visited)
        self.findWordsHelper(board, nextNode, i, j+1, tmpResult, result, visited)
        visited[i][j] = False
        tmpResult.pop()
        return
    

if __name__ == '__main__':
#     board = ["oaan","etae","ihkr","iflv"]
#     words = ["oath","pea","eat","rain"]
    board = ["ab","aa"]
    words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
    print Solution().findWords(board, words)