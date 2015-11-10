# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
# 
# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
from compiler.ast import Node

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root: return float('inf')
        if target == root.val:
            return root.val
        elif target < root.val:
            left = self.closestValue(root.left, target)
            if abs(left-target) < root.val-target:
                return left
            else:
                return root.val
        else:
            right = self.closestValue(root.right, target)
            if abs(right-target) < target - root.val:
                return right
            else:
                return root.val
            
if __name__ == '__main__':
    root = TreeNode(1)
    node = TreeNode(2)
    root.right = node
    target = 3.428571
    print Solution().closestValue(root, target)