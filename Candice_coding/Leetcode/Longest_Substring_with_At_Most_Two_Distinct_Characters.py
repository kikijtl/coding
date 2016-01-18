# Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
# 
# For example, Given s = 'eceba',
# 
# T is "ece" which its length is 3.


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <=2:
            return len(s)
        table = {}
        start, end = 0, 0
        maxLen = 0
        while end < len(s):
            if s[end] in table:
                table[s[end]] += 1
                end += 1
                continue
            elif len(table) < 2:
                table[s[end]] = 1
                end += 1
                continue
            l = end - start
            maxLen = max(maxLen, l)
            table[s[start]] -= 1
            if table[s[start]] == 0:
                table.pop(s[start])
            start += 1
        return max(maxLen, end-start)
                
        