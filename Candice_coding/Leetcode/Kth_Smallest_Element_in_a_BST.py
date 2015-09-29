# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def kthSmallest(self, root, k):
#         """
#         :type root: TreeNode
#         :type k: int
#         :rtype: int
#         """
#         small_ls = []
#         self._kthSmallestHelper(root, k, small_ls)
#         return small_ls[-1]
#     
#     
#     def _kthSmallestHelper(self, root, k, small_ls):
#         if not root:
#             return
#         self._kthSmallestHelper(root.left, k, small_ls)
#         if len(small_ls) == k:
#             return
#         small_ls.append(root.val)
#         self._kthSmallestHelper(root.right, k, small_ls)


class TreeNodeWithCount(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 1
        # count is used to count how many descendants the 
        # root has including itself.

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        root = self._buildTreeWithCount(root)
        return self._kthSmallestHelper(root, k)
        
        
    def _kthSmallestHelper(self, root, k):
        # Because k is valid, we don't have to check if root exists
        if root.left:
            if k == root.left.count + 1:
                return root.val
            elif k < root.left.count + 1:
                return self._kthSmallestHelper(root.left, k)
            else:
                return self._kthSmallestHelper(root.right, k-root.left.count-1)
        elif k == 1:
            return root.val
        else:
            return self._kthSmallestHelper(root.right, k-1)
            
        
        
    def _buildTreeWithCount(self, root):
        if not root:
            return
        left = self._buildTreeWithCount(root.left)
        new_root = TreeNodeWithCount(root.val)
        right = self._buildTreeWithCount(root.right)
        new_root.left = left
        new_root.right = right
        if left: new_root.count += left.count
        if right: new_root.count += right.count
        return new_root


if __name__ == '__main__':
#     node_vals = [1, 2, 3]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    solution = Solution()
    print solution.kthSmallest(root, 3)