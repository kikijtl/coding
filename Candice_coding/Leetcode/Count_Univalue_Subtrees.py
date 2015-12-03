# Given a binary tree, count the number of uni-value subtrees.
# 
# A Uni-value subtree means all nodes of the subtree have the same value.
# 
# For example:
# Given binary tree,
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
# return 4.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        is_unival, count = self._countUnivalSubtreesHelper(root, 0)
        return count
    
    def _countUnivalSubtreesHelper(self, root, count):
        if not root:
            return True, 0
        # if not root.left and not root.right:
        #     return True, 1
        is_unival = True
        unival_left, left_count = self._countUnivalSubtreesHelper(root.left, 0)
        unival_right, right_count = self._countUnivalSubtreesHelper(root.right, 0)
        if root.left:
            is_unival = is_unival and unival_left and root.val == root.left.val
        if root.right:
            is_unival = is_unival and unival_right and root.val == root.right.val
        if is_unival:
            return True, left_count + right_count + 1
        else:
            return False, left_count + right_count
            