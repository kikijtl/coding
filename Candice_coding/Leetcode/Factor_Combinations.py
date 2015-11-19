# Numbers can be regarded as product of its factors. For example,
# 
# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.
# 
# Note: 
# Each combination's factors must be sorted ascending, for example: The factors of 2 and 6 is [2, 6], not [6, 2].
# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.
# Examples: 
# input: 1
# output: 
# []
# input: 37
# output: 
# []
# input: 12
# output:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
# input: 32
# output:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]


import copy

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1: return []
        factors = []
        for i in xrange(2, n-1):
            if n % i == 0:
                factors.append(i)
        results = []
        self._getFactorsHelper(factors, n, [], results, 0)
        return results
    
    def _getFactorsHelper(self, factors, n, curr_result, results, idx):
        if n == 1:
            results.append(copy.deepcopy(curr_result))
            return
        for i in xrange(idx, len(factors)):
            if n % factors[i] != 0:
                continue
            curr_result.append(factors[i])
            self._getFactorsHelper(factors, n/factors[i], curr_result, results, i)
            curr_result.pop()
        

if __name__ == '__main__':
    n = 6
    print Solution().getFactors(n)