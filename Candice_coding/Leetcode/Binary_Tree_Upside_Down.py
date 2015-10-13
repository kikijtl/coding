'''
Given a binary tree where all the right nodes are either leaf nodes with a sibling 
(a left node that shares the same parent node) or empty, flip it upside down and 
turn it into a tree where the original right nodes turned into left leaf nodes. 
Return the new root.
 
For example:
Given a binary tree [1,2,3,4,5],
 
    1
   / \
  2   3
 / \
4   5
 
return the root of the binary tree [4,5,2,#,#,3,1].
 
   4
  / \
 5   2
    / \
   3   1  
'''

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        current = root
        parent = None
        parent_right = None
        while current:
            # First memorize current.left
            # current.left will be used for next loop
            current_left = current.left
            # The new left child is current.parent.right
            current.left = parent_right
            # Memorize current.right for next loop before change it
            parent_right = current.right
            # The new right child is current.parent
            current.right = parent
            # After finishing left and right children
            # Memorize current as parent for next loop
            parent = current
            # Ready for next loop
            current = current_left
        return parent
