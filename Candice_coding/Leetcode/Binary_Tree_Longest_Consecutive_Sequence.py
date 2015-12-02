# Given a binary tree, find the length of the longest consecutive sequence path.
# 
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
# 
# For example,
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_length = 0
        self.longestConsecutiveHelper(root)
        return self.max_length
    
    def longestConsecutiveHelper(self, root):
        if not root:
            return 0
        current_length = 1
        left_length = self.longestConsecutiveHelper(root.left)
        right_length = self.longestConsecutiveHelper(root.right)
        if root.left and root.left.val == root.val + 1:
            current_length = max(current_length, left_length+1)
        if root.right and root.right.val == root.val + 1:
            current_length = max(current_length, right_length+1)
        self.max_length = max(self.max_length, current_length, left_length, right_length)
        return current_length