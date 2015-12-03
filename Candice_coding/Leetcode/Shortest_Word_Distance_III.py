# This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.
# 
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
# 
# word1 and word2 may be the same and they represent two individual words in the list.
# 
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# 
# Given word1 = ¡°makes¡±, word2 = ¡°coding¡±, return 1.
# Given word1 = "makes", word2 = "makes", return 3.
# 
# Note:
# You may assume word1 and word2 are both in the list.


class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        distance = len(words)
        index1 = index2 = None
        for i in xrange(len(words)):
            if words[i] == word1:
                # If word1 == word2, it is dealt as following
                # index2 will always be None
                if word1 == word2 and index1 != None:
                    distance = min(distance, abs(i-index1))
                index1 = i
            elif words[i] == word2:
                index2 = i
            if index1 != None and index2 != None:
                distance = min(distance, abs(index1-index2))
        return distance
