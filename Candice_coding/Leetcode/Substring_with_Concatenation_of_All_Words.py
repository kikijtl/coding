# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
# 
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
# 
# You should return the indices: [0,9].
# (order does not matter).

class Solution(object):
    def findSubstring(self, s, words):
        '''
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        '''
        result = []
        wordSize = len(words[0])
        wordNumber = len(words)
        wordDict = {}
        for word in words:
            if word not in wordDict:
                wordDict[word] = 1
            else:
                wordDict[word] += 1
        for i in xrange(len(s)-wordNumber*wordSize+1):
            currentDict = {}
            j = 0
            while j < wordNumber:
                tmp = s[i+j*wordSize: i+j*wordSize+wordSize]
                if tmp not in wordDict:
                    # not a match
                    break
                if tmp not in currentDict:
                    currentDict[tmp] = 0
                currentDict[tmp] += 1
                if currentDict[tmp] > wordDict[tmp]:
                    # not a match
                    break
                j += 1
            if j == wordNumber:
                # means match found
                result.append(i)
        return result

if __name__ == "__main__":
    print Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])