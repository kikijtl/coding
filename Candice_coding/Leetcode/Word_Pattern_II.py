# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.
# 
# Examples:
# pattern = "abab", str = "redblueredblue" should return true.
# pattern = "aaaa", str = "asdasdasdasd" should return true.
# pattern = "aabb", str = "xyzabcxzyabc" should return false.
# Notes:
# You may assume both pattern and str contains only lowercase letters.

# Reference: http://blog.csdn.net/pointbreak1/article/details/49040879


# import sets


class Solution(object):
    def wordPatternMatch(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        used = {}
        table = {}
        return self._wordPatternMatchHelper(pattern, string, table, used)
    
    def _wordPatternMatchHelper(self, pattern, string, table, used):
        if len(pattern) == 0 and len(string) == 0:
            return True
        elif len(pattern) == 0 or len(string) == 0:
            return False
        if len(pattern) == 1:
            if pattern in table:
                if table[pattern] == string:
                    return True
                else:
                    return False
            elif string in used:
                return False
            else:
                return True
        if pattern[0] in table:
            if string.find(table[pattern[0]]) != 0:
                return False
            else:
                result = self._wordPatternMatchHelper(pattern[1:], string[len(table[pattern[0]]):], table, used)
                if result: return True
        else:
            deltaLen = len(string) - (len(pattern) - 1)
            for i in xrange(deltaLen):
                current = string[:i+1]
                if current in used:
                    continue
                used[current] = pattern[0]
                table[pattern[0]] = current
                result = self._wordPatternMatchHelper(pattern[1:], string[len(current):], table, used)
                if result: return True
                else:
                    used.pop(current)
                    table.pop(pattern[0])
            return False
        

if __name__ == '__main__':
    pattern = 'ab'
    string = 'aa'
    print Solution().wordPatternMatch(pattern, string)    