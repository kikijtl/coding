# Given a complete binary tree, count the number of nodes.
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, 
# and all nodes in the last level are as far left as possible. 
# It can have between 1 and 2h nodes inclusive at the last level h.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        node = root
        level = 0
        while node.left:
            level += 1
            node = node.left
        lower = 2**level
        upper = 2**(level+1)
        # lower bound and upper bound for count
        # do binary search
        while lower < upper:
            middle = lower + (upper-lower) / 2
            if self.nthNodeExists(root, middle):
                lower = middle + 1
            else:
                upper = middle
        return lower - 1
        
        
    def nthNodeExists(self, root, n):
        '''Check if the nth node exists'''
        # root is the 0th node
        direction = []
        # a stack for recording nth node routine from root
        # 1 means go left, 0 means go right
        n -= 1
        while n > 0:
            direction.append(n%2)
            if n%2: n = (n-1) / 2
            else: n = (n - 2) / 2
        for i in range(len(direction)-1, -1, -1):
            if direction[i]: root = root.left
            else: root = root.right
        return root != None
    

if __name__ == '__main__':
    root = TreeNode(1)
    print Solution().countNodes(root)