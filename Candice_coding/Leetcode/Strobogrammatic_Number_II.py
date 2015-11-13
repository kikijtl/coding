# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# 
# Find all strobogrammatic numbers that are of length = n.
# 
# For example,
# Given n = 2, return ["11","69","88","96"].

# Hint:
# Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.valid = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        return self._findStrobogrammaticHelper(n, n)
    
    def _findStrobogrammaticHelper(self, n, k):
        if k == 0: return ['']
        if k == 1: return ['0', '1', '8']
        result = []
        for num in self._findStrobogrammaticHelper(n, k-2):
            for digit in self.valid:
                if n != k or digit != '0':
                    result.append(digit + num + self.valid[digit])
        return result
    

if __name__ == '__main__':
    n = 2
    print Solution().findStrobogrammatic(n)