# There is a fence with n posts, each post can be painted with one of the k colors.
# 
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# 
# Return the total number of ways you can paint the fence.
# 
# Note:
# n and k are non-negative integers.


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # f(i) indicates ways of painting i posts.
        # The (i+1)th post has two choices:
        # 1. use a different color from ith post, which is f(i)*(k-1)
        # 2. use the same color as ith post, which means the (i, i+1)th posts can be seen as one post and need to choose a different color from (i-1)th post, which is f(i-1)*(k-1)
        ways = [0, k]
        ways.append(k*(k-1)+k)
        for i in xrange(3, n+1):
            different = ways[i-1] * (k-1)
            same = ways[i-2] * (k-1)
            ways.append(different+same)
        return ways[n]