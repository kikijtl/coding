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