# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
# 
# Note:
# Given target value is a floating point.
# You may assume k is always valid, that is: k <= total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
# 
# Hint:
# 
# Consider implement these two helper functions:
# getPredecessor(N), which returns the next smaller node to N.
# getSuccessor(N), which returns the next larger node to N.
# Try to assume that each node has a parent pointer, it makes the problem much easier.
# Without parent pointer we just need to keep track of the path from the root to the current node using a stack.
# You would need two stacks to track the path in finding predecessor and successor node separately.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        incr = []
        decr = []
        self._getInOrderStack(root, target, incr, increase=True)
        # Put all elements that are equal or smaller than target into incr stack in increasing order
        self._getInOrderStack(root, target, decr, increase=False)
        # Put all elements that are larger than target in decr stack in decreasing order
        result = []
        while len(result) < k:
            if not incr:
                result.append(decr.pop())
            elif not decr:
                result.append(incr.pop())
            elif abs(incr[-1]-target) < abs(decr[-1]-target):
                result.append(incr.pop())
            else:
                result.append(decr.pop())
        return result
    
    def _getInOrderStack(self, root, target, stack, increase=True):
        if not root: return
        if increase:
            self._getInOrderStack(root.left, target, stack, increase=True)
        else:
            self._getInOrderStack(root.right, target, stack, increase=False)
        if (increase and root.val > target) or (not increase and root.val <= target):
            return
        stack.append(root.val)
        if increase:
            self._getInOrderStack(root.right, target, stack, increase=True)
        else:
            self._getInOrderStack(root.left, target, stack, increase=False)
            
