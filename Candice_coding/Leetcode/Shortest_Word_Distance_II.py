# This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?
# 
# Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.
# 
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# 
# Given word1 = ¡°coding¡±, word2 = ¡°practice¡±, return 3.
# Given word1 = "makes", word2 = "coding", return 1.
# 
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.indexMap = {}
        for i in xrange(len(words)):
            if words[i] not in self.indexMap:
                self.indexMap[words[i]] = [i]
            else:
                self.indexMap[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        distance = float('inf')
        i = j = 0
        index1 = self.indexMap[word1]
        index2 = self.indexMap[word2]
        while i < len(index1) and j < len(index2):
            distance = min(distance, abs(index2[j]-index1[i]))
            if distance == 1: return distance
            if index1[i] > index2[j]:
                j += 1
            else:
                i += 1
        return distance


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")