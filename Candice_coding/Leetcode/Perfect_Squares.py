# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.


class Solution(object):
#     result = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
#         result = self.result
#         for i in xrange(len(result), n+1):
#             smallest = result[i-1] + 1
#             for k in xrange(1, int(i**0.5) + 1):
#                 smallest = min(smallest, result[i-k**2] + 1)
#             result.append(smallest)
#         return result[n]
        # The original version is time limit exceeded.
        result = [0]
        for i in xrange(1, n+1):
            smallest = result[i-1] + 1
            for k in xrange(1, int(i**0.5)+1):
                smallest = min(smallest, result[i-k**2]+1)
                # because i = i-k**2+k**2
            result.append(smallest)
        return result[n]


if __name__ == '__main__':
    n = 8285
    print Solution().numSquares(n)