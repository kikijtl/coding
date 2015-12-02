# Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.
# 
# For example:
# 
# Given s = "aabb", return ["abba", "baab"].
# 
# Given s = "abc", return [].
# 
# Hint:
# 
# If a palindromic permutation exists, we just need to generate the first half of the string.
# To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II or Next Permutation.

class Solution(object):
    def __init__(self):
        self.results = []
        
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        chars = []
        ch_set = sets.Set([])
        for ch in s:
            if ch not in ch_set:
                ch_set.add(ch)
            else:
                ch_set.remove(ch)
                chars.append(ch)
        if (len(s) % 2 == 0 and len(ch_set) > 0) \
            or (len(s) % 2 == 1 and len(ch_set) > 1):
            return []
        chars.sort()
        single = ''
        if ch_set:
            single = ch_set.pop()
        self._permutation(chars, [])
        for i in xrange(len(self.results)):
            result = self.results[i]
            reverse = reversed(result)
            result.append(single)
            result.extend(reverse)
            self.results[i] = ''.join(result)
        return self.results
    
    def _permutation(self, chars, curr_result):
        if not chars:
            self.results.append(copy.deepcopy(curr_result))
            return
        for i in xrange(len(chars)):
            if i > 0 and chars[i] == chars[i-1]:
                continue
            curr_result.append(chars[i])
            self._permutation(chars[:i]+chars[i+1:], curr_result)
            curr_result.pop()
        
    