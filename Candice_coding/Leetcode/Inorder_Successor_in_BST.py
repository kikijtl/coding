# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
# 
# Note: If the given node has no in-order successor in the tree, return null.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if p.right:
            current = p.right
            while current.left:
                current = current.left
            return current
        return self._inorderSuccessorHelper(root, p)
    
    def _inorderSuccessorHelper(self, root, p):
        if not root: return None
        if p == root.left:
            return root
        if p.val < root.val:
            successor = self._inorderSuccessorHelper(root.left, p)
            if successor: return successor
            else: return root
        if p.val > root.val:
            successor = self._inorderSuccessorHelper(root.right, p)
            if successor: return successor
        return None