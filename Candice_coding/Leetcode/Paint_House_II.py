# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
# 
# The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.
# 
# Note:
# All costs are positive integers.
# 
# Follow up:
# Could you solve it in O(nk) runtime?


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        n = len(costs)
        k = len(costs[0])
        # if k < 2: return 0
        # pre_min to record the least cost and second least cost of the previous row
        # curr_min to record the two least cost of the current row
        pre_min = [float('inf'), float('inf')]
        curr_min = [float('inf'), float('inf')]
        for j in xrange(k):
            if costs[0][j] < pre_min[0]:
                pre_min[1] = pre_min[0]
                pre_min[0] = costs[0][j]
            elif costs[0][j] < pre_min[1]:
                pre_min[1] = costs[0][j]
        for i in xrange(1, n):
            for j in xrange(k):
                if costs[i-1][j] == pre_min[0]:
                    costs[i][j] += pre_min[1]
                else:
                    costs[i][j] += pre_min[0]
                if costs[i][j] < curr_min[0]:
                    curr_min[1] = curr_min[0]
                    curr_min[0] = costs[i][j]
                elif costs[i][j] < curr_min[1]:
                    curr_min[1] = costs[i][j]
            pre_min = copy.deepcopy(curr_min)
            curr_min = [float('inf'), float('inf')]
        return pre_min[0]